# Surf Japan

[Surf Japan](https://pyotr777.github.io/surfing/) is an independent, non-commercial guide to surfing Japan’s Pacific coast. It currently covers Chiba and Shonan: their coastal areas, surf spots, boards, sea safety and the way the coastline shapes swell.

The site is made and maintained by surfing enthusiasts. It has no paid rankings or sponsored listings, and it will grow gradually as new areas and spots are researched. Conditions, access and safety can change quickly; always check the forecast, local rules and the beach before going out.

## Built with Panehe

<a href="https://github.com/pyotr777/panehe"><img src="rawsite/img/panehe-wood.png" alt="Panehe logo" width="180"></a>

The site is generated with [Panehe](https://github.com/pyotr777/panehe), a small static-site generator that lets HTML pages use Python during the build. Shared navigation, language links, area cards, maps and data panels are assembled from the source files; the published site itself is plain static HTML, CSS, JavaScript and images.

## Languages and structure

Surf Japan is available in English, Russian and Japanese. English pages use the ordinary filename; Russian and Japanese versions add `_ru` and `_ja` before the extension:

```text
index.html        index_ru.html        index_ja.html
spots/asahi/index.html
spots/asahi/index_ru.html
spots/asahi/index_ja.html
```

The area hierarchy follows the visitor’s path through the guide:

```text
spots/                       illustrated overview and area cards
spots/<area>/                area profile and map of its spots
spots/<area>/<spot>/         spot page, when a detailed page is available
```

The current overview areas are Asahi, Sosa, Sakuta, Ichinomiya, Katsuura and South Boso. They are navigation areas, not a fixed list of all the spots covered by the project.

## Local build

The source site is in `rawsite/`; `surfing/` is generated output and is not committed. You need Python 3, [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/), and a local copy of Panehe:

```bash
python3 /path/to/panehe.py rawsite -o surfing
```

For this working copy, run the command from `surfjapan/`:

```bash
../.venv-surfjapan/bin/python ../panehe.py rawsite -o surfing
```

## Publishing on GitHub Pages

Every push to `main` starts the GitHub Actions workflow in `.github/workflows/deploy-pages.yml`. The workflow obtains the pinned Panehe revision, verifies its checksum, installs Beautiful Soup 4, builds `rawsite/`, and deploys the result to GitHub Pages. The repository therefore stores only the source site; generated files do not need to be committed.

For the first deployment, set **Settings → Pages → Source** to **GitHub Actions** in the repository.

## Repository layout

```text
rawsite/
  index.html  index_ru.html  index_ja.html      home page
  about.html  about_ru.html  about_ja.html      project and authors
  spots/                                      area overview and profiles
  gear/                                       boards and wetsuit guide
  waves/                                      waves and swell articles
  safety/                                     sea-safety overview
  data/  tags/                               comparison and tag index
  _include/                                  shared templates and data
  css/  js/  csv/  img/                      static assets and source data
.github/workflows/deploy-pages.yml           GitHub Pages build and deployment
tools/                                       one-off artwork helpers
```

## Sources and scope

Spot profiles are compiled from published surf guides and local mapping. They are intended as an orientation tool, not a forecast or a guarantee of conditions. The illustrated overview map is based on Natural Earth data (public domain); interactive area maps use OpenStreetMap tiles under their applicable terms.

## Bluesky comments

Mansionsita's English, Russian and Japanese pages share one discussion. To enable
comments for another spot, add a `bluesky` entry to its `SPOT_DETAILS` record in
`rawsite/_include/sitedata.py`:

```python
"bluesky": {"post": "https://bsky.app/profile/YOUR_HANDLE/post/POST_ID"},
```

The shared spot template handles the rest. `hours` is optional (default: 72);
48 means the last two days, and 0 means all time. All language versions use
the same post; interface language comes from the page, comments are not translated.
Accounts whose branches should be hidden across every spot are listed once in
`BLUESKY_BLOCKED_DIDS` in `rawsite/_include/sitedata.py`.

For an ordinary static HTML page, one script tag at the desired position is enough:

```html
<script type="module" src="../../../js/bluesky-comments.js"
  data-bluesky-post="https://bsky.app/profile/YOUR_HANDLE/post/POST_ID"
  data-bluesky-hours="72"></script>
```

Use the appropriate relative path to `js/`. Omit `data-bluesky-hours` for 72 hours.
`data-bluesky-exclude` accepts space-separated DIDs when the component is embedded
without the shared spot template. No CSS link or separate form markup is needed:
the single bundle contains styles, the component,
and the official OAuth client. It is loaded only on pages with comments (and the
shared OAuth callback page). No CDN JavaScript or backend is needed.

Visitors can draft a reply, sign in through Bluesky, and explicitly submit it
from the page. OAuth requests only permission to create `app.bsky.feed.post`
records. Tokens and cryptographic keys are managed by the official SDK; the site
does not collect account passwords. Draft text is stored in tab session storage,
kept through sign-in and failures, and removed after confirmed publication.
Replies may take a little time to appear in the public API; a successful submission
provides a link to the new reply. Reloading the page reloads the discussion. The form always replies to the original configured post; individual comments have no reply buttons. The component
never publishes automatically on sign-in or return from authorization.

### Shared OAuth setup

Two static files are required once per website:

- `rawsite/bluesky-client-metadata.json` declares the production site URL,
  callback URL, and permission scope. It must be publicly accessible as JSON.
- `rawsite/bluesky-callback.html` completes sign-in and returns to the originating
  language page. It loads the same JavaScript bundle.

These are configured for `https://pyotr777.github.io/surfing/`. If the site moves,
update the metadata URLs and rebuild the bundle. Callback return paths are limited
to the same origin under the site path derived from the script URL. Production OAuth sign-in requires publishing the metadata and callback first.
Local sign-in uses the AT Protocol loopback exception: no public metadata or
tunnel is required. Open the website over HTTP at `127.0.0.1` (not `file://` or
`localhost`). Run a local server from the project directory:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8765/surfing/spots/asahi/mansionsita/index.html`.
The local port and path prefix are detected from the script URL; serving the
contents of `surfing/` directly at the server root also works. The local OAuth
callback returns to the same local page. Local authorization is labelled as a
development client by Bluesky. Automated tests mock authentication and posting
and do not publish real replies.

### Maintaining the JavaScript

All Bluesky development files are kept together under the hidden
`rawsite/.bluesky/` directory. Panehe skips hidden directories, so sources,
tests and installed Node.js dependencies are never copied to the published site.
Editable sources are in `rawsite/.bluesky/src/`.
`rawsite/js/bluesky-comments.js` is a committed, self-contained generated bundle.
Normal Panehe builds just copy it and need no Node.js or network access.
To change it, use Node.js 22 or newer:

```bash
npm --prefix rawsite/.bluesky ci
npm --prefix rawsite/.bluesky run build:comments
npm --prefix rawsite/.bluesky run test:comments
```

The OAuth dependency currently has a transitive Zod advisory
[GHSA-mrhx-c7xc-m3w5](https://github.com/advisories/GHSA-mrhx-c7xc-m3w5).
The SDK fetch boundary therefore rejects responses over 256 KiB and JSON
collections over 256 entries / documents over 5,000 nodes before SDK validation.
Keep the official client and lockfile updated as upstream fixes become available.

### Display limits

Comments load at page opening or after a successful submission; the rolling time window is evaluated
at that moment. Replies are shown newest first, including recent replies under
older parents. Hidden and excluded branches are omitted. Personal account block
lists are not fetched. Filtering affects display on this website, not Bluesky
posting permissions. Threadgate/block restrictions are enforced when Bluesky
accepts or rejects a submitted reply.

Only text is rendered here; the original thread links to attachments. The API
returns a bounded tree (requested depth: 100), so large discussions can be
incomplete. Date filtering does not reduce the API response. Build-time requests
to Bluesky are never required.
