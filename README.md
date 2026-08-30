# Surf Japan 

A small bilingual site in three sections — surf breaks, board shapes, and the physics of the waves. The site is built using [Panehe](https://github.com/pyotr777/panehe/) SSG.  Everything on it (the map pins, the board outlines, the refraction diagram, the card lists, the comparison table, the tag index) is computed while the site is being built, by Python written inline in the HTML.

```
python3 panehe.py rawsite -o surfing
```

The build needs Python 3 and BeautifulSoup 4, and nothing else.

## What each feature demonstrates

| Feature on the site | Engine capability |
| --- | --- |
| Header, nav and footer on every page | `include()` with parameters and defaults |
| Nav inside the header | includes nested inside includes |
| Pages at `spots/<id>/`, `gear/<id>/`, `waves/<id>/` | `page_file` and `__file__` → relative paths with no hard-coded root |
| Card lists on each section page | build-time `glob`, pages parsed with BeautifulSoup |
| Three separate feeds | filtering on `<meta name="section">` and `<meta name="language">` |
| Table of contents | the same file scan, counted rather than listed |
| Facts panel, map, table, roses | one `csv/spots.csv`, read at build time |
| Board outlines, painted | `csv/boards.csv` → a spline through six measured stations |
| Refraction diagram | Snell's law integrated across the frame at build time |
| Shoaling block | dispersion relation solved at every depth, height shoaled through the group velocity |
| Spot card illustrations | wave steepness generated from the difficulty column |
| Wetsuit heat grid | second CSV, cell colours computed from the values |
| Tag pages with anchors | cross-page scan against one canonical tag list |
| Language link | file-name convention, resolved without configuration |
| `_include/sitedata.py` | shared code and data that never reaches the output |
| Prev/next links | ordering derived from a data column, not a hand-kept list |

## Layout

```
rawsite/
  index.html  index_ru.html           front page: contents and the map
  how-it-works.html  ..._ru.html      what the engine does
  data/      tags/                    comparison table, tag index
  spots/index.html  ..._ru.html       section page, then six breaks below it
  spots/<id>/index.html  ..._ru.html
  gear/index.html   ..._ru.html       section page with the boards to scale
  gear/<id>/index.html   ..._ru.html  five boards + the wetsuit guide
  waves/index.html  ..._ru.html       section page with the shoaling block
  waves/<id>/index.html  ..._ru.html  two articles
  _include/                           templates + sitedata.py (never copied out)
  css/  js/  csv/  img/               static files, copied verbatim
tools/                                one-off scripts, not part of the build
```

Sections are declared once, in `sitedata.SECTIONS`. Adding a fourth means
creating the folder, adding an entry there, and nothing else: the navigation,
the table of contents, the tag index and the feeds all read that list.

## The bilingual convention

A Russian page is the same file name with `_ru` before the extension:
`index.html` ↔ `index_ru.html`, `spots/kugenuma/index.html` ↔
`spots/kugenuma/index_ru.html`. That single rule does three jobs:

- `sitedata.lang_of()` reads it to decide which language a template prints in,
  so no page ever passes a `lang` parameter;
- the language link finds the current page's twin in the same directory;
- navigation is built with the current language applied, so only the language
  link ever switches language.

Tags are the exception: they are keys rather than prose, and are identical in
both languages so that an English and a Russian page with the same tag land in
the same list. `_include/pagetags.html` refuses to render a tag that is not in
`sitedata.TAGS`, which keeps typos out of the index.

## Drawings that are not pictures

Four graphics on the site have no image file behind them:

- **Board outlines** (`sitedata.board_outline`) are a spline fitted through the
  six width measurements a shaper would quote — the tip, six and twelve inches
  back, the wide point, twelve inches from the tail, and the tail block — then
  mirrored. That is why the log ends up with a broad round nose and parallel
  rails while the gun tapers to a needle: the numbers say so. The deck stripes
  in `_include/board-art.html` are generated from the same sampled profile
  rather than clipped against it, so a band narrows towards the nose because
  the board does. The card thumbnails and the scale drawing call the same code.
- **Compass roses** (`_include/swell-rose.html`) are an SVG arc between the two
  bearings in the swell-window column, plus an arrow at the wind bearing.
- **The refraction diagram** (`_include/wave-diagram.html`) traces each wave
  crest across the frame, turning it by Snell's law at the local depth, so the
  crests really are perpendicular to the ray and really do flatten towards the
  beach.
- **The shoaling block** (`_include/shoaling.html`) solves the dispersion
  relation `ω² = gk·tanh(kd)` at every step towards the beach, shoals the wave
  height through the group velocity and accumulates the phase. The waves crowd
  together and grow on their own, and the break lands where the depth-limited
  criterion puts it.

## Regenerating the artwork

`tools/` holds two scripts that were run once and whose output is committed.
The site builds without them.

- `make_art.py` — draws the card illustrations and the favicon as SVG.

If you move the map window, change `MAP` in `_include/sitedata.py` and the
matching constants in `make_basemap.py`, then re-run the script: the pins
follow automatically, because they are projected from the same box.

## Sources and licences

The basemap is Natural Earth, which is public domain. Spot descriptions and
board dimensions were compiled from published surf guides; the numbers are
indicative and this is a demo, not a forecast.
