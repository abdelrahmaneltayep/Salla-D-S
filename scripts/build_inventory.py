#!/usr/bin/env python3
"""Build the component inventory from a Figma metadata snapshot.

Input : figma/snapshots/main-components.xml  (get_metadata dump of the
        "Main Components (Full)" page of the Merchant - Storybook DS file)
Output: figma/components.json           machine-readable inventory
        docs/components/README.md       index of all sections
        docs/components/<section>.md    one page per section
        icons/figma-icon-names.json     names of the Icons/Filled + Icons/Outline symbols
        icons/flags.json                flag symbol names

Run:  python3 scripts/build_inventory.py
"""
import json
import os
import re
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAPSHOT = os.path.join(ROOT, "figma", "snapshots", "main-components.xml")
FILE_KEY = "dnmyqzYKK9dUJjVHuIWMDS"  # branch that holds the component page
MAIN_FILE_KEY = "zuGhoKg2BaBIYUreKuSBGY"

ICON_FRAMES = {"Icons/Filled", "Icons/Outline"}
FLAG_FRAME = "Flag"


def slug(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "untitled"


def parse_variant(name: str):
    """'Variant=--primary, Size=--lg-48px' -> {'Variant': '--primary', ...}"""
    props = {}
    for part in name.split(", "):
        if "=" in part:
            k, v = part.split("=", 1)
            props[k.strip()] = v.strip()
    return props


def figma_url(file_key, node_id):
    return f"https://www.figma.com/design/{file_key}/?node-id={node_id.replace(':', '-')}"


def collect_sets(top):
    """Return component sets (elements with symbol children) under a top-level node."""
    sets = []
    for el in top.iter():
        if el is top:
            continue
        syms = [k for k in el if k.tag == "symbol"]
        if syms:
            sets.append((el, syms))
    return sets


def main():
    tree = ET.parse(SNAPSHOT)
    root = tree.getroot()
    inventory = {"fileKey": FILE_KEY, "mainFileKey": MAIN_FILE_KEY, "page": {"id": root.get("id"), "name": root.get("name")}, "sections": []}
    icon_names = {}
    flags = []

    for top in root:
        name = top.get("name")
        section = {
            "id": top.get("id"),
            "name": name,
            "kind": top.tag,
            "url": figma_url(FILE_KEY, top.get("id")),
            "componentSets": [],
            "standaloneComponents": [],
        }
        if name in ICON_FRAMES:
            icon_names[name] = sorted(s.get("name") for s in top.iter("symbol"))
            section["symbolCount"] = len(icon_names[name])
            inventory["sections"].append(section)
            continue
        if name == FLAG_FRAME:
            flags = sorted(s.get("name") for s in top.iter("symbol"))
            section["symbolCount"] = len(flags)
            inventory["sections"].append(section)
            continue

        # direct symbols with no set (e.g. the Button frame holds 441 symbols directly)
        direct = [k for k in top if k.tag == "symbol"]
        if direct and all("=" in (k.get("name") or "") for k in direct):
            # treat the frame itself as a component set
            sets = [(top, direct)]
        else:
            sets = collect_sets(top)
            for k in direct:
                section["standaloneComponents"].append({
                    "id": k.get("id"), "name": k.get("name"),
                    "width": float(k.get("width", 0)), "height": float(k.get("height", 0)),
                    "url": figma_url(FILE_KEY, k.get("id")),
                })

        for el, syms in sets:
            props = {}
            variants = []
            for s in syms:
                p = parse_variant(s.get("name") or "")
                for k, v in p.items():
                    props.setdefault(k, set()).add(v)
                variants.append({
                    "id": s.get("id"), "name": s.get("name"), "props": p,
                    "width": float(s.get("width", 0)), "height": float(s.get("height", 0)),
                })
            section["componentSets"].append({
                "id": el.get("id"),
                "name": el.get("name"),
                "internal": (el.get("name") or "").startswith("_"),
                "url": figma_url(FILE_KEY, el.get("id")),
                "variantCount": len(variants),
                "properties": {k: sorted(v) for k, v in props.items()},
                "variants": variants,
            })
        inventory["sections"].append(section)

    os.makedirs(os.path.join(ROOT, "figma"), exist_ok=True)
    with open(os.path.join(ROOT, "figma", "components.json"), "w") as f:
        json.dump(inventory, f, indent=2, ensure_ascii=False)

    os.makedirs(os.path.join(ROOT, "icons"), exist_ok=True)
    with open(os.path.join(ROOT, "icons", "figma-icon-names.json"), "w") as f:
        json.dump(icon_names, f, indent=2, ensure_ascii=False)
    with open(os.path.join(ROOT, "icons", "flags.json"), "w") as f:
        json.dump(flags, f, indent=2, ensure_ascii=False)

    # ---- docs ----
    docs = os.path.join(ROOT, "docs", "components")
    os.makedirs(docs, exist_ok=True)
    index = ["# Component inventory", "",
             "Generated from the Figma library **Merchant - Storybook DS**, page *Main Components (Full)*.",
             "Regenerate with `python3 scripts/build_inventory.py`.", "",
             "| Section | Component sets | Variants | Figma |", "|---|---:|---:|---|"]
    for sec in inventory["sections"]:
        n_sets = len(sec["componentSets"])
        n_var = sum(cs["variantCount"] for cs in sec["componentSets"]) + len(sec["standaloneComponents"]) + sec.get("symbolCount", 0)
        page = f"{slug(sec['name'])}.md"
        index.append(f"| [{sec['name']}]({page}) | {n_sets} | {n_var} | [open]({sec['url']}) |")
        lines = [f"# {sec['name']}", "",
                 f"Figma node `{sec['id']}` · [open in Figma]({sec['url']})", ""]
        img = f"{slug(sec['name'])}.png"
        if os.path.exists(os.path.join(ROOT, "docs", "images", img)):
            lines += [f"![{sec['name']}](../images/{img})", ""]
        if sec.get("symbolCount"):
            lines.append(f"This frame holds **{sec['symbolCount']}** symbols. Names are listed in "
                         + ("`icons/figma-icon-names.json`." if sec["name"] in ICON_FRAMES else "`icons/flags.json`."))
        for cs in sec["componentSets"]:
            tag = " *(internal, underscore-prefixed)*" if cs["internal"] else ""
            lines += [f"## {cs['name']}{tag}", "",
                      f"Node `{cs['id']}` · {cs['variantCount']} variants · [open]({cs['url']})", ""]
            if cs["properties"]:
                lines += ["| Property | Values |", "|---|---|"]
                for k, vals in cs["properties"].items():
                    lines.append(f"| `{k}` | " + ", ".join(f"`{v}`" for v in vals) + " |")
                lines.append("")
            lines += ["<details><summary>All variants</summary>", "", "| Variant | Node | Size |", "|---|---|---|"]
            for v in cs["variants"]:
                lines.append(f"| {v['name']} | `{v['id']}` | {v['width']:g}×{v['height']:g} |")
            lines += ["", "</details>", ""]
        if sec["standaloneComponents"]:
            lines += ["## Standalone components", "", "| Name | Node | Size |", "|---|---|---|"]
            for c in sec["standaloneComponents"]:
                lines.append(f"| {c['name']} | `{c['id']}` | {c['width']:g}×{c['height']:g} |")
            lines.append("")
        with open(os.path.join(docs, page), "w") as f:
            f.write("\n".join(lines))
    with open(os.path.join(docs, "README.md"), "w") as f:
        f.write("\n".join(index) + "\n")

    total_sets = sum(len(s["componentSets"]) for s in inventory["sections"])
    print(f"sections={len(inventory['sections'])} componentSets={total_sets} "
          f"icons={ {k: len(v) for k, v in icon_names.items()} } flags={len(flags)}")


if __name__ == "__main__":
    main()
