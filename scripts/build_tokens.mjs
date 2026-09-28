#!/usr/bin/env node
/**
 * Build design tokens from the Figma variable dump.
 *
 * Input : figma/variables.json   flat map { "background/default/white": "#ffffff", ... }
 *                                 (merged output of get_variable_defs over every section of
 *                                 the "Main Components (Full)" page)
 * Output: tokens/tokens.json      DTCG-style nested tokens ($value / $type)
 *         tokens/tokens.css       CSS custom properties  (--salla-<path>)
 *         tokens/tokens.flat.json flat map name -> resolved value (handy for tooling)
 *         tokens/tailwind.preset.cjs Tailwind preset (colors, spacing, radius, fontSize, boxShadow)
 *
 * Run: node scripts/build_tokens.mjs
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const INPUT = path.join(ROOT, "figma", "variables.json");
const OUT = path.join(ROOT, "tokens");

const raw = JSON.parse(fs.readFileSync(INPUT, "utf8"));

// ---------------------------------------------------------------- helpers
const isColor = (v) => /^#[0-9a-f]{6}([0-9a-f]{2})?$/i.test(v);
const isNumber = (v) => /^-?\d+(\.\d+)?$/.test(v);
const kebab = (s) =>
  s
    .replace(/\$/g, "")
    .replace(/\(.*?\)/g, (m) => "-" + m.slice(1, -1))
    .replace(/[^a-zA-Z0-9]+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "")
    .toLowerCase();

/** Legacy / duplicated collections that we keep but flag as deprecated. */
const LEGACY = [/^0\d-? ?/, /^Spacing ?- ?/, /^Spacing-/, /^Radius ?- ?/, /^Radius-/, /^Component Heading$/, /^White$/, /^fl-purple$/, /^Map Marker/, /^UI Colors/, /^fill$/, /^border$/];
const isLegacy = (name) => LEGACY.some((re) => re.test(name));

function resolve(v, depth = 0) {
  // a bare variable reference, e.g. "shadow/xs/color" or "Typography/Size/md"
  if (typeof v === "string" && raw[v] !== undefined && depth < 8) return resolve(raw[v], depth + 1);
  return v;
}

function parseFont(str) {
  // Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/md, weight: 500, lineHeight: typography/line-height (Descreptive)/6, letterSpacing: 0)
  const inner = str.slice(5, -1);
  const get = (key) => {
    const m = inner.match(new RegExp(`${key}: ("[^"]*"|[^,]+)`));
    return m ? m[1].replace(/^"|"$/g, "").trim() : undefined;
  };
  const family = resolve(get("family"));
  const style = resolve(get("style"));
  const size = Number(resolve(get("size")));
  const weight = Number(resolve(get("weight")));
  const lineHeight = Number(resolve(get("lineHeight")));
  const letterSpacing = Number(resolve(get("letterSpacing")) || 0);
  return { fontFamily: family, fontStyle: style, fontSize: size, fontWeight: weight, lineHeight, letterSpacing };
}

function parseEffects(str) {
  return str.split("; ").map((e) => {
    const inner = e.slice(7, -1); // strip "Effect(" ... ")"
    const get = (key) => {
      const m = inner.match(new RegExp(`${key}: (\\([^)]*\\)|[^,]+)`));
      return m ? m[1].trim() : undefined;
    };
    const type = get("type");
    const color = resolve(get("color"));
    const off = (get("offset") || "(0, 0)").slice(1, -1).split(",").map((s) => Number(resolve(s.trim())));
    const radius = Number(resolve(get("radius")));
    const spread = Number(resolve(get("spread")));
    return { type, color, offsetX: off[0], offsetY: off[1], blur: radius, spread };
  });
}

const shadowCss = (layers) => layers.map((l) => `${l.offsetX}px ${l.offsetY}px ${l.blur}px ${l.spread}px ${l.color}`).join(", ");
const fontCss = (f) => `${f.fontWeight} ${f.fontSize}px/${f.lineHeight}px "${f.fontFamily}"`;

// ---------------------------------------------------------------- classify
const nested = {};
const flat = {};
const css = [];
const tw = { colors: {}, spacing: {}, borderRadius: {}, fontSize: {}, boxShadow: {}, fontFamily: {}, fontWeight: {} };

function setNested(pathParts, token) {
  let cur = nested;
  for (const p of pathParts.slice(0, -1)) cur = cur[p] ??= {};
  cur[pathParts.at(-1)] = token;
}

const entries = Object.entries(raw).sort(([a], [b]) => a.localeCompare(b));
for (const [name, value] of entries) {
  const parts = name.split("/").map((s) => s.trim());
  const legacy = isLegacy(name);
  const cssName = `--salla-${kebab(name)}`;
  let token;

  if (value.startsWith("Font(")) {
    const f = parseFont(value);
    token = { $type: "typography", $value: f };
    css.push(`  ${cssName}: ${fontCss(f)};`);
    flat[name] = fontCss(f);
  } else if (value.startsWith("Effect(")) {
    const layers = parseEffects(value);
    token = { $type: "shadow", $value: layers };
    css.push(`  ${cssName}: ${shadowCss(layers)};`);
    flat[name] = shadowCss(layers);
    if (/^Shadows\//.test(name)) tw.boxShadow[kebab(parts.at(-1))] = shadowCss(layers);
  } else if (isColor(value)) {
    token = { $type: "color", $value: value.toLowerCase() };
    css.push(`  ${cssName}: ${value.toLowerCase()};`);
    flat[name] = value.toLowerCase();
    if (!legacy && !/^shadow\//.test(name)) tw.colors[kebab(name)] = value.toLowerCase();
  } else if (isNumber(value)) {
    const n = Number(value);
    const lower = name.toLowerCase();
    const isDim = /spacing|radius|size|line-height|blur|spread|position/.test(lower);
    token = { $type: isDim ? "dimension" : "number", $value: isDim ? `${n}px` : n };
    css.push(`  ${cssName}: ${isDim ? n + "px" : n};`);
    flat[name] = isDim ? `${n}px` : n;
    if (!legacy) {
      if (/^spacing\//i.test(name)) tw.spacing[kebab(name.replace(/^spacing\/(sizes\/)?/i, ""))] = `${n}px`;
      if (/^radius\//i.test(name)) tw.borderRadius[kebab(name.replace(/^radius\/(sizes\/)?/i, ""))] = `${n}px`;
      if (/^Typography\/Size\//.test(name)) tw.fontSize[kebab(parts.at(-1))] = `${n}px`;
    }
  } else {
    // strings: font family / weight names
    const isWeight = /Weight/.test(name);
    token = { $type: isWeight ? "fontWeight" : "string", $value: value };
    css.push(`  ${cssName}: ${isWeight ? value : JSON.stringify(value)};`);
    flat[name] = value;
    if (/Family/.test(name)) tw.fontFamily.sans = [value, "system-ui", "sans-serif"];
    if (isWeight) tw.fontWeight[kebab(parts.at(-1))] = { Regular: 400, Medium: 500, Bold: 700 }[value] ?? value;
  }
  if (legacy) token.$deprecated = "Legacy collection kept for reference; prefer the semantic tokens.";
  token.$extensions = { "com.figma.variableName": name };
  setNested(legacy ? ["legacy", ...parts] : parts, token);
}

// ---------------------------------------------------------------- docs/foundations.md
const md = [];
md.push("# Foundations", "", "Generated by `scripts/build_tokens.mjs` from `figma/variables.json` (Figma variables of *Merchant - Storybook DS*).",
  "Each row shows the Figma variable name, the generated CSS custom property and the value.", "");
function table(title, filter, fmt = (v) => `\`${v}\``) {
  const rows = entries.filter(([n, v]) => filter(n, v) && !isLegacy(n));
  if (!rows.length) return;
  md.push(`## ${title}`, "", "| Figma variable | CSS variable | Value |", "|---|---|---|");
  for (const [n] of rows) md.push(`| \`${n}\` | \`--salla-${kebab(n)}\` | ${fmt(flat[n])} |`);
  md.push("");
}
const swatch = (v) => `<img src="https://placehold.co/14x14/${String(v).slice(1, 7)}/${String(v).slice(1, 7)}.png" alt="" /> \`${v}\``;
table("Colors — brand & primary", (n, v) => isColor(v) && /^(primary|secondary|background\/primary|background\/secondary|text\/primary|text\/secondary|border\/primary|border\/seconadry|icon\/primary|foreground\/primary)/.test(n), swatch);
table("Colors — backgrounds", (n, v) => isColor(v) && /^background\/(default|page|supporting)/.test(n), swatch);
table("Colors — status (semantic)", (n, v) => isColor(v) && /^(background\/status|text\/status|border\/status|danger|success|info|warning|icon\/status)/.test(n), swatch);
table("Colors — text, icons & foreground", (n, v) => isColor(v) && /^(text\/gray|text\/Upgrade|text\/supporting|icon\/(?!primary|status)|foreground\/(?!primary))/.test(n), swatch);
table("Colors — borders", (n, v) => isColor(v) && /^border\/(?!primary|seconadry|status)/.test(n), swatch);
table("Colors — other palettes", (n, v) => isColor(v) && /^(color\/|gray\/|white\/|fill$|Base)/.test(n), swatch);
table("Spacing", (n, v) => isNumber(v) && /^spacing\//i.test(n));
table("Radius", (n, v) => isNumber(v) && /^radius\//i.test(n));
table("Typography — scale", (n, v) => /^Typography\//.test(n) || /^typography\/line-height/.test(n));
table("Typography — text styles", (n, v) => v.startsWith("Font("));
table("Shadows", (n, v) => v.startsWith("Effect(") || /^shadow\//.test(n));
md.push("## Legacy collections", "", "Variables from older collections (`01- Primary`, `06 - Dark`, `07- Light Theme`, `Spacing - *`, `Radius-*`, map markers…) are kept under `legacy` in `tokens/tokens.json` and emitted as CSS variables for completeness, but new work should use the semantic names above.", "");
fs.mkdirSync(path.join(ROOT, "docs"), { recursive: true });
fs.writeFileSync(path.join(ROOT, "docs", "foundations.md"), md.join("\n") + "\n");

fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(path.join(OUT, "tokens.json"), JSON.stringify(nested, null, 2) + "\n");
fs.writeFileSync(path.join(OUT, "tokens.flat.json"), JSON.stringify(flat, null, 2) + "\n");
fs.writeFileSync(
  path.join(OUT, "tokens.css"),
  `/* Salla Design System tokens — generated by scripts/build_tokens.mjs from figma/variables.json. Do not edit by hand. */\n:root {\n${css.join("\n")}\n}\n`
);
fs.writeFileSync(
  path.join(OUT, "tailwind.preset.cjs"),
  `/* Salla Design System — Tailwind preset. Generated by scripts/build_tokens.mjs. */\nmodule.exports = {\n  theme: {\n    extend: ${JSON.stringify(tw, null, 6).replace(/\n/g, "\n    ")}\n  }\n};\n`
);
console.log(`tokens: ${entries.length} variables -> ${css.length} css vars; tailwind colors=${Object.keys(tw.colors).length} spacing=${Object.keys(tw.spacing).length} radius=${Object.keys(tw.borderRadius).length} shadows=${Object.keys(tw.boxShadow).length}`);
