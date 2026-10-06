# UX map skill for Claude Code

Give Claude a URL and it walks the site in a browser, then builds a UX map of how visitors get from their first visit to the goal: a purchase on commercial sites, or a completed task (find, understand, act) on free and public-information sites.

Every claim is tagged as seen in the browser, stated by the site, or not reached, so the map shows what the site actually does rather than what such sites usually do.

## What you get

- Personas, splitting who uses the site from who pays or acts
- Journey stages
- A plain-language infographic for non-technical readers: an animated HTML page with a Portrait / Landscape switch, plus PNG images of both layouts (rendered with Edge or Chrome)
- Two flowcharts: public site and logged-in app, or desktop and phone
- A journey map table with friction and fixes per stage
- Findings and fixes, sorted by priority
- Metrics to track per stage
- A checklist of what was not verified

The map is delivered as a shareable doc when a docs connector is available, otherwise as a markdown file.

## Install

In Claude Code:

```
/plugin marketplace add BedarAsad/UX-Map
/plugin install ux-map@arced-skills
```

Updates arrive automatically when the plugin version changes.

## Use

```
/ux-map:ux-map https://example.com
```

It also starts on its own when you ask things like "map the customer journey for this site" or "where do visitors drop off before buying?"

## Requirements and limits

- **A browser Claude can control:** the built-in browser in the Claude desktop app, or Claude in Chrome. Without one, the skill can't walk the site.
- **Logged-in pages:** Claude never creates accounts, types passwords or pays. For logged-in pages you sign in yourself in the browser, and Claude walks read-only, checking a dashboard counter before and after to show nothing changed.
- **Shareable doc:** needs a docs connector; otherwise you get markdown.

## License

MIT. See [LICENSE](LICENSE).
