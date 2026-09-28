#!/usr/bin/env node
/**
 * Capture the rendered markup of every story in the public Storybook
 * (https://dashboard-ui-components.pages.dev/) into storybook/<component>/<story>.html,
 * plus storybook/index.json (the Storybook story index) and storybook/README.md.
 *
 * Requires Playwright's chromium:  npm i -D playwright  (or use an existing install).
 * Run:  node scripts/sync_storybook.mjs [storybookUrl]
 *
 * NOTE: this script could not be exercised from the environment that authored it
 * (the Storybook host is blocked by that environment's network policy). It follows the
 * standard Storybook 7/8 layout: /index.json lists stories, and
 * /iframe.html?id=<storyId>&viewMode=story renders one story into #storybook-root.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const BASE = (process.argv[2] || "https://dashboard-ui-components.pages.dev").replace(/\/$/, "");
const OUT = path.join(ROOT, "storybook");

const slug = (s) => s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

async function main() {
  const { chromium } = await import("playwright");
  const res = await fetch(`${BASE}/index.json`);
  if (!res.ok) throw new Error(`index.json -> HTTP ${res.status}`);
  const index = await res.json();
  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(path.join(OUT, "index.json"), JSON.stringify(index, null, 2));

  const entries = Object.values(index.entries ?? index.stories ?? {}).filter((e) => (e.type ?? "story") === "story");
  console.log(`${entries.length} stories`);

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const lines = ["# Storybook snapshots", "", `Source: ${BASE}`, "", "| Component | Story | File |", "|---|---|---|"];
  for (const e of entries) {
    const url = `${BASE}/iframe.html?id=${encodeURIComponent(e.id)}&viewMode=story`;
    await page.goto(url, { waitUntil: "networkidle" });
    await page.waitForSelector("#storybook-root", { timeout: 15000 }).catch(() => {});
    const html = await page.evaluate(() => document.querySelector("#storybook-root")?.innerHTML ?? "");
    const dir = path.join(OUT, slug(e.title));
    fs.mkdirSync(dir, { recursive: true });
    const file = path.join(dir, `${slug(e.name)}.html`);
    fs.writeFileSync(file, `<!-- ${e.title} / ${e.name} — ${url} -->\n${html.trim()}\n`);
    lines.push(`| ${e.title} | ${e.name} | \`${path.relative(ROOT, file)}\` |`);
    console.log("saved", path.relative(ROOT, file));
  }
  await browser.close();
  fs.writeFileSync(path.join(OUT, "README.md"), lines.join("\n") + "\n");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
