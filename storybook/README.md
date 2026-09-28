# Storybook snapshots

Target: the public Twilight component Storybook at <https://dashboard-ui-components.pages.dev/>.

This folder is empty on purpose. The host was denied by the network policy of the environment that
assembled this repository, so no story markup could be captured. Run `node scripts/sync_storybook.mjs`
from a machine that can reach the site (needs Playwright's Chromium) to populate
`storybook/<component>/<story>.html` with the rendered markup of every story and `storybook/index.json`
with the story index.
