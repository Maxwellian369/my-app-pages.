# PRISM by Maxwellian

A static, responsive website for **maxwellian.help**, ready for GitHub Pages.

## Upload to GitHub Pages

1. Open the existing GitHub repository that currently publishes `maxwellian.help`.
2. Replace the old site files with the contents of this folder. Keep `CNAME` and `.nojekyll` in the repository root.
3. Commit the changes to the branch used by GitHub Pages.
4. In **Settings → Pages**, choose **Deploy from a branch**, then select that branch and the **/(root)** folder.
5. Keep **Custom domain** set to `maxwellian.help`. Your existing DNS records can remain unchanged.

There is no build command, package installation, framework, backend, or environment variable to configure.

## Preview locally

From this folder, run any static web server. For example:

```sh
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

## Included

- `index.html` — PRISM product, methodology, founder submission, and Drive Connector page
- `privacy.html` — existing Drive Connector privacy content with the new design
- `terms.html` — existing Drive Connector terms with the new design
- `404.html` — custom not-found page
- `styles.css` — responsive layout, typography, and interaction states
- `src/main.js` — accessible mobile navigation and workspace tabs
- `CNAME` — custom domain configuration for GitHub Pages
- `robots.txt` and `sitemap.xml` — search-engine discovery
- `favicon.svg` and `og-image.png` — browser and social-sharing artwork

The Northstar Systems workspace is explicitly labeled as an illustrative demo. It does not claim to display live customer analysis.

## External destinations

The company-submission buttons retain the existing Maxwellian Decile Hub form. The AI Fundraising Kit retains its existing Notion destination. External links open in a separate tab.

## Fonts

Antic Didone and IBM Plex are served by Google Fonts and are distributed under the SIL Open Font License. System-font fallbacks are included.
