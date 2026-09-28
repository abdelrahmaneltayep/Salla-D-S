#!/usr/bin/env python3
"""Generate demo/components.html — a live gallery of every design-system component.

Sources: storybook/components.json + storybook/captures/stories/**.html (real story markup),
         tokens/tokens.flat.json (foundations), icons/manifest.json, demo/assets/salla-logo.svg.
The page loads the Twilight runtime (storybook/static) so every s-* element is the production component.

Run: python3 scripts/build_components_demo.py
"""
import html as H
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAP = os.path.join(ROOT, "storybook", "captures")
comps = json.load(open(os.path.join(ROOT, "storybook", "components.json")))
tokens = json.load(open(os.path.join(ROOT, "tokens", "tokens.flat.json")))
logo = open(os.path.join(ROOT, "demo", "assets", "salla-logo.svg")).read().strip().replace("<svg ", '<svg class="logo" role="img" aria-label="سلة" ', 1)
# Header: reuse the Figma-accurate title bar from demo/index.html verbatim (styles in demo/header.css)
_demo = open(os.path.join(ROOT, "demo", "index.html"), encoding="utf-8").read()
hd_top = re.search(r'    <div class="hd-top">.*?\n    </div>\n', _demo, re.S).group(0)
hd_top = hd_top.replace('class="hd-tab is-active"', 'class="hd-tab"').replace('class="hd-tab" href="#"><span class="icon" data-icon="home-01">', 'class="hd-tab is-active" href="#"><span class="icon" data-icon="home-01">')
hd_top = hd_top.replace('<a href="#" aria-label="الرئيسية">', '<a href="../demo/index.html" aria-label="الرئيسية">')

# Figma design references (exports under figma/exports/, updated 2026-09-28)
FIGMA_REF = {
    "Components/Button": [("button/button.png", "Button — كل الأنواع والحالات (Figma)")],
    "Components/Tag": [("tag/tag.png", "Tag — 7 أنماط × filled / subtle")],
    "Components/Breadcrumbs": [("breadcrumb/breadcrumb.png", "Breadcrumb — desktop + mobile، عربي/إنجليزي")],
    "Components/Checkbox": [("checkbox/checkboxfield.png", "checkboxfield — default / disabled / info / tooltip")],
    "Components/Tabs": [("tabs/radiotext-tabs.png", "RadioText tabs (chips) — 4 أنماط"), ("tabs/secondary-tabs-list.png", "Secondary Tabs List"), ("tabs/header-secondary-tabs.png", "Header Secondary Tabs — contained / plain"), ("tabs/primary-tabs-list.png", "Primary Tabs List — dashboard"), ("tabs/header-primary-tabs.png", "Header Primary Tabs — states")],
    "Components/Calendar": [("calendar/calendar-time-date.png", "Calendar — تاريخ + وقت"), ("calendar/time.png", "Time input — states"), ("calendar/big-calendar-items.png", "Day cells"), ("calendar/date-item.png", "Date item"), ("calendar/time-item.png", "Time item")],
    "Components/AlertBox": [("alertbox/alertbox.png", "Alertbox — 6 أنماط × inline / white × title on/off (Figma)")],
    "Components/Avatar": [("avatar/avatar.png", "Avatar — sizes × circular/rectangular × image/fallback"), ("avatar/avatar-stack.png", "AvatarStack — overlapping / compact"), ("avatar/avatar-with-text.png", "AvatarWithText"), ("avatar/avatar-placeholder-images.png", "Placeholder images"), ("avatar/bank-placeholder-images.png", "Bank placeholder")],
    "Components/Accordion": [("accordion/accordion.png", "Accordion"), ("accordion/accordion-header.png", "Accordion header — states"), ("accordion/accordion-icon.png", "Accordion icon")],
    "Components/Qty": [("qty/quantity.png", "Quantity — states"), ("qty/counter.png", "Counter — compact / default"), ("qty/quantity-hotreload.png", "Quantity hot-reload")],
    "Components/OTP": [("otp/single-digit.png", "Single digit — states")],
    "Components/Telephone Input": [("tel-input/phone-input.png", "Phone input — states, AR/EN")],
    "Components/Textarea": [("textarea/textarea.png", "Textarea — plain / rich text, states")],
    "Components/Input": [("input/text-input.png", "Text input — 7 states × error, AR/EN"), ("input/search-input.png", "Search input"), ("input/input-with-image.png", "Input with image"), ("input/input-with-button.png", "Input with button"), ("input/input-counter.png", "Input counter"), ("input/amount-input.png", "Amount input"), ("input/email-input.png", "Email input"), ("input/password-input.png", "Password input — hidden / requirements")],
    "Components/Select": [("select/dropdown-single.png", "Dropdown single — with search / add new"), ("select/dropdown-multiple.png", "Dropdown multiple"), ("select/basic-dropdown-single.png", "Basic dropdown single"), ("select/basic-dropdown-multiple.png", "Basic dropdown multiple")],
    "Components/Table": [("table/desktop-default.png", "Table — Default"), ("table/desktop-tabs.png", "Table — Tabs"), ("table/desktop-title.png", "Table — Title"), ("table/desktop-filter-results.png", "Table — Filter results"), ("table/desktop-selected.png", "Table — Selected (bulk banner)"), ("table/desktop-more-menu.png", "Table — More menu"), ("table/desktop-no-results.png", "Table — No results"), ("table/desktop-scroll-down.png", "Table — Scroll (sticky header)"), ("table/mobile-default.png", "Table — Mobile"), ("table/mobile-selected.png", "Table — Mobile selected"), ("table/mobile-no-results.png", "Table — Mobile empty")],
}

# Figma-only components (no Storybook story yet): title, slug, refs, note
FIGMA_ONLY = [
    ("Toast", "toast", [("toast/toast.png", "Toast — default / success / danger / warning / info, with action")], "لا يوجد له قصة في Storybook؛ الرن تايم يحمّل مكتبة toastify (<code>--toastify-*</code>) لعرض الإشعارات."),
]

# stories that need a note or trimming
LIMIT = {"Components/Editor": 4, "Components/LingualField": 6, "Components/Maps": 1}
NOTES = {
    "Components/Maps": "يحتاج مفتاح Google Maps (<code>api-key</code>) ليعرض الخريطة.",
    "Components/Editor": "عُرضت 4 قصص من 12 (المحرر ثقيل). بقية القصص في docs/storybook/editor.md.",
    "Components/LingualField": "عُرضت 6 قصص من 18. بقية القصص في docs/storybook/lingualfield.md.",
    "Components/IconPicker": "الأيقونات داخل المنتقي تعتمد على خط Hugeicons من CDN سلة.",
}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def clean(markup):
    """Strip Storybook-only bits from captured markup so it re-hydrates cleanly."""
    markup = markup.split("\n", 1)[-1]  # drop the "<!-- title / name -->" comment line
    markup = re.sub(r"<style>\s*(?:\[?#?\[?id\*?=?\"?story--[^{]*\{[^}]*\}\s*)+</style>", "", markup, flags=re.S)
    markup = re.sub(r"<style>[^<]*story--[^<]*</style>", "", markup, flags=re.S)
    markup = re.sub(r'\s@[a-z]+="[^"]*"(?:\s[^\s=<>]*=""|\s"[^"]*"=""|\s[a-z:,]+="[^"]*")*', "", markup)  # broken @event attrs
    markup = re.sub(r'\s(?:hydrated|ltr)(?=[\s"])', "", markup)
    markup = re.sub(r'class="\s*"', "", markup)
    markup = re.sub(r"\sautofocus(?:=\"[^\"]*\")?", "", markup)
    return markup.strip()


# ---------------------------------------------------------------- foundations
def swatches(title, pred):
    rows = [(n, v) for n, v in tokens.items() if isinstance(v, str) and v.startswith("#") and pred(n)]
    if not rows:
        return ""
    cells = "".join(
        f'<div class="sw"><span class="sw__c" style="background:{v}"></span><span class="sw__n">{H.escape(n)}</span><span class="sw__v">{v}</span></div>'
        for n, v in rows)
    return f'<h3>{title}</h3><div class="sw-grid">{cells}</div>'


colors = "".join([
    swatches("Primary & secondary", lambda n: re.match(r"^(primary|secondary|background/primary|background/secondary|text/primary|text/secondary|border/primary|border/seconadry|icon/primary|foreground/primary)", n) is not None),
    swatches("Backgrounds", lambda n: re.match(r"^background/(default|page)", n) is not None),
    swatches("Status", lambda n: re.match(r"^(danger|success|info|warning)/", n) is not None),
    swatches("Status backgrounds / text / borders", lambda n: re.match(r"^(background|text|border)/status", n) is not None),
    swatches("Text, icons, borders", lambda n: re.match(r"^(text/gray|icon/|border/(default|hover|gray|White|Light|focus)|foreground/gray)", n) is not None),
    swatches("Supporting colors", lambda n: re.match(r"^(background/supporting|text/supporting|color/support|text/Upgrade|foreground/Upgrade|border/upgrade)", n) is not None),
])
type_styles = "".join(
    f'<div class="ty"><div class="ty__s" style="font:{tokens[n]}">سلة تُمكّن التجار — Salla empowers merchants 0123</div><div class="ty__n">{H.escape(n)} <span>{tokens[n]}</span></div></div>'
    for n in ["Bold/$text-2xl", "Bold/$text-xl", "Bold/$text-lg", "Medium/$text-lg", "Bold/$text-base", "Medium/$text-base", "Regular/$text-base", "Bold/$text-sm", "Medium/$text-sm", "Regular/$text-sm", "Bold/$text-xs", "Medium/$text-xs", "Regular/$text-xs", "Regular/$text-xxs"] if n in tokens)
spacing = "".join(
    f'<div class="sp"><span class="sp__b" style="width:{tokens[n]}"></span><span class="sp__n">{H.escape(n)}</span><span class="sp__v">{tokens[n]}</span></div>'
    for n in ["spacing/6xs", "spacing/5xs", "spacing/4xs", "spacing/3xs", "spacing/2xs", "spacing/xs", "spacing/sm", "spacing/base", "spacing/2xl", "spacing/7xl", "Spacing/Sizes/13xl"] if n in tokens)
radius = "".join(
    f'<div class="rd"><span class="rd__b" style="border-radius:{tokens[n]}"></span><span class="sp__n">{H.escape(n)}</span><span class="sp__v">{tokens[n]}</span></div>'
    for n in ["radius/sm", "radius/md", "radius/xl", "Radius/Sizes/3xl", "radius/full"] if n in tokens)
shadows = "".join(
    f'<div class="sh"><span class="sh__b" style="box-shadow:{tokens[n]}"></span><span class="sp__n">{H.escape(n)}</span></div>'
    for n in ["Shadows/xs", "Shadows/sm", "Shadows/base", "Shadows/lg"] if n in tokens)
icon_names = ["home-01", "delivery-box-02", "shirt-01", "marketing", "chart-breakout-square", "pie-chart", "search-01", "notification-01", "message-01", "settings-01", "add-01", "delete-02", "edit-02", "copy-01", "printer", "filter-horizontal", "sorting-01", "calendar-03", "user", "shopping-cart-02", "credit-card", "truck-delivery", "checkmark-circle-02", "alert-circle"]
icons_html = "".join(f'<div class="ic"><span class="icon" data-icon="{n}"></span><span class="icon icon--f" data-icon-f="{n}"></span><span class="ic__n">{n}</span></div>' for n in icon_names)
icon_count = json.load(open(os.path.join(ROOT, "icons", "manifest.json")))["count"]

# ---------------------------------------------------------------- components
nav = []
sections = []
total = 0
for c in comps:
    title = c["title"].replace("Components/", "").replace("Design System/", "DS · ")
    sid = "c-" + c["slug"]
    stories = c["stories"]
    lim = LIMIT.get(c["title"])
    shown = stories[:lim] if lim else stories
    tags = " ".join(f"<code>&lt;{t}&gt;</code>" for t in c["tags"])
    nav.append(f'<a href="#{sid}" data-nav="{sid}">{H.escape(title)}<span>{len(stories)}</span></a>')
    props = ""
    if c["argTypes"]:
        rows = "".join(
            f"<tr><td><code>{H.escape(k)}</code></td><td>{H.escape(', '.join(str(o) for o in (v.get('options') or [])) or (v.get('control') if isinstance(v.get('control'), str) else (v.get('control') or {}).get('type', '') or ''))}</td><td>{H.escape(str(((v.get('table') or {}).get('defaultValue') or {}).get('summary', '') or ''))}</td><td>{H.escape((v.get('description') or '').replace(chr(10), ' '))}</td></tr>"
            for k, v in c["argTypes"].items())
        props = f'<details class="props"><summary>الخصائص ({len(c["argTypes"])})</summary><div class="tbl"><table><thead><tr><th>Prop</th><th>Control / options</th><th>Default</th><th>Description</th></tr></thead><tbody>{rows}</tbody></table></div></details>'
    cards = []
    for s in shown:
        if not s.get("html"):
            continue
        markup = clean(open(os.path.join(CAP, s["html"])).read())
        if not markup:
            continue
        total += 1
        args = {k: v for k, v in (s.get("args") or {}).items() if isinstance(v, (str, int, float, bool)) and k != "style"}
        args_html = f'<details class="args"><summary>args</summary><pre>{H.escape(json.dumps(args, ensure_ascii=False, indent=1))}</pre></details>' if args else ""
        wide = " card--wide" if len(markup) > 2500 or "s-table" in markup or "s-editor" in markup or "s-calendar" in markup or "s-uploader" in markup or "s-tabs-group" in markup or "s-panel" in markup or "s-accordion" in markup or "s-maps" in markup or "s-lingual" in markup or "s-modal" in markup else ""
        cards.append(f'<article class="card{wide}" data-story="{H.escape(s["id"])}"><header><h4>{H.escape(s["name"])}</h4><code>{H.escape(s["id"])}</code></header><div class="card__body">{markup}</div>{args_html}</article>')
    note = f'<p class="note">{NOTES[c["title"]]}</p>' if c["title"] in NOTES else ""
    refs = FIGMA_REF.get(c["title"])
    if refs:
        note += '<div class="figref"><h3>التصميم في Figma <span>figma/exports/ · 2026-09-28</span></h3><div class="figref__row">' + "".join(
            f'<figure><a href="../figma/exports/{f}" target="_blank"><img loading="lazy" src="../figma/exports/{f}" alt="{H.escape(cap)}" /></a><figcaption>{H.escape(cap)}</figcaption></figure>' for f, cap in refs) + "</div></div>"
    desc = f'<p class="desc" dir="auto">{H.escape(c["description"])}</p>' if c.get("description") else ""
    sections.append(f'''<section class="comp" id="{sid}" data-title="{H.escape(title.lower())}">
  <div class="comp__head"><h2>{H.escape(title)}</h2><div class="tags">{tags}</div><a class="doclink" href="../docs/storybook/{c["slug"]}.md">docs/storybook/{c["slug"]}.md</a></div>
  {desc}{note}{props}
  <div class="grid">{"".join(cards)}</div>
</section>''')

for title, sl, refs, note in FIGMA_ONLY:
    sid = "c-" + sl
    nav.append(f'<a href="#{sid}" data-nav="{sid}">{H.escape(title)}<span>Figma</span></a>')
    cards = "".join(f'<figure><a href="../figma/exports/{f}" target="_blank"><img loading="lazy" src="../figma/exports/{f}" alt="{H.escape(cap)}" /></a><figcaption>{H.escape(cap)}</figcaption></figure>' for f, cap in refs)
    sections.append(f'''<section class="comp" id="{sid}" data-title="{H.escape(title.lower())} figma">
  <div class="comp__head"><h2>{H.escape(title)}</h2><div class="tags"><code>Figma only</code></div><a class="doclink" href="../figma/exports/{sl}/">figma/exports/{sl}/</a></div>
  <p class="note">{note}</p>
  <div class="figref"><h3>التصميم في Figma <span>figma/exports/ · 2026-09-28</span></h3><div class="figref__row">{cards}</div></div>
</section>''')

page = f'''<!doctype html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Salla DS — معرض المكونات</title>
  <link rel="stylesheet" href="../fonts/pingarlt.css" />
  <link rel="stylesheet" href="https://cdn.salla.network/fonts/hugeicons-font.min.css" />
  <link rel="stylesheet" href="../storybook/static/styles.css" />
  <script type="module" src="../storybook/static/admin-ui.esm.js"></script>
  <link rel="stylesheet" href="../tokens/tokens.css" />
  <link rel="stylesheet" href="header.css" />
  <style>
    html {{ background: var(--salla-background-default-page, #f4f4f4); scroll-behavior: smooth; }}
    body {{ margin: 0; font-family: PingARLT, "PT Sans", system-ui, sans-serif; color: var(--salla-text-gray-dark, #333); font-size: 14px; }}
    .icon {{ display: inline-flex; width: 20px; height: 20px; vertical-align: middle; }} .icon svg {{ width: 100%; height: 100%; }}
    .hd-sub__tab.lnk {{ color: var(--salla-text-gray-light, #666); }}
    .hd-toggle {{ font: inherit; cursor: pointer; height: 32px; padding: 0 12px; border-radius: 12px; border: 1px solid var(--salla-border-seconadry, #a4ffe5); background: #fff; color: #004956; font-size: 12px; font-weight: 500; }}
    .g-title {{ display: flex; align-items: baseline; gap: 12px; padding: 16px var(--hd-pad, 64px) 0; }}
    .g-title h1 {{ margin: 0; font-size: 24px; line-height: 32px; font-weight: 700; color: var(--salla-text-primary-primary, #004956); }}
    .g-title span {{ color: var(--salla-text-gray-lighter, #737373); font-size: 13px; }}
    .g-wrap {{ display: grid; grid-template-columns: 240px minmax(0, 1fr); gap: 24px; padding: 24px 32px 96px; max-width: 1600px; margin: 0 auto; }}
    .g-side {{ position: sticky; top: 16px; align-self: start; max-height: calc(100vh - 32px); overflow: auto; background: #fff; border-radius: 8px; padding: 8px; box-shadow: var(--salla-shadows-xs); }}
    .g-side input {{ width: 100%; box-sizing: border-box; font: inherit; padding: 8px 10px; border: 1px solid var(--salla-border-default, #eee); border-radius: 8px; margin-bottom: 6px; }}
    .g-side a {{ display: flex; justify-content: space-between; padding: 7px 10px; border-radius: 6px; color: var(--salla-text-gray-light, #666); text-decoration: none; font-size: 13px; }}
    .g-side a span {{ color: var(--salla-text-gray-lighter, #737373); font-size: 12px; }}
    .g-side a:hover, .g-side a.is-active {{ background: var(--salla-background-secondary-lighter, #e6fff9); color: var(--salla-text-primary-primary, #004956); }}
    .g-side .h {{ padding: 10px 10px 4px; font-size: 11px; letter-spacing: .04em; color: var(--salla-text-gray-lighter, #737373); text-transform: uppercase; }}
    .comp {{ background: #fff; border-radius: 8px; padding: 20px 24px 24px; margin-bottom: 24px; box-shadow: var(--salla-shadows-xs); scroll-margin-top: 84px; }}
    .comp__head {{ display: flex; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 8px; }}
    .comp h2 {{ margin: 0; font-size: 20px; font-weight: 700; color: var(--salla-text-primary-primary, #004956); }}
    .tags code, .card code, .props code {{ font-size: 12px; background: var(--salla-background-default-neutrals, #f4f4f4); border-radius: 4px; padding: 2px 6px; color: #555; direction: ltr; unicode-bidi: embed; }}
    .doclink {{ margin-inline-start: auto; font-size: 12px; color: var(--salla-text-primary-link, #004956); direction: ltr; }}
    .desc {{ margin: 0 0 8px; color: var(--salla-text-gray-light, #666); }}
    .note {{ margin: 0 0 8px; padding: 8px 12px; border-radius: 6px; background: var(--salla-background-status-warning-lighter, #fff9eb); color: var(--salla-text-status-warning-darker, #8f5f22); font-size: 13px; }}
    details.props {{ margin: 8px 0 14px; }} details.props summary {{ cursor: pointer; color: var(--salla-text-primary-link, #004956); font-size: 13px; }}
    .tbl {{ overflow-x: auto; margin-top: 8px; }} .tbl table {{ width: 100%; border-collapse: collapse; font-size: 12px; }} .tbl th, .tbl td {{ text-align: right; padding: 6px 8px; border-bottom: 1px solid var(--salla-border-default, #eee); vertical-align: top; }} .tbl th {{ color: #737373; font-weight: 500; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 16px; align-items: start; }}
    .card {{ border: 1px solid var(--salla-border-default, #eee); border-radius: 8px; min-width: 0; background: #fff; }}
    .card--wide {{ grid-column: 1 / -1; }}
    .card header {{ display: flex; align-items: center; gap: 8px; padding: 8px 12px; border-bottom: 1px solid var(--salla-border-default, #eee); background: var(--salla-background-default-neutrals-light, #fcfcfc); border-radius: 8px 8px 0 0; }}
    .card h4 {{ margin: 0; font-size: 13px; font-weight: 500; flex: 1; }}
    .card__body {{ padding: 16px; overflow-x: auto; min-height: 48px; }}
    .card__body > * {{ max-width: 100%; }}
    details.args {{ border-top: 1px solid var(--salla-border-default, #eee); padding: 6px 12px; }} details.args summary {{ font-size: 12px; color: #737373; cursor: pointer; }} details.args pre {{ direction: ltr; text-align: left; font-size: 11px; margin: 6px 0 0; white-space: pre-wrap; }}
    .figref {{ margin: 8px 0 16px; padding: 12px; border-radius: 8px; background: var(--salla-background-default-neutrals-light, #fcfcfc); border: 1px dashed var(--salla-border-hover, #ddd); }}
    .figref h3 {{ margin: 0 0 10px; font-size: 13px; color: #555; }} .figref h3 span {{ color: #737373; font-weight: 400; margin-inline-start: 8px; direction: ltr; unicode-bidi: embed; }}
    .figref__row {{ display: flex; gap: 12px; overflow-x: auto; padding-bottom: 4px; }}
    .figref figure {{ margin: 0; flex: none; width: 360px; max-width: 100%; }} .figref img {{ width: 100%; height: 200px; object-fit: contain; object-position: top; background: #fff; border: 1px solid var(--salla-border-default, #eee); border-radius: 6px; display: block; }}
    .figref figcaption {{ font-size: 11px; color: #737373; margin-top: 4px; }}
    /* foundations */
    .fd h3 {{ font-size: 14px; margin: 18px 0 8px; color: #555; }}
    .sw-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(170px, 1fr)); gap: 8px; }}
    .sw {{ display: grid; grid-template-columns: 28px 1fr; grid-template-rows: auto auto; column-gap: 8px; align-items: center; font-size: 11px; }}
    .sw__c {{ grid-row: 1 / 3; width: 28px; height: 28px; border-radius: 6px; border: 1px solid rgba(0,0,0,.08); }}
    .sw__n {{ color: #333; direction: ltr; text-align: right; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }} .sw__v {{ color: #737373; direction: ltr; text-align: right; }}
    .ty {{ display: flex; align-items: baseline; gap: 16px; padding: 6px 0; border-bottom: 1px dashed var(--salla-border-default, #eee); }} .ty__s {{ flex: 1; color: #333; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }} .ty__n {{ font-size: 11px; color: #737373; direction: ltr; text-align: right; white-space: nowrap; }} .ty__n span {{ display: block; color: #bbb; }}
    .sp, .rd, .sh {{ display: flex; align-items: center; gap: 12px; padding: 4px 0; font-size: 12px; }} .sp__b {{ height: 16px; background: var(--salla-background-secondary-seconadry, #a4ffe5); border-radius: 2px; }} .sp__n {{ width: 170px; direction: ltr; text-align: right; color: #333; }} .sp__v {{ color: #737373; }}
    .rd__b {{ width: 48px; height: 32px; background: #fff; border: 2px solid var(--salla-border-primary, #004956); }} .sh__b {{ width: 64px; height: 40px; background: #fff; border-radius: 8px; margin: 8px 0; }}
    .ic-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap: 8px; }} .ic {{ display: flex; align-items: center; gap: 6px; font-size: 11px; color: #555; }} .ic .icon {{ width: 24px; height: 24px; color: #004956; }} .ic__n {{ direction: ltr; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
    @media (max-width: 900px) {{ .g-wrap {{ grid-template-columns: 1fr; padding: 16px; }} .g-side {{ position: static; max-height: none; }} .g-title {{ padding: 16px 16px 0; }} .g-title span {{ display: none; }} }}
  </style>
</head>
<body>
  <!-- Header: Figma "Header" component — title bar shared with demo/index.html, gallery subcategory row -->
  <header>
{hd_top}
    <div class="hd-sub">
      <nav class="hd-sub__tabs" aria-label="صفحات العرض">
        <a class="hd-sub__tab is-active" href="#">معرض المكونات</a>
        <a class="hd-sub__tab lnk" href="index.html">شاشة الطلبات</a>
        <a class="hd-sub__tab lnk" href="../docs/components/">التوثيق</a>
      </nav>
      <div class="hd-sub__btns">
        <button type="button" class="hd-toggle" id="dirToggle" title="تبديل اتجاه الصفحة">LTR ⇄ RTL</button>
        <a class="hd-moshammer" href="#"><span class="hd-moshammer__spark"><span class="icon" data-icon="sparkles"></span></span> مشمر <span class="icon chev" data-icon="arrow-left-01"></span></a>
        <a class="hd-help" href="#" title="مركز المساعدة"><span class="icon" data-icon="help-circle"></span></a>
      </div>
    </div>
  </header>
  <div class="g-title"><h1>معرض مكونات نظام التصميم</h1><span>Twilight · {len(comps)} مكوّن · {total} قصة حيّة من Storybook</span></div>
  <div class="g-wrap">
    <aside class="g-side">
      <input id="filter" type="search" placeholder="ابحث عن مكوّن…" aria-label="بحث" />
      <div class="h">الأساسيات</div>
      <a href="#f-colors" data-nav="f-colors">الألوان<span>{sum(1 for v in tokens.values() if isinstance(v, str) and v.startswith('#'))}</span></a>
      <a href="#f-type" data-nav="f-type">الخطوط<span>14</span></a>
      <a href="#f-space" data-nav="f-space">المسافات والزوايا والظلال</a>
      <a href="#f-icons" data-nav="f-icons">الأيقونات<span>{icon_count}</span></a>
      <div class="h">المكوّنات</div>
      {"".join(nav)}
    </aside>
    <main>
      <section class="comp fd" id="f-colors" data-title="colors الألوان tokens"><div class="comp__head"><h2>الألوان</h2><a class="doclink" href="../docs/foundations.md">docs/foundations.md</a></div><p class="desc">متغيرات Figma (Merchant - Storybook DS) كما هي في <code>tokens/tokens.css</code>.</p>{colors}</section>
      <section class="comp fd" id="f-type" data-title="typography الخطوط fonts"><div class="comp__head"><h2>الخطوط</h2><a class="doclink" href="../fonts/README.md">fonts/README.md</a></div><p class="desc">Ping AR + LT — أنماط النصوص من Figma.</p>{type_styles}</section>
      <section class="comp fd" id="f-space" data-title="spacing radius shadows المسافات"><div class="comp__head"><h2>المسافات والزوايا والظلال</h2></div><h3>Spacing</h3>{spacing}<h3>Radius</h3>{radius}<h3>Shadows</h3><div style="display:flex;gap:24px;flex-wrap:wrap">{shadows}</div></section>
      <section class="comp fd" id="f-icons" data-title="icons الأيقونات hugeicons"><div class="comp__head"><h2>الأيقونات</h2><a class="doclink" href="../icons/README.md">icons/README.md</a></div><p class="desc">{icon_count} أيقونة بنمطي outline و filled (Hugeicons) — عيّنة:</p><div class="ic-grid">{icons_html}</div></section>
      {"".join(sections)}
    </main>
  </div>
  <script>
    const ICON_BASE = '../icons/svg/outline/', ICON_BASE_F = '../icons/svg/filled/';
    const put = async (el, url) => {{ try {{ const r = await fetch(url); if (r.ok) el.innerHTML = (await r.text()).replace(/<\\?xml[^>]*>/, ''); }} catch (e) {{}} }};
    document.querySelectorAll('[data-icon]').forEach(el => put(el, ICON_BASE + el.dataset.icon + '.svg'));
    document.querySelectorAll('[data-icon-f]').forEach(el => put(el, ICON_BASE_F + el.dataset.iconF + '.svg'));
    // some stories focus themselves on hydration (OTP); keep the page at the top on load
    if (!location.hash) {{ let n = 0; const t = setInterval(() => {{ document.activeElement?.blur?.(); window.scrollTo(0, 0); if (++n > 20) clearInterval(t); }}, 150); }}
    // filter
    const filter = document.getElementById('filter');
    filter.addEventListener('input', () => {{
      const q = filter.value.trim().toLowerCase();
      document.querySelectorAll('section.comp').forEach(s => {{ s.hidden = q && !s.dataset.title.includes(q) && !s.id.includes(q); }});
      document.querySelectorAll('.g-side a[data-nav]').forEach(a => {{ const s = document.getElementById(a.dataset.nav); a.hidden = s ? s.hidden : false; }});
    }});
    // active nav on scroll
    const links = [...document.querySelectorAll('.g-side a[data-nav]')];
    const io = new IntersectionObserver(es => es.forEach(e => {{ if (e.isIntersecting) links.forEach(a => a.classList.toggle('is-active', a.dataset.nav === e.target.id)); }}), {{ rootMargin: '-80px 0px -70% 0px' }});
    document.querySelectorAll('section.comp').forEach(s => io.observe(s));
    // direction toggle: flip dir and re-create the components so they re-read it
    document.getElementById('dirToggle').addEventListener('click', () => {{
      const root = document.documentElement; root.dir = root.dir === 'rtl' ? 'ltr' : 'rtl';
      document.querySelectorAll('.card__body').forEach(b => {{ const h = b.innerHTML; b.innerHTML = ''; requestAnimationFrame(() => b.innerHTML = h); }});
    }});
  </script>
</body>
</html>
'''
out = os.path.join(ROOT, "demo", "components.html")
open(out, "w").write(page)
print(f"components={len(comps)} stories={total} size={os.path.getsize(out)//1024}KB -> {out}")
