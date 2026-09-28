#!/usr/bin/env python3
"""Build component docs from the captured Storybook stories.

Input : storybook/captures/stories.json   (written by scripts/capture_storybook.mjs)
        storybook/captures/stories/<component>/<story>.html|png
        figma/components.json              (for the Figma <-> Storybook map)
Output: storybook/components.json          per-component API (argTypes), tags, stories
        docs/storybook/README.md           index
        docs/storybook/<component>.md      props table + every story (args, screenshot, markup)
        docs/component-map.md              Figma section <-> Storybook component <-> s-* tag

Run: python3 scripts/build_storybook_docs.py
"""
import json
import os
import re
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAP = os.path.join(ROOT, "storybook", "captures")
DOCS = os.path.join(ROOT, "docs", "storybook")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def fmt_type(at):
    t = at.get("type")
    if isinstance(t, dict):
        return t.get("name", "")
    c = at.get("control")
    if isinstance(c, dict):
        return c.get("type", "")
    return c or ""


def main():
    stories = json.load(open(os.path.join(CAP, "stories.json")))
    comps = OrderedDict()
    for s in stories:
        title = s["title"]
        c = comps.setdefault(title, {"title": title, "slug": slug(title.replace("Components/", "")), "importPath": s.get("importPath"),
                                     "tags": set(), "argTypes": OrderedDict(), "description": None, "stories": []})
        c["tags"].update(s.get("tags_used") or [])
        for k, v in (s.get("argTypes") or {}).items():
            if k not in c["argTypes"] and (v.get("description") or v.get("options") or v.get("control")):
                c["argTypes"][k] = v
        if not c["description"] and s.get("componentDescription"):
            c["description"] = s["componentDescription"]
        c["stories"].append({"id": s["id"], "name": s["name"], "args": s.get("args"), "html": s.get("htmlFile"), "png": s.get("pngFile"), "error": s.get("error")})

    os.makedirs(DOCS, exist_ok=True)
    index = ["# Storybook components", "",
             "Captured from the Twilight component Storybook (Storybook 8.6, `@storybook/html`, Stencil web components).",
             "Each page lists the component's props (from the story `argTypes`), and every story with its args, a screenshot and the",
             "rendered light-DOM markup. Regenerate with `node scripts/capture_storybook.mjs` then `python3 scripts/build_storybook_docs.py`.", "",
             "| Component | Tags | Stories | Props |", "|---|---|---:|---:|"]
    out_json = []
    for c in comps.values():
        tags = sorted(c["tags"])
        page = f"{c['slug']}.md"
        index.append(f"| [{c['title'].replace('Components/', '')}]({page}) | {' '.join('`<'+t+'>`' for t in tags)} | {len(c['stories'])} | {len(c['argTypes'])} |")
        lines = [f"# {c['title'].replace('Components/', '')}", "", f"Storybook title `{c['title']}` · source `{c['importPath']}`", ""]
        if tags:
            lines += ["Tags rendered: " + ", ".join(f"`<{t}>`" for t in tags), ""]
        if c["description"]:
            lines += [c["description"], ""]
        if c["argTypes"]:
            lines += ["## Props", "", "| Prop | Type / control | Options | Default | Description |", "|---|---|---|---|---|"]
            for k, v in c["argTypes"].items():
                opts = ", ".join(f"`{o}`" for o in (v.get("options") or []))
                default = ((v.get("table") or {}).get("defaultValue") or {}).get("summary", "")
                desc = (v.get("description") or "").replace("\n", " ").replace("|", "\\|")
                lines.append(f"| `{k}` | {fmt_type(v)} | {opts} | {('`'+str(default)+'`') if default not in ('', None) else ''} | {desc} |")
            lines.append("")
        lines += ["## Stories", ""]
        for st in c["stories"]:
            lines += [f"### {st['name']}", "", f"Story id `{st['id']}`", ""]
            if st.get("error"):
                lines += [f"> capture error: {st['error']}", ""]
            if st.get("png"):
                lines += [f"![{st['name']}](../../storybook/captures/{st['png']})", ""]
            args = {k: v for k, v in (st.get("args") or {}).items() if not callable(v)}
            if args:
                lines += ["Args:", "", "```json", json.dumps(args, ensure_ascii=False, indent=2), "```", ""]
            if st.get("html"):
                html = open(os.path.join(CAP, st["html"])).read().split("\n", 1)[-1].strip()
                if html:
                    lines += ["<details><summary>Rendered markup</summary>", "", "```html", html, "```", "", "</details>", ""]
        open(os.path.join(DOCS, page), "w").write("\n".join(lines))
        out_json.append({"title": c["title"], "slug": c["slug"], "importPath": c["importPath"], "tags": tags, "description": c["description"],
                         "argTypes": c["argTypes"], "stories": c["stories"]})
    open(os.path.join(DOCS, "README.md"), "w").write("\n".join(index) + "\n")
    json.dump(out_json, open(os.path.join(ROOT, "storybook", "components.json"), "w"), indent=1, ensure_ascii=False)

    # ---- Figma <-> Storybook map
    figma = json.load(open(os.path.join(ROOT, "figma", "components.json")))
    fig_sections = [s["name"] for s in figma["sections"]]
    MAP = [  # (Figma section, Storybook component title(s), main tag, note)
        ("Header", [], "", "app shell header; no public Storybook component"),
        ("Bread crumb", ["Components/Breadcrumbs"], "s-breadcrumbs", ""),
        ("Button", ["Components/Button", "Components/ButtonsGroup"], "s-button", "Figma Variant→`theme`, Appearance→`outlined`/link, Size→`size`, Layout→`layout`"),
        ("check Box", ["Components/Checkbox"], "s-checkbox", ""),
        ("radio Buttton", ["Components/Radio"], "s-radio", "radioImage/radioColor are radio variants"),
        ("Toggle", ["Components/Toggle"], "s-toggle", ""),
        ("Loader", ["Components/Loader", "Components/Skeleton"], "s-loader", ""),
        ("Status", ["Components/Tag"], "s-tag", "status badge = tag with dot"),
        ("Avatar", ["Components/Avatar"], "s-avatar", ""),
        ("Alertbox", ["Components/AlertBox"], "s-alert-box", ""),
        ("Inputs", ["Components/Input", "Components/Textarea", "Components/Select", "Components/Telephone Input", "Components/OTP", "Components/Qty", "Components/Uploader", "Components/LingualField", "Components/Editor", "Components/Tags Input", "Components/ColorPicker", "Components/IconPicker", "Components/Range Slider", "Components/Rate", "Components/Calendar"], "s-input", "one Figma section covers every field type"),
        ("searchbar", ["Components/Input"], "s-input", "search variant"),
        ("Maps", ["Components/Maps"], "s-maps", ""),
        ("Side menu", ["Components/Tabs"], "s-tabs-group", "vertical tabs"),
        ("More Menu", ["Components/Dropdown"], "s-dropdown", ""),
        ("Drop Down List", ["Components/Dropdown", "Components/Select", "Components/Item"], "s-dropdown", "list items = `s-list-item`"),
        ("Table", ["Components/Table"], "s-table", ""),
        ("Steps", [], "", "no public Storybook component"),
        ("Learn More", ["Components/Panel"], "s-panel", "panel with media"),
        ("Icons/Filled", ["Components/Icon"], "s-icon", "see icons/"),
        ("Icons/Outline", ["Components/Icon"], "s-icon", "see icons/"),
        ("Illustrations Collection", ["Components/Placeholder"], "s-placeholder", "empty states"),
        ("Action Buttons", ["Components/ButtonsGroup"], "s-buttons-group", ""),
        ("Products Management", ["Components/Table", "Components/Panel"], "", "page composition"),
        ("Header Primary Tabs", [], "", "app shell"),
        ("Flag", ["Components/Telephone Input"], "s-tel-input", "country flags"),
        ("Social media icons", ["Components/Icon"], "s-icon", ""),
        ("Illustration", ["Components/Placeholder"], "s-placeholder", ""),
    ]
    sb_titles = {c["title"] for c in comps.values()}
    lines = ["# Figma ↔ Storybook component map", "",
             "How the sections of the Figma page *Main Components (Full)* relate to the Twilight Storybook components and `s-*` tags.",
             "Storybook components not listed against a Figma section: " + ", ".join(sorted(f"`{t.replace('Components/', '')}`" for t in sb_titles - {t for _, ts, _, _ in MAP for t in ts})) + ".", "",
             "| Figma section | Storybook component(s) | Main tag | Note |", "|---|---|---|---|"]
    for fig, sbs, tag, note in MAP:
        if fig not in fig_sections:
            continue
        sb_links = ", ".join(f"[{t.replace('Components/', '')}](storybook/{slug(t.replace('Components/', ''))}.md)" for t in sbs) or "—"
        lines.append(f"| [{fig}](components/{slug(fig)}.md) | {sb_links} | {('`<'+tag+'>`') if tag else ''} | {note} |")
    open(os.path.join(ROOT, "docs", "component-map.md"), "w").write("\n".join(lines) + "\n")
    print(f"components={len(comps)} stories={len(stories)} errors={sum(1 for s in stories if s.get('error'))}")


if __name__ == "__main__":
    main()
