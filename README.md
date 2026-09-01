# Surf Japan

[Surf Japan](https://pyotr777.github.io/surfing/) is an independent, non-commercial guide to surfing Japan’s Pacific coast. It begins with Chiba, Kanagawa and Shizuoka: their coastal areas, surf spots, boards and the way the coastline shapes swell.

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

The current overview areas are Asahi, Sosa, Sakuta, Ichinomiya, Katsuura and Fujisawa. They are navigation areas, not a fixed list of all the spots covered by the project.

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
  data/  tags/                               comparison and tag index
  _include/                                  shared templates and data
  css/  js/  csv/  img/                      static assets and source data
.github/workflows/deploy-pages.yml           GitHub Pages build and deployment
tools/                                       one-off artwork helpers
```

## Sources and scope

Spot profiles are compiled from published surf guides and local mapping. They are intended as an orientation tool, not a forecast or a guarantee of conditions. The illustrated overview map is based on Natural Earth data (public domain); interactive area maps use OpenStreetMap tiles under their applicable terms.
