# -*- coding: utf-8 -*-
"""Shared data, vocabulary and helpers for the Surf Japan demo site.

This module lives inside _include/, which parser.py never copies to the
built site -- so build-time code and data can sit next to the templates
without leaking into the output.

It is named sitedata.py, not site.py, because `site` is a standard
library module and importing our own `site` would shadow it.

Templates load it with the three-line idiom at the top of every
_include/*.html file:

    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import sitedata as S
"""

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # rawsite/

LANGS = ("en", "ru")

# --------------------------------------------------------------------------
# Site identity
# --------------------------------------------------------------------------

SITE = {
    "en": {
        "name": "Surf Japan",
        "tagline": "Surf spots, board types, physics of the waves",
    },
    "ru": {
        "name": "Сёрф Япония",
        "tagline": "Cпоты для серфинга, типы досок, физика волн",
    },
}

# --------------------------------------------------------------------------
# Interface strings. Everything the templates print lives here, so a page
# never has to know which language it is written in -- it is derived from
# the file name (see lang_of() below).
# --------------------------------------------------------------------------

UI = {
    "en": {
        "nav_home": "Home",
        "nav_spots": "Spots",
        "nav_gear": "Gear",
        "nav_waves": "Waves",
        "nav_data": "Compare spots",
        "nav_tags": "Tags",
        "nav_how": "How this site is built",
        "switch": "Русский",
        "switch_title": "This page in Russian",
        "read_more": "Read more",
        "toc_heading": "What is on this site",
        "toc_count": "pages",
        "board_length": "Length",
        "board_width": "Width",
        "board_thickness": "Thickness",
        "board_volume": "Volume",
        "board_fins": "Fins",
        "board_tail": "Tail",
        "board_waves": "Wave size",
        "board_scale_heading": "All five to scale",
        "board_scale_caption":
            "Outlines are drawn during the build from the length, "
            "width and shape ratios in csv/boards.csv. The bar is "
            "six feet, for reference.",
        "map_heading": "Where the waves are",
        "map_caption": "Illustrated map of the Kanto–Tokai coast, drawn for Surf Japan.",
        "map_legend": "Difficulty",
        "map_pending": "Blue pins are new locations; their guides are in preparation.",
        "table_spot": "Spot",
        "table_region": "Region",
        "table_break": "Break",
        "table_level": "Level",
        "table_season": "Peak season",
        "table_swell": "Swell window",
        "table_wind": "Best wind",
        "table_size": "Typical size",
        "table_aug": "Water, Aug",
        "table_feb": "Water, Feb",
        "table_sort_hint": "Click a column heading to sort.",
        "facts_heading": "At a glance",
        "tags_heading": "All tags",
        "tags_intro": "Tags are shared between both languages, so an English "
                      "and a Russian page carrying the same tag land in the same list.",
        "tagged": "Tagged",
        "back_home": "Back to all spots",
        "no_pages": "No pages yet.",
        "built_with": "Built with <a href='https://github.com/pyotr777/panehe/'>Panehe</a>",
        "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "wetsuit_region": "Region",
        "wetsuit_note": "Thickness in millimetres. 2 mm means a spring suit is enough; "
                        "5 mm implies a hood, boots and gloves.",
    },
    "ru": {
        "nav_home": "Главная",
        "nav_spots": "Споты",
        "nav_gear": "Снаряжение",
        "nav_waves": "Волны",
        "nav_data": "Сравнение спотов",
        "nav_tags": "Теги",
        "nav_how": "Как собран этот сайт",
        "switch": "English",
        "switch_title": "Эта же страница по-английски",
        "read_more": "Читать",
        "toc_heading": "Что есть на сайте",
        "toc_count": "страниц",
        "board_length": "Длина",
        "board_width": "Ширина",
        "board_thickness": "Толщина",
        "board_volume": "Объём",
        "board_fins": "Плавники",
        "board_tail": "Хвост",
        "board_waves": "Размер волны",
        "board_scale_heading": "Все пять в одном масштабе",
        "board_scale_caption": "Контуры рисуются на сборке из длины, ширины и "
                               "пропорций формы в csv/boards.csv. Полоса внизу — "
                               "шесть футов для сравнения.",
        "map_heading": "Где ловить волну",
        "map_caption": "Иллюстрированная карта побережья Канто–Токай, созданная для «Сёрф Япония».",
        "map_legend": "Уровень",
        "map_pending": "Синие пины — новые точки; страницы для них готовятся.",
        "table_spot": "Спот",
        "table_region": "Регион",
        "table_break": "Тип волны",
        "table_level": "Уровень",
        "table_season": "Сезон",
        "table_swell": "Свелл-окно",
        "table_wind": "Лучший ветер",
        "table_size": "Обычный размер",
        "table_aug": "Вода, авг.",
        "table_feb": "Вода, фев.",
        "table_sort_hint": "Нажмите на заголовок столбца, чтобы отсортировать.",
        "facts_heading": "Коротко",
        "tags_heading": "Все теги",
        "tags_intro": "Теги общие для обоих языков, поэтому английская и русская "
                      "страницы с одним тегом попадают в один список.",
        "tagged": "Тег",
        "back_home": "Ко всем спотам",
        "no_pages": "Страниц пока нет.",
        "built_with": "Сайт сделан при помощи <a href='https://github.com/pyotr777/panehe/'>Panehe</a>",
        "months": ["янв.", "фев.", "март", "апр.", "май", "июнь", "июль", "авг.", "сен.", "окт.", "нояб.", "дек."],
        "wetsuit_region": "Регион",
        "wetsuit_note": "Толщина в миллиметрах. 2 мм — хватит короткого гидрокостюма; "
                        "5 мм — подразумевает шлем, боты и перчатки.",
    },
}

# --------------------------------------------------------------------------
# Vocabulary shared by the CSV files and the pages. The CSV stores stable
# English keys; the translations live here.
# --------------------------------------------------------------------------

REGIONS = {
    "hokkaido": {
        "en": "Hokkaido",
        "ru": "Хоккайдо"
    },
    "niigata": {
        "en": "Niigata",
        "ru": "Ниигата"
    },
    "chiba": {
        "en": "Chiba",
        "ru": "Тиба"
    },
    "shonan": {
        "en": "Shonan",
        "ru": "Сёнан"
    },
    "izu-islands": {
        "en": "Izu Islands",
        "ru": "Острова Идзу"
    },
    "miyazaki": {
        "en": "Miyazaki",
        "ru": "Миядзаки"
    },
}

BREAKS = {
    "beach": {
        "en": "beach break",
        "ru": "бич-брейк"
    },
    "rivermouth": {
        "en": "rivermouth",
        "ru": "устье реки"
    },
    "reef": {
        "en": "reef",
        "ru": "риф"
    },
}

LEVELS = {
    "beginner": {
        "en": "beginner",
        "ru": "новичок",
        "color": "#4bb3a0"
    },
    "intermediate": {
        "en": "intermediate",
        "ru": "средний",
        "color": "#e0a23a"
    },
    "advanced": {
        "en": "advanced",
        "ru": "продвинутый",
        "color": "#d9563f"
    },
}

SEASONS = {
    "winter": {
        "en": "winter",
        "ru": "зима"
    },
    "spring": {
        "en": "spring",
        "ru": "весна"
    },
    "summer-autumn": {
        "en": "summer–autumn",
        "ru": "лето — осень"
    },
    "year-round": {
        "en": "year-round",
        "ru": "круглый год"
    },
}

# --------------------------------------------------------------------------
# The three content sections. Order matters: it drives the table of contents,
# the navigation and the order of the feeds on the front page.
# --------------------------------------------------------------------------

SECTIONS = ["spots", "gear", "waves"]

SECTION_META = {
    "spots": {
        "en": {
            "title": "Spots",
            "blurb": "Six breaks, north to south, with the "
                     "conditions that make each one work."
        },
        "ru": {
            "title": "Споты",
            "blurb": "Шесть спотов с севера на юг и условия, "
                     "при которых каждый работает."
        },
    },
    "gear": {
        "en": {
            "title": "Gear",
            "blurb": "Five board shapes drawn to scale, and how "
                     "much rubber the water temperature demands."
        },
        "ru": {
            "title": "Снаряжение",
            "blurb": "Пять форм досок в одном масштабе и "
                     "сколько резины требует температура воды."
        },
    },
    "waves": {
        "en": {
            "title": "Waves",
            "blurb": "Where a wave comes from, and what the "
                     "coast does to it on the way in."
        },
        "ru": {
            "title": "Волны",
            "blurb": "Откуда берётся волна и что делает с ней "
                     "берег по дороге."
        },
    },
}

# Board names and how each deck is painted. The measurements that decide the
# shape live in csv/boards.csv; the colours live here, because they are
# decoration rather than data.
#
#   deck    "bands"  cross-wise stripes, the classic log
#           "wood"   timber grain
#           "panel"  a diagonal two-colour panel
#           "rails"  lengthwise stripes down the deck
#           "solid"  one colour with a contrasting stringer
BOARDS_META = {
    "fish": {
        "en": "Fish",
        "ru": "Фиш",
        "deck": "wood",
        "base": "#d8b184",
        "grain": "#b98a58",
        "rail": "#6ec05c",
        "stringer": "#8a5a33",
    },
    "shortboard": {
        "en": "Shortboard",
        "ru": "Шортборд",
        "deck": "panel",
        "base": "#f3f6f7",
        "accent": "#d9563f",
        "accent2": "#e8b13a",
        "rail": "#e8b13a",
        "stringer": "#c9d2d6",
    },
    "funboard": {
        "en": "Funboard",
        "ru": "Фанборд",
        "deck": "solid",
        "base": "#eef4f5",
        "accent": "#0e9aa7",
        "rail": "#0e9aa7",
        "stringer": "#0e9aa7",
    },
    "gun": {
        "en": "Gun",
        "ru": "Ган",
        "deck": "rails",
        "base": "#f3f6f7",
        "accent": "#7cc242",
        "accent2": "#0e9aa7",
        "rail": "#0e9aa7",
        "stringer": "#c9d2d6",
    },
    "longboard": {
        "en": "Longboard",
        "ru": "Лонгборд",
        "deck": "bands",
        "base": "#f3f6f7",
        "bands": ["#7cc242", "#2fb3a8", "#d9563f", "#f0a92e", "#2fb3a8", "#7cc242"],
        "rail": "#7cc242",
        "stringer": "#e6eef0",
    },
}

# The drawings use one representative board per shape; these are the broader
# everyday ranges shown on the overview and card grid.  A rider's weight,
# skill and local waves still decide the right board within the range.
BOARD_RANGES = {
    "fish": {"length_in": (62, 76), "volume_l": (28, 45)},
    "shortboard": {"length_in": (68, 78), "volume_l": (24, 36)},
    "funboard": {"length_in": (78, 96), "volume_l": (40, 65)},
    "gun": {"length_in": (84, 120), "volume_l": (40, 70)},
    "longboard": {"length_in": (96, 120), "volume_l": (60, 100)},
}

TAILS = {
    "squash": {
        "en": "squash",
        "ru": "сквош"
    },
    "swallow": {
        "en": "swallow",
        "ru": "ласточкин"
    },
    "round": {
        "en": "round",
        "ru": "круглый"
    },
    "square": {
        "en": "square",
        "ru": "квадратный"
    },
    "pin": {
        "en": "pin",
        "ru": "пин"
    },
}

# Spot names, and where the map label should sit relative to its pin.
# dx/dy are in map pixels; "anchor" is the SVG text-anchor.
SPOTS_META = {
    "shioya": {
        "en": "Shioya",
        "ru": "Сиоя",
        "dx": 14,
        "dy": -6,
        "anchor": "start"
    },
    "ikarashi": {
        "en": "Ikarashi",
        "ru": "Икараси",
        "dx": -14,
        "dy": -6,
        "anchor": "end"
    },
    "tsurigasaki": {
        "en": "Tsurigasaki",
        "ru": "Цуригасаки",
        "dx": 20,
        "dy": -10,
        "anchor": "start"
    },
    "iioka-mansionshita": {
        "en": "Iioka Mansionshita",
        "ru": "Ииока: Мансёнсита",
        "dx": -18,
        "dy": -12,
        "anchor": "end"
    },
    "kanpomae": {
        "en": "Kanpomae",
        "ru": "Канпомаэ",
        "dx": -18,
        "dy": 20,
        "anchor": "end"
    },
    "sakuta": {
        "en": "Sakuta",
        "ru": "Сакута",
        "dx": 18,
        "dy": -12,
        "anchor": "start"
    },
    "ichinomiya": {
        "en": "Ichinomiya",
        "ru": "Итиномия",
        "dx": -18,
        "dy": -18,
        "anchor": "end"
    },
    "onjuku": {
        "en": "Onjuku",
        "ru": "Ондзюку",
        "dx": 18,
        "dy": 18,
        "anchor": "start"
    },
    "kugenuma": {
        "en": "Kugenuma",
        "ru": "Кугэнума",
        "dx": -20,
        "dy": 6,
        "anchor": "end"
    },
    "habushiura": {
        "en": "Habushiura",
        "ru": "Хабусиура",
        "dx": 14,
        "dy": 14,
        "anchor": "start"
    },
    "kisakihama": {
        "en": "Kisakihama",
        "ru": "Кисакихама",
        "dx": 14,
        "dy": 4,
        "anchor": "start"
    },
}

# Area names and label placement on the illustrated overview map.  These are
# navigation areas, not administrative prefectures: a dense coast can then be
# explored on a separate map without overlapping every individual surf spot.
AREAS_META = {
    "asahi": {
        "en": "Asahi", "ru": "Асахи"
    },
    "sosa": {
        "en": "Sosa", "ru": "Соса"
    },
    "sakuta": {
        "en": "Sakuta", "ru": "Сакута"
    },
    "ichinomiya": {
        "en": "Ichinomiya", "ru": "Итиномия"
    },
    "katsuura": {
        "en": "Katsuura", "ru": "Кацуура"
    },
    "fujisawa": {
        "en": "Fujisawa", "ru": "Фудзисава"
    },
}

# The overview groups the coast into navigation areas.  A card describes the
# shared feel of a stretch of shore; individual spot pages carry the more
# precise, local conditions.
AREAS = {
    "asahi": {
        "image": "ikarashi",
        "region": {"en": "Chiba · Chiba North", "ru": "Тиба · Тиба Кита"},
        "summary": {
            "en": "Iioka’s south-west-facing bend: sandy beach breaks shaped by tetrapods, south swell and more room than crowds.",
            "ru": "Юго-западный изгиб побережья у Ииоки: песчаные брейки у тетраподов, южный свелл и больше пространства, чем людей.",
        },
    },
    "sosa": {
        "image": "shioya",
        "region": {"en": "Chiba · Chiba North", "ru": "Тиба · Тиба Кита"},
        "summary": {
            "en": "An open east-Chiba coast that catches east-to-south swell; a broad, sandy alternative when the famous peaks are busy.",
            "ru": "Открытое побережье восточной Тибы, принимающее свелл с востока до юга; широкий песчаный выбор, когда известные пики заняты.",
        },
    },
    "sakuta": {
        "image": "tsurigasaki",
        "region": {"en": "Chiba · Chiba North", "ru": "Тиба · Тиба Кита"},
        "summary": {
            "en": "A wide, shallow sandy beach with several peaks, soft waves and enough coastline to spread out along the Kujukuri arc.",
            "ru": "Широкий пологий песчаный пляж с несколькими пиками, мягкой волной и простором всей дуги Кудзюкури.",
        },
    },
    "ichinomiya": {
        "image": "habushiura",
        "region": {"en": "Chiba · Chiba North", "ru": "Тиба · Тиба Кита"},
        "summary": {
            "en": "Chiba’s surf centre: mobile sandbanks, east swell, a deep surf culture and consistently busy line-ups from Ichinomiya to Shidashita.",
            "ru": "Сёрф-центр Тибы: подвижные песчаные банки, восточный свелл, глубокая сёрф-культура и неизменно оживлённые лайн-апы от Итиномии до Сидаситы.",
        },
    },
    "katsuura": {
        "image": "kisakihama",
        "region": {"en": "Chiba · Chiba South", "ru": "Тиба · Тиба Минами"},
        "summary": {
            "en": "South-facing Onjuku brings a gentler rhythm: open white sand, south-east to south swell and room beyond the harbour peak.",
            "ru": "Обращённый на юг Ондзюку — более спокойный ритм: белый песок, юго-восточный и южный свелл, свободное место за пределами пика у гавани.",
        },
    },
    "fujisawa": {
        "image": "kugenuma",
        "region": {"en": "Kanagawa · Shonan", "ru": "Канагава · Сёнан"},
        "summary": {
            "en": "Kugenuma is Shonan’s social beach break: forgiving sandbanks, south swell, surf schools and one of Japan’s liveliest line-ups.",
            "ru": "Кугэнума — социальный бич-брейк Сёнана: дружелюбные песчаные банки, южный свелл, школы и один из самых оживлённых лайн-апов Японии.",
        },
    },
}

AREA_FACTS = {
    "asahi": {
        "en": [("Coast", "Chiba North · Iioka"), ("Breaks", "Sandy beach breaks and tetrapod peaks"), ("Swell", "E–SSW, best with south in the mix"), ("Clean wind", "NNE"), ("Crowds", "Usually room to spread out")],
        "ru": [("Побережье", "Тиба Кита · Ииока"), ("Брейки", "Песчаные пляжи и пики у тетраподов"), ("Свелл", "В–ЮЮЗ, лучше с южной составляющей"), ("Чистый ветер", "ССВ"), ("Люди", "Обычно есть пространство")],
        "spots": {"en": ["Mansionsita"], "ru": ["Мэнсионсита"]},
    },
    "sosa": {
        "en": [("Coast", "Chiba North · Sosa"), ("Breaks", "Open sandy beach breaks"), ("Swell", "E–S"), ("Clean wind", "N–NW"), ("Crowds", "Visitors, but a less concentrated line-up")],
        "ru": [("Побережье", "Тиба Кита · Соса"), ("Брейки", "Открытые песчаные бич-брейки"), ("Свелл", "В–Ю"), ("Чистый ветер", "С–СЗ"), ("Люди", "Приезжих много, но лайн-ап менее концентрирован")],
        "spots": {"en": ["Kanpomae"], "ru": ["Канпомаэ"]},
    },
    "sakuta": {
        "en": [("Coast", "Chiba North · Kujukuri"), ("Breaks", "Wide, shallow sandy beach"), ("Swell", "NE–SSE"), ("Clean wind", "NW"), ("Crowds", "Popular, with several peaks to choose from")],
        "ru": [("Побережье", "Тиба Кита · Кудзюкури"), ("Брейки", "Широкий пологий песчаный пляж"), ("Свелл", "СВ–ЮЮВ"), ("Чистый ветер", "СЗ"), ("Люди", "Популярно, но можно выбрать пик")],
        "spots": {"en": ["Sakuta"], "ru": ["Сакута"]},
    },
    "ichinomiya": {
        "en": [("Coast", "Chiba North · Ichinomiya"), ("Breaks", "Mobile sandbanks beside jetties"), ("Swell", "NE–SE, especially east"), ("Clean wind", "W"), ("Crowds", "One of Chiba’s busiest surf hubs")],
        "ru": [("Побережье", "Тиба Кита · Итиномия"), ("Брейки", "Подвижные песчаные банки у молов"), ("Свелл", "СВ–ЮВ, особенно восточный"), ("Чистый ветер", "З"), ("Люди", "Один из самых оживлённых сёрф-центров Тибы")],
        "spots": {"en": ["Ichinomiya", "Tsurigasaki / Shidashita"], "ru": ["Итиномия", "Цуригасаки / Сидасита"]},
    },
    "katsuura": {
        "en": [("Coast", "Chiba South · Onjuku"), ("Breaks", "Open sandy beach, harbour and river-mouth peaks"), ("Swell", "ESE–SSW, especially SE–S"), ("Clean wind", "N"), ("Crowds", "Calmer beyond the harbour peak")],
        "ru": [("Побережье", "Тиба Минами · Ондзюку"), ("Брейки", "Открытый песчаный пляж, пики у гавани и устья"), ("Свелл", "ВЮВ–ЮЮЗ, особенно ЮВ–Ю"), ("Чистый ветер", "С"), ("Люди", "За пределами пика у гавани спокойнее")],
        "spots": {"en": ["Onjuku"], "ru": ["Ондзюку"]},
    },
    "fujisawa": {
        "en": [("Coast", "Kanagawa · Shonan"), ("Breaks", "Shallow sandy beach and river-mouth bars"), ("Swell", "E–SW, especially south"), ("Clean wind", "N–NE"), ("Crowds", "One of Japan’s busiest line-ups")],
        "ru": [("Побережье", "Канагава · Сёнан"), ("Брейки", "Пологий песчаный пляж и банки у устья"), ("Свелл", "В–ЮЗ, особенно южный"), ("Чистый ветер", "С–СВ"), ("Люди", "Один из самых оживлённых лайн-апов Японии")],
        "spots": {"en": ["Kugenuma"], "ru": ["Кугэнума"]},
    },
}

# Real-map geometry is separate from the illustrated overview map.  These
# coordinates are used only on the corresponding area page, where a visitor
# can pan and zoom around the actual coastline.
AREA_MAPS = {
    "asahi": {
        "center": (35.6991, 140.7173),
        "zoom": 15,
        "spots": [
            {
                "id": "mansionsita",
                "coordinates": (35.69908, 140.71730),
                "en": "Mansionsita (マンション下)",
                "ru": "Мэнсионсита (マンション下)",
            },
        ],
    },
}

# Tag labels are deliberately identical in both languages -- see UI["tags_intro"].
TAGS = [
    "beginner",
    "intermediate",
    "advanced",
    "beach-break",
    "rivermouth",
    "barrel",
    "cold-water",
    "warm-water",
    "typhoon-swell",
    "winter-swell",
    "tokyo-daytrip",
    "island",
    "olympic",
    "board",
    "small-waves",
    "big-waves",
    "high-volume",
    "low-volume",
    "wave-theory",
    "wind",
    "bathymetry",
]

# --------------------------------------------------------------------------
# Map geometry. The illustrated map deliberately favours a readable horizontal
# composition over a north-up projection. Pin coordinates are therefore set
# against the hand-drawn coastline rather than calculated from latitude/long.
# --------------------------------------------------------------------------

MAP = {
    "width": 1821,
    "height": 864,
    "area_labels": {
        "asahi": (1510, 250),
        "sosa": (1430, 330),
        "sakuta": (1340, 390),
        "ichinomiya": (1280, 465),
        "katsuura": (1260, 550),
        "fujisawa": (770, 400),
    },
}

# Compass bearings, used to turn a swell window such as "NE-S" into an arc.
DIRECTIONS = {
    "N": 0,
    "NNE": 22.5,
    "NE": 45,
    "ENE": 67.5,
    "E": 90,
    "ESE": 112.5,
    "SE": 135,
    "SSE": 157.5,
    "S": 180,
    "SSW": 202.5,
    "SW": 225,
    "WSW": 247.5,
    "W": 270,
    "WNW": 292.5,
    "NW": 315,
    "NNW": 337.5,
}


def bearing(name):
    """Degrees clockwise from north for a compass point such as 'WNW'."""
    return DIRECTIONS[name.strip().upper()]


def swell_arc(window):
    """('NE-S') -> (45.0, 180.0). The arc always runs clockwise."""
    start, end = window.split("-")
    return bearing(start), bearing(end)


# --------------------------------------------------------------------------
# Data loading
# --------------------------------------------------------------------------


def load_spots():
    """Read csv/spots.csv and return a list of dicts, north to south."""
    path = os.path.join(ROOT, "csv", "spots.csv")
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["lat"] = float(r["lat"])
        r["lon"] = float(r["lon"])
        r["water_aug_c"] = int(r["water_aug_c"])
        r["water_feb_c"] = int(r["water_feb_c"])
    rows.sort(key=lambda r: -r["lat"])
    return rows


def spot_by_id(spot_id):
    for r in load_spots():
        if r["id"] == spot_id:
            return r
    raise KeyError(f"No spot {spot_id!r} in csv/spots.csv")


def load_boards():
    """Read csv/boards.csv and return a list of dicts in display order."""
    path = os.path.join(ROOT, "csv", "boards.csv")
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for key in (
            "length_in", "width_in", "nose_tip_in", "nose_6_in", "nose_12_in", "tail_12_in", "tail_end_in", "wide_point", "thickness_in", "volume_l",
            "wave_min_ft", "wave_max_ft", "order"
        ):
            r[key] = float(r[key])
    rows.sort(key=lambda r: r["order"])
    return rows


def board_by_id(board_id):
    for r in load_boards():
        if r["id"] == board_id:
            return r
    raise KeyError(f"No board {board_id!r} in csv/boards.csv")


def _hermite(stations, x):
    """Value of a Catmull-Rom spline through (x, y) stations at position x.

    Tangents are the centred finite differences at each station, which is the
    Catmull-Rom rule written for unevenly spaced points. The stations are the
    only thing stored; everything else about the outline follows from here.
    """
    xs = [p[0] for p in stations]
    ys = [p[1] for p in stations]
    if x <= xs[0]:
        return ys[0]
    if x >= xs[-1]:
        return ys[-1]

    n = len(xs)
    i = max(j for j in range(n - 1) if xs[j] <= x)
    h = xs[i + 1] - xs[i]
    t = (x - xs[i]) / h

    def tangent(k):
        lo = max(0, k - 1)
        hi = min(n - 1, k + 1)
        return (ys[hi] - ys[lo]) / (xs[hi] - xs[lo])

    m0, m1 = tangent(i) * h, tangent(i + 1) * h
    t2, t3 = t * t, t * t * t
    return ((2 * t3 - 3 * t2 + 1) * ys[i] + (t3 - 2 * t2 + t) * m0 + (-2 * t3 + 3 * t2) * ys[i + 1] + (t3 - t2) * m1)


def board_stations(row):
    """The width measurements that define an outline, in inches.

    Shapers quote a board by its width at a few stations along the length --
    the tip, six and twelve inches back, the wide point, twelve inches from
    the tail, and the tail block. Those numbers are the whole shape: it is
    the six-inch station that gives a log its broad round nose and a gun its
    needle, so the pair is worth storing separately.

    Returned as (distance from nose, half width) pairs.
    """
    L = row["length_in"]
    return [
        (0.0, row["nose_tip_in"] / 2),
        (6.0, row["nose_6_in"] / 2),
        (12.0, row["nose_12_in"] / 2),
        (L * row["wide_point"], row["width_in"] / 2),
        (L - 12.0, row["tail_12_in"] / 2),
        (L, row["tail_end_in"] / 2),
    ]


BOARD_SAMPLES = 96


def board_profile(row, cx, top, ppi, n=BOARD_SAMPLES, decor=False):
    """Sample the outline: a list of (y, half_width) in SVG units, nose first.

    Every drawing of a board -- the silhouette, the deck stripes, the wood
    grain -- is built from this one list, which is why the stripes follow the
    curve of the rail instead of being clipped against it.

    With decor=True the samples stop short of a swallow tail's notch, so deck
    decoration does not paint across the gap between the two points.
    """
    stations = board_stations(row)
    L = row["length_in"]
    end = L
    if decor and row["tail"] == "swallow":
        end = L - row["tail_end_in"] * 1.25
    out = []
    for i in range(n + 1):
        along = end * i / n
        out.append((top + along * ppi, _hermite(stations, along) * ppi))
    return out


def board_outline(row, cx, top, ppi):
    """SVG path for one board outline, nose at the top.

    Nothing about the shape is drawn by hand. The five stations come from
    csv/boards.csv, a spline is fitted through them, the result is mirrored,
    and the tail is closed according to the tail column. This is why the log
    ends up with a blunt round nose and the gun with a needle -- the numbers
    say so.
    """
    prof = board_profile(row, cx, top, ppi)
    shape = row["tail"]
    nose_y, nose_hw = prof[0]
    tail_y, tail_hw = prof[-1]

    d = [f"M {cx + nose_hw:.2f},{nose_y:.2f}"]
    for y, hw in prof[1:]:
        d.append(f"L {cx + hw:.2f},{y:.2f}")

    if shape == "swallow":
        d.append(f"L {cx + tail_hw * 0.62:.2f},{tail_y - tail_hw * 0.7:.2f}")
        d.append(f"L {cx:.2f},{tail_y - tail_hw * 2.4:.2f}")
        d.append(f"L {cx - tail_hw * 0.62:.2f},{tail_y - tail_hw * 0.7:.2f}")
        d.append(f"L {cx - tail_hw:.2f},{tail_y:.2f}")
    elif shape == "square":
        d.append(f"L {cx - tail_hw:.2f},{tail_y:.2f}")
    elif shape == "pin":
        d.append(f"Q {cx:.2f},{tail_y + tail_hw * 2.2:.2f} {cx - tail_hw:.2f},{tail_y:.2f}")
    else:  # squash, round
        d.append(f"Q {cx:.2f},{tail_y + tail_hw * 0.6:.2f} {cx - tail_hw:.2f},{tail_y:.2f}")

    for y, hw in reversed(prof[:-1]):
        d.append(f"L {cx - hw:.2f},{y:.2f}")

    # Round off the nose: the log's tip is two and a half inches across, the
    # gun's is under half an inch, and the cap follows whatever the CSV says.
    d.append(f"A {nose_hw:.2f},{nose_hw * 1.6:.2f} 0 0 1 {cx + nose_hw:.2f},{nose_y:.2f}")
    d.append("Z")
    return " ".join(d)


def board_band(prof, cx, y_from, y_to):
    """A cross-wise stripe on the deck, bounded by the rails.

    Returned as an SVG path, so it can be filled directly -- no clipping
    path, no rectangle poking out past the rail.
    """
    inside = [(y, hw) for y, hw in prof if y_from <= y <= y_to]
    if len(inside) < 2:
        return ""
    d = [f"M {cx + inside[0][1]:.2f},{inside[0][0]:.2f}"]
    for y, hw in inside[1:]:
        d.append(f"L {cx + hw:.2f},{y:.2f}")
    for y, hw in reversed(inside):
        d.append(f"L {cx - hw:.2f},{y:.2f}")
    d.append("Z")
    return " ".join(d)


def board_stripe(prof, cx, x_from, x_to):
    """A lengthwise stripe, trimmed where it would run past the rail."""
    right, left = [], []
    for y, hw in prof:
        lo = max(x_from, cx - hw)
        hi = min(x_to, cx + hw)
        if hi - lo > 0.2:
            right.append((hi, y))
            left.append((lo, y))
    if len(right) < 2:
        return ""
    d = [f"M {right[0][0]:.2f},{right[0][1]:.2f}"]
    for x, y in right[1:]:
        d.append(f"L {x:.2f},{y:.2f}")
    for x, y in reversed(left):
        d.append(f"L {x:.2f},{y:.2f}")
    d.append("Z")
    return " ".join(d)


def feet_inches(total_inches):
    """72.0 -> "6'0\"" """
    feet, inches = divmod(int(round(total_inches)), 12)
    return f"{feet}&prime;{inches}&Prime;"


def feet_inches_range(start_inches, end_inches):
    """Format a board-length range in the same notation as one length."""
    return f"{feet_inches(start_inches)}–{feet_inches(end_inches)}"


def load_wetsuit():
    """Return {region: {month: thickness_mm}} from csv/wetsuit.csv."""
    path = os.path.join(ROOT, "csv", "wetsuit.csv")
    table = {}
    with open(path, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            table.setdefault(r["region"], {})[int(r["month"])] = int(r["thickness_mm"])
    return table


# --------------------------------------------------------------------------
# Language and path helpers
#
# The whole bilingual scheme rests on one naming convention:
#     page.html   <->  page_ru.html
# Nothing else in the site records which language a page is in.
# --------------------------------------------------------------------------

RU_SUFFIX = "_ru.html"


def lang_of(page_file):
    """'ru' for foo_ru.html, otherwise 'en'."""
    return "ru" if os.path.basename(page_file).endswith(RU_SUFFIX) else "en"


def other_lang_name(page_file):
    """File name of the same page in the other language."""
    name = os.path.basename(page_file)
    if name.endswith(RU_SUFFIX):
        return name[:-len(RU_SUFFIX)] + ".html"
    return name[:-len(".html")] + RU_SUFFIX


def base_url(page_file):
    """Relative path from the page being rendered up to the site root.

    Returns '' for a page in the root and '../../' for spots/kugenuma/index.html,
    so templates can link without ever hard-coding an absolute path.
    """
    rel = os.path.relpath(ROOT, os.path.dirname(os.path.abspath(page_file)))
    return "" if rel == "." else rel.replace(os.sep, "/") + "/"


def localize(name, lang):
    """Apply the naming convention to a root-relative link."""
    if lang == "ru":
        return name[:-len(".html")] + RU_SUFFIX
    return name


def nav_items(page_file):
    """Navigation entries for the language the current page is written in.

    Navigation never switches language: only the flag link does that.
    """
    lang = lang_of(page_file)
    b = base_url(page_file)
    u = UI[lang]
    items = [(b + localize("index.html", lang), u["nav_home"])]
    for name in SECTIONS:
        items.append((b + localize(f"{name}/index.html", lang), SECTION_META[name][lang]["title"]))
    items += [
        (b + localize("data/index.html", lang), u["nav_data"]),
        (b + localize("tags/index.html", lang), u["nav_tags"]),
        (b + localize("how-it-works.html", lang), u["nav_how"]),
    ]
    return items


def section_url(name, page_file):
    """Link from the current page to a section's index page."""
    lang = lang_of(page_file)
    return base_url(page_file) + localize(f"{name}/index.html", lang)
