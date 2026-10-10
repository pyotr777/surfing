"""Build-time direction data and SVG for detailed spot pages.

English compass codes describe an inclusive clockwise range of 16 sectors.
For example, E-SSW includes every sector from E through SSW; N selects one.
"""

import html
import math

COMPASS = (
    "N",
    "NNE",
    "NE",
    "ENE",
    "E",
    "ESE",
    "SE",
    "SSE",
    "S",
    "SSW",
    "SW",
    "WSW",
    "W",
    "WNW",
    "NW",
    "NNW",
)

SPOT_DIRECTIONS = {
    "mansionsita": {
        "swell": "SE-SW",
        "wind": "N-ENE"
    },
    "shingosita": {
        "swell": "ESE-S",
        "wind": "NNW-ENE"
    },
    "shoppumae": {
        "swell": "NE-SSW",
        "wind": "NW-NE"
    },
    "kanpomae": {
        "swell": "E-S",
        "wind": "NW-N"
    },
    "sakuta": {
        "swell": "NE-S",
        "wind": "WSW-NW"
    },
    "motosuka": {
        "swell": "NE-E",
        "wind": "W-NW"
    },
}


def selected_sectors(description):
    """Return all sectors from the first code clockwise through the last."""
    codes = description.split("-")
    if len(codes) not in (1, 2) or any(code not in COMPASS for code in codes):
        raise ValueError(f"Invalid compass description: {description!r}")
    if len(codes) == 1:
        return {codes[0]}
    start = COMPASS.index(codes[0])
    end = COMPASS.index(codes[1])
    return {COMPASS[index % len(COMPASS)] for index in range(start, start + (end - start) % len(COMPASS) + 1)}


def diagram(description, label):
    """Return a self-contained, accessible 16-sector compass SVG."""
    selected = selected_sectors(description)
    center, radius = 100, 90
    paths = []
    for index, code in enumerate(COMPASS):
        start = math.radians(index * 22.5 - 11.25)
        end = math.radians(index * 22.5 + 11.25)

        def point(angle, distance):
            return (center + distance * math.sin(angle), center - distance * math.cos(angle))

        x1, y1 = point(start, radius)
        x2, y2 = point(end, radius)
        tx, ty = point(math.radians(index * 22.5), radius * .72)
        state = " is-selected" if code in selected else ""
        paths.append(
            f'<path class="direction-sector{state}" '
            f'd="M {center},{center} L {x1:.2f},{y1:.2f} '
            f'A {radius},{radius} 0 0 1 {x2:.2f},{y2:.2f} Z"/>'
            f'<text class="direction-label{state}" x="{tx:.2f}" y="{ty:.2f}" '
            f'text-anchor="middle" dominant-baseline="central">{code}</text>'
        )
    title = f"{label}: {description}"
    return (
        f'<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-label="{html.escape(title, quote=True)}">' + "".join(paths) + '</svg>'
    )
