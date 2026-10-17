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

LANGS = ("en", "ru", "ja")
LANGUAGE_NAMES = {"en": "English", "ru": "Русский", "ja": "日本語"}

MAP_LAYER_NAMES = {
    "en": {
        "standard": "Street map",
        "topographic": "Terrain",
        "humanitarian": "Detailed map"
    },
    "ru": {
        "standard": "Улицы",
        "topographic": "Рельеф",
        "humanitarian": "Подробная карта"
    },
    "ja": {
        "standard": "地図",
        "topographic": "地形図",
        "humanitarian": "詳細地図"
    },
}

# Amenity keys are English and shared by every language.
AMENITY_META = {
    "parking": {
        "icon": "parking-free-engraved-v1.png",
        "sign": "P",
        "label": {
            "en": "Free parking",
            "ru": "Бесплатная парковка",
            "ja": "無料駐車場"
        }
    },
    "paid_parking": {
        "icon": "parking-paid-engraved-v1.png",
        "sign": "P",
        "label": {
            "en": "Paid parking",
            "ru": "Платная парковка",
            "ja": "有料駐車場"
        }
    },
    "shower": {
        "icon": "shower-engraved-v1.png",
        "sign": "shower",
        "label": {
            "en": "Shower",
            "ru": "Душ",
            "ja": "シャワー"
        }
    },
    "restroom": {
        "icon": "toilet-engraved-v1.png",
        "sign": "WC",
        "label": {
            "en": "Restroom",
            "ru": "Туалет",
            "ja": "トイレ"
        }
    },
}


def iter_map_amenity_coordinates(amenity_coordinates):
    """Yield one (kind, coordinates) pair for each map amenity."""
    items = amenity_coordinates.items() if hasattr(amenity_coordinates, "items") else amenity_coordinates
    for kind, values in items:
        if (isinstance(values, (list, tuple)) and len(values) == 2 and all(isinstance(value, (int, float)) for value in values)):
            yield kind, values
        else:
            for coordinates in values:
                yield kind, coordinates


def map_amenities(amenity_coordinates, lang):
    """Build map markers and merge a co-located shower and restroom."""
    grouped = {}
    for kind, coordinates in iter_map_amenity_coordinates(amenity_coordinates):
        grouped.setdefault(tuple(coordinates), []).append(kind)

    markers = []
    for coordinates, kinds in grouped.items():
        remaining = list(kinds)
        if "shower" in remaining and "restroom" in remaining:
            remaining.remove("shower")
            remaining.remove("restroom")
            markers.append(
                {
                    "coordinates": coordinates,
                    "kind": "shower-restroom",
                    "sign": "shower-restroom",
                    "label": f'{AMENITY_META["shower"]["label"][lang]} · {AMENITY_META["restroom"]["label"][lang]}',
                }
            )
        for kind in remaining:
            meta = AMENITY_META[kind]
            markers.append({"coordinates": coordinates, "kind": kind, "sign": meta["sign"], "label": meta["label"][lang]})
    return markers


# --------------------------------------------------------------------------
# Site identity
# --------------------------------------------------------------------------

SITE = {
    "en": {
        "name": "Surf Japan",
        "tagline": "Surf areas, boards, wave theory and sea safety",
    },
    "ru": {
        "name": "Surf Japan",
        "tagline": "Районы для сёрфинга, доски, физика волн и безопасность на море",
    },
    "ja": {
        "name": "Surf Japan",
        "tagline": "サーフエリア、ボード、波のしくみ、海の安全",
    },
}

# --------------------------------------------------------------------------
# Interface strings. Everything the templates print lives here, so a page
# never has to know which language it is written in -- it is derived from
# the file name (see lang_of() below).
# --------------------------------------------------------------------------

UI = {
    "en":
        {
            "nav_home": "Home",
            "gear_sections": "Gear sections",
            "gear_boards": "Boards",
            "gear_fins": "Fins",
            "gear_leash": "Leash",
            "gear_wetsuit": "Wetsuit",
            "nav_tags": "Tags",
            "nav_glossary": "Glossary",
            "nav_how": "About",
            "nav_menu": "Menu",
            "languages": "Languages",
            "skip": "Skip to content",
            "nav_label": "Main navigation",
            "read_more": "Read more",
            "toc_heading": "What is on this site",
            "board_length": "Length",
            "board_width": "Width",
            "board_thickness": "Thickness",
            "board_volume": "Volume",
            "board_fins": "Fins",
            "board_tail": "Tail",
            "board_waves": "Wave size",
            "board_scale_heading": "All four to scale",
            "board_scale_caption":
                "Outlines are drawn during the build from the length, "
                "width and shape ratios in csv/boards.csv. The bar is "
                "six feet, for reference.",
            "map_heading": "Where the waves are",
            "map_caption": "Illustrated map of surf areas along Chiba’s Pacific coast.",
            "table_area": "Area",
            "table_spot": "Spot",
            "table_region": "Region",
            "table_break": "Break",
            "table_level": "Level",
            "table_season": "Peak season",
            "table_swell": "Swell window",
            "table_wind": "Best wind",
            "table_size": "Wave height",
            "table_aug": "Water, Aug",
            "table_feb": "Water, Feb",
            "table_sort_hint": "Click a column heading to sort.",
            "facts_heading": "At a glance",
            "tags_heading": "All tags",
            "tagged": "Tagged",
            "back_home": "Back to all spots",
            "no_pages": "No pages yet.",
            "built_with": "Built with <a href='https://github.com/pyotr777/panehe/'>Panehe</a>",
            "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            "wetsuit_region": "Region",
            "wetsuit_note": "Thickness in millimetres. 2 mm means a spring suit is enough; "
                            "5 mm implies a hood, boots and gloves.",
        },
    "ru":
        {
            "nav_home": "Главная",
            "gear_sections": "Разделы снаряжения",
            "gear_boards": "Доски",
            "gear_fins": "Плавники",
            "gear_leash": "Лиш",
            "gear_wetsuit": "Гидрокостюм",
            "nav_tags": "Теги",
            "nav_glossary": "Глоссарий",
            "nav_how": "О сайте",
            "nav_menu": "Меню",
            "languages": "Языки",
            "skip": "К содержанию",
            "nav_label": "Основная навигация",
            "read_more": "Читать",
            "toc_heading": "Что есть на сайте",
            "board_length": "Длина",
            "board_width": "Ширина",
            "board_thickness": "Толщина",
            "board_volume": "Объём",
            "board_fins": "Плавники",
            "board_tail": "Хвост",
            "board_waves": "Размер волны",
            "board_scale_heading": "Все четыре в одном масштабе",
            "board_scale_caption":
                "Контуры рисуются на сборке из длины, ширины и "
                "пропорций формы в csv/boards.csv. Полоса внизу — "
                "шесть футов для сравнения.",
            "map_heading": "Где ловить волну",
            "map_caption": "Иллюстрированная карта районов для сёрфинга на тихоокеанском побережье Тибы.",
            "table_area": "Район",
            "table_spot": "Спот",
            "table_region": "Регион",
            "table_break": "Тип волны",
            "table_level": "Уровень",
            "table_season": "Сезон",
            "table_swell": "Свелл-окно",
            "table_wind": "Лучший ветер",
            "table_size": "Высота волны",
            "table_aug": "Вода, авг.",
            "table_feb": "Вода, фев.",
            "table_sort_hint": "Нажмите на заголовок столбца, чтобы отсортировать.",
            "facts_heading": "Коротко",
            "tags_heading": "Все теги",
            "tagged": "Тег",
            "back_home": "Ко всем спотам",
            "no_pages": "Страниц пока нет.",
            "built_with": "Сайт сделан при помощи <a href='https://github.com/pyotr777/panehe/'>Panehe</a>",
            "months": ["янв.", "фев.", "март", "апр.", "май", "июнь", "июль", "авг.", "сен.", "окт.", "нояб.", "дек."],
            "wetsuit_region": "Регион",
            "wetsuit_note": "Толщина в миллиметрах. 2 мм — хватит короткого гидрокостюма; "
                            "5 мм — подразумевает шлем, боты и перчатки.",
        },
    "ja":
        {
            "nav_home": "ホーム",
            "gear_sections": "ギアの項目",
            "gear_boards": "ボード",
            "gear_fins": "フィン",
            "gear_leash": "リーシュ",
            "gear_wetsuit": "ウェットスーツ",
            "nav_tags": "タグ",
            "nav_glossary": "用語集",
            "nav_how": "このサイトについて",
            "nav_menu": "メニュー",
            "languages": "言語",
            "skip": "本文へ移動",
            "nav_label": "メインナビゲーション",
            "read_more": "詳しく見る",
            "toc_heading": "このサイトの内容",
            "board_length": "長さ",
            "board_width": "幅",
            "board_thickness": "厚さ",
            "board_volume": "容量",
            "board_fins": "フィン",
            "board_tail": "テール",
            "board_waves": "対応する波のサイズ",
            "board_scale_heading": "4種類を同じ縮尺で",
            "board_scale_caption": "アウトラインは、csv/boards.csv の長さ、幅、形状比からビルド時に描かれます。下のバーは6フィートです。",
            "map_heading": "波を探す場所",
            "map_caption": "千葉の太平洋沿いのサーフエリアを示す図解地図",
            "table_area": "エリア",
            "table_spot": "スポット",
            "table_region": "エリア",
            "table_break": "ブレイク",
            "table_level": "レベル",
            "table_season": "ベストシーズン",
            "table_swell": "対応するうねり",
            "table_wind": "最適風向",
            "table_size": "波の高さ",
            "table_aug": "水温・8月",
            "table_feb": "水温・2月",
            "table_sort_hint": "列の見出しをクリックすると並べ替えられます。",
            "facts_heading": "概要",
            "tags_heading": "すべてのタグ",
            "tagged": "タグ",
            "back_home": "すべてのスポットへ戻る",
            "no_pages": "ページはまだありません。",
            "built_with": "<a href='https://github.com/pyotr777/panehe/'>Panehe</a> で作成",
            "months": ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
            "wetsuit_region": "エリア",
            "wetsuit_note": "厚さはミリメートル。2 mm はスプリングスーツで十分な目安、5 mm はフード、ブーツ、グローブも必要になる水温です。",
        },
}

# --------------------------------------------------------------------------
# Vocabulary shared by the CSV files and the pages. The CSV stores stable
# English keys; the translations live here.
# --------------------------------------------------------------------------

REGIONS = {
    "chiba-north": {
        "en": "North Chiba",
        "ru": "Северная Тиба",
        "ja": "千葉北"
    },
    "chiba-south": {
        "en": "South Chiba",
        "ru": "Южная Тиба",
        "ja": "千葉南"
    },
    "chiba": {
        "en": "Chiba",
        "ru": "Тиба",
        "ja": "千葉"
    },
    "shonan": {
        "en": "Shonan",
        "ru": "Сёнан",
        "ja": "湘南"
    },
}

BREAKS = {
    "beach": {
        "en": "beach break",
        "ru": "бич-брейк",
        "ja": "ビーチブレイク"
    },
}

LEVELS = {
    "beginner": {
        "en": "beginner",
        "ru": "новичок",
        "ja": "初級",
        "color": "#4bb3a0"
    },
    "intermediate": {
        "en": "intermediate",
        "ru": "средний",
        "ja": "中級",
        "color": "#e0a23a"
    },
    "advanced": {
        "en": "advanced",
        "ru": "продвинутый",
        "ja": "上級",
        "color": "#d9563f"
    },
}

SEASONS = {
    "summer-autumn": {
        "en": "summer–autumn",
        "ru": "лето — осень",
        "ja": "夏〜秋"
    },
    "year-round": {
        "en": "year-round",
        "ru": "круглый год",
        "ja": "通年"
    },
}

# --------------------------------------------------------------------------
# The content sections. Order matters: it drives the table of contents,
# the navigation and the order of the feeds on the front page.
# --------------------------------------------------------------------------

SECTIONS = ["spots", "gear", "waves", "safety"]

SECTION_META = {
    "spots":
        {
            "en": {
                "title": "Spots",
                "blurb": "Regions and surf spots, with the conditions that "
                         "make each one work."
            },
            "ru": {
                "title": "Споты",
                "blurb": "Области и споты, а также условия, при которых "
                         "каждый из них работает."
            },
            "ja": {
                "title": "スポット",
                "blurb": "エリアとスポット、それぞれが良くなる条件を紹介します。"
            },
        },
    "gear":
        {
            "en": {
                "title": "Gear",
                "blurb": "Four board shapes drawn to scale, and how "
                         "much rubber the water temperature demands."
            },
            "ru": {
                "title": "Снаряжение",
                "blurb": "Четыре формы досок в одном масштабе и "
                         "сколько резины требует температура воды."
            },
            "ja": {
                "title": "ギア",
                "blurb": "縮尺を揃えて描いた4種類のボードと、水温に合うウェットスーツ。"
            },
        },
    "waves":
        {
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
            "ja": {
                "title": "波",
                "blurb": "波が生まれる場所と、岸に近づく途中で海岸が波にすること。"
            },
        },
    "safety":
        {
            "en": {
                "title": "Safety",
                "blurb": "Simple checks and decisions for a safer session in the sea."
            },
            "ru": {
                "title": "Безопасность",
                "blurb": "Простые проверки и решения для более безопасного выхода в море."
            },
            "ja": {
                "title": "海の安全",
                "blurb": "海で安全に過ごすための、基本的な確認と判断。"
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
        "ja": "フィッシュ",
        "deck": "wood",
        "base": "#d8b184",
        "grain": "#b98a58",
        "rail": "#6ec05c",
        "stringer": "#8a5a33",
    },
    "shortboard":
        {
            "en": "Shortboard",
            "ru": "Шортборд",
            "ja": "ショートボード",
            "deck": "panel",
            "base": "#f3f6f7",
            "accent": "#d9563f",
            "accent2": "#e8b13a",
            "rail": "#e8b13a",
            "stringer": "#c9d2d6",
        },
    "funboard":
        {
            "en": "Funboard",
            "ru": "Фанборд",
            "ja": "ファンボード",
            "deck": "solid",
            "base": "#eef4f5",
            "accent": "#0e9aa7",
            "rail": "#0e9aa7",
            "stringer": "#0e9aa7",
        },
    "gun":
        {
            "en": "Gun",
            "ru": "Ган",
            "ja": "ガン",
            "deck": "rails",
            "base": "#f3f6f7",
            "accent": "#7cc242",
            "accent2": "#0e9aa7",
            "rail": "#0e9aa7",
            "stringer": "#c9d2d6",
        },
    "longboard":
        {
            "en": "Longboard",
            "ru": "Лонгборд",
            "ja": "ロングボード",
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
    "fish": {
        "length_in": (62, 76),
        "volume_l": (28, 45)
    },
    "shortboard": {
        "length_in": (68, 78),
        "volume_l": (24, 36)
    },
    "funboard": {
        "length_in": (78, 96),
        "volume_l": (40, 65)
    },
    "gun": {
        "length_in": (84, 120),
        "volume_l": (40, 70)
    },
    "longboard": {
        "length_in": (96, 120),
        "volume_l": (60, 100)
    },
}

# Longboards are a family of outlines rather than one fixed board. These
# shapes are grouped by outline, rail line and rocker; fin setup is a separate
# choice and therefore does not define a type here.
LONGBOARD_SHAPES = [
    {
        "id": "classic",
        "en": {
            "title": "Classic / Traditional",
            "summary": "A full outline with balanced nose, tail and rocker for stable trim and smooth turns.",
        },
        "ru":
            {
                "title": "Классический / традиционный",
                "summary": "Полный outline, сбалансированные нос, корма и рокер — для устойчивого трима и плавных поворотов.",
            },
        "ja": {
            "title": "クラシック / トラディショナル",
            "summary": "幅のあるアウトラインと、バランスの取れたノーズ、テール、ロッカー。安定したトリムと滑らかなターン向きです。",
        },
    },
    {
        "id": "all-around",
        "en":
            {
                "title": "All-around",
                "summary": "A balanced outline with a full nose and rounded tail; moderate rocker combines early entry and trim with confident turns.",
            },
        "ru":
            {
                "title": "Универсальный (all-around)",
                "summary": "Сбалансированный outline, полный нос и округлая корма; умеренный рокер сочетает ранний вход в волну, трим и уверенные повороты.",
            },
        "ja": {
            "title": "オールラウンド",
            "summary": "バランスの取れたアウトラインに、幅を残したノーズと丸みのあるテール。ほどよいロッカーが早いテイクオフ、トリム、安定したターンを両立します。",
        },
    },
    {
        "id": "noserider",
        "en": {
            "title": "Noserider",
            "summary": "A wide, full nose and a wide tail; a flatter entry and tail kick help it settle in the pocket.",
        },
        "ru": {
            "title": "Нозрайдер",
            "summary": "Широкий полный нос и широкая корма; плоский вход и подъём кормы помогают доске держаться в кармане волны.",
        },
        "ja": {
            "title": "ノーズライダー",
            "summary": "広いノーズと幅のあるテール。フラットなエントリーとテールキックが、ポケットでの安定につながります。",
        },
    },
    {
        "id": "performance",
        "en": {
            "title": "Performance",
            "summary": "A pulled-in nose and tail with more rocker for tighter turns and quicker changes of direction.",
        },
        "ru": {
            "title": "Перформанс",
            "summary": "Зауженные нос и корма, более выраженный рокер — для более резких поворотов и быстрой смены направления.",
        },
        "ja": {
            "title": "パフォーマンス",
            "summary": "絞ったノーズとテール、強めのロッカー。よりタイトなターンと素早い切り返しに向きます。",
        },
    },
    {
        "id": "glider",
        "en": {
            "title": "Glider",
            "summary": "A long, narrow plan shape with low rocker, built to carry speed and cover distance on a small wave.",
        },
        "ru": {
            "title": "Глайдер",
            "summary": "Длинная узкая форма с мягким рокером; несёт скорость и проходит длинную дистанцию на небольшой волне.",
        },
        "ja": {
            "title": "グライダー",
            "summary": "長く細いアウトラインと穏やかなロッカー。小波でスピードを保ち、長い距離を走るための形です。",
        },
    },
]

# Longer explanations shown on each outline's own page. Keep the same fields
# for every shape and language so the localized pages cover the same ground.
LONGBOARD_SHAPE_DETAILS = {
    "classic": {
        "en": {
            "lead": "A traditional longboard for relaxed trim, flowing lines and classic footwork.",
            "design": "The full outline carries width through the nose and tail, while a moderate rocker keeps the board predictable. It is commonly paired with a single fin, though the fin setup is a separate choice from the outline.",
            "ideal": "Choose it for small to medium, clean waves and a steady style built around holding a line, walking the board and drawing smooth turns.",
            "tradeoff": "The broad outline and longer rail need room to turn. In steep, fast surf or crowded water, the board can feel slow to redirect and takes care to manage.",
        },
        "ru": {
            "lead": "Традиционный лонгборд для спокойного трима, плавных линий и классической работы ног.",
            "design": "Полный outline сохраняет ширину в носу и корме, а умеренный рокер делает поведение доски предсказуемым. Часто такую доску ставят на сингл-фин, хотя выбор плавников не определяет форму.",
            "ideal": "Подходит для небольших и средних чистых волн и спокойного стиля: держать линию, перемещаться по доске и выполнять плавные повороты.",
            "tradeoff": "Широкий outline и длинный кант требуют места для поворота. На крутых быстрых волнах и в толпе доска медленнее меняет направление и требует внимательного контроля.",
        },
        "ja": {
            "lead": "落ち着いたトリム、流れるライン、伝統的なフットワークを楽しむロングボードです。",
            "design": "幅をノーズからテールまで保ったアウトラインと、穏やかなロッカーで予測しやすい乗り味になります。シングルフィンがよく使われますが、フィンの選択はアウトラインとは別の要素です。",
            "ideal": "小さめから中程度のきれいな波で、ラインを保ち、ボード上を歩き、滑らかにターンするスタイルに向いています。",
            "tradeoff": "幅のあるアウトラインと長いレールラインには、ターンするためのスペースが必要です。急で速い波や混雑した場所では方向転換が遅く、慎重な扱いが求められます。",
        },
    },
    "all-around": {
        "en": {
            "lead": "A versatile longboard that balances early entry, easy trim and controlled turns.",
            "design": "A full nose and rounded tail provide useful glide without making the ends overly specialised. Moderate rocker helps the board paddle into waves early and still redirect through a turn.",
            "ideal": "Choose it as a first longboard or as one board for changing small-wave conditions, especially when you want to mix trimming with regular turns.",
            "tradeoff": "Its balanced design does not maximise one specialty. A dedicated noserider is steadier on the nose, while a performance model turns more sharply.",
        },
        "ru": {
            "lead": "Универсальный лонгборд, который сочетает ранний вход в волну, лёгкий трим и контролируемые повороты.",
            "design": "Полный нос и округлая корма дают хорошее скольжение, не делая концы доски слишком специализированными. Умеренный рокер помогает рано заходить на волну и при этом менять направление в повороте.",
            "ideal": "Подходит как первый лонгборд или одна доска для переменчивых небольших волн, особенно если хочется чередовать трим и обычные повороты.",
            "tradeoff": "Сбалансированная форма не доводит до максимума одну конкретную функцию. Специализированный нозрайдер устойчивее на носу, а перформанс-модель резче поворачивает.",
        },
        "ja": {
            "lead": "早いテイクオフ、扱いやすいトリム、コントロールしやすいターンをバランスよく備えたロングボードです。",
            "design": "幅を残したノーズと丸みのあるテールが、極端に用途を絞らずグライドを生みます。ほどよいロッカーにより早く波に乗れ、ターンでも方向を変えやすくなります。",
            "ideal": "初めてのロングボードや、変化する小波に一本で対応したいときに向いています。トリムと通常のターンを組み合わせたい人にも適しています。",
            "tradeoff": "バランス重視のため、特定の動きを最大限に伸ばす形ではありません。ノーズライダーはノーズでより安定し、パフォーマンス型はより鋭くターンできます。",
        },
    },
    "noserider": {
        "en": {
            "lead": "A longboard shaped to stay settled while you move forward and ride near the nose.",
            "design": "The wide nose gives the front foot a broad platform. A full tail and added tail kick help hold the board in the wave's pocket when weight shifts forward; the exact feel depends on rocker, rails and fin choice too.",
            "ideal": "Choose it for slower, peeling waves and a traditional approach focused on cross-stepping, nose time and maintaining position in the pocket.",
            "tradeoff": "The design rewards a clean line and good positioning, but it can feel sticky when pushed through tight turns. It is less suited to steep, fast sections that call for quick redirection.",
        },
        "ru": {
            "lead": "Лонгборд, рассчитанный на устойчивость, когда вы перемещаетесь вперёд и катаетесь у самого носа.",
            "design": "Широкий нос даёт передней ноге просторную опору. Широкая корма и её подъём помогают удерживать доску в кармане волны, когда вес смещается вперёд; на ощущения также влияют рокер, рейлы и плавники.",
            "ideal": "Подходит для медленных раскатывающихся волн и традиционного стиля с кросс-степом, временем на носу и удержанием позиции в кармане.",
            "tradeoff": "Такая форма поощряет чистую линию и точный выбор позиции, но может казаться неповоротливой в резких манёврах. Для крутых быстрых участков, где нужно быстро менять направление, она подходит хуже.",
        },
        "ja": {
            "lead": "前方へ歩き、ノーズ付近で波に乗るときの安定性を重視したロングボードです。",
            "design": "幅広いノーズが前足を支える広い足場になります。幅のあるテールとテールキックは、重心を前に移したときにボードを波のポケットに保つ助けになります。ロッカー、レール、フィンの選択も乗り味に影響します。",
            "ideal": "ゆっくり崩れる波で、クロスステップやノーズライディング、ポケットでの位置取りを楽しむ伝統的なスタイルに向いています。",
            "tradeoff": "きれいなラインと適切なポジションが活きる一方、タイトなターンでは重く感じることがあります。素早い切り返しが必要な急で速いセクションにはあまり向きません。",
        },
    },
    "performance": {
        "en": {
            "lead": "A high-performance longboard brings shortboard-style rail work and turning range to a board that still paddles, trims and can be ridden from the nose.",
            "overview": (
                "High-performance longboards are not simply smaller or narrower logs. They are purpose-built longboards for drawing committed lines: driving a bottom turn, linking a cutback to the pocket, redirecting off the lip and then moving forward to trim or noseride. The category spans dedicated competition shapes and more forgiving everyday designs, but its common aim is speed, hold and quick response from a full-length board.",
                "The current range makes that spectrum clear. The Firewire Taylor Jensen Pro is a competition-focused rounded-pin design; the TJ Pro V keeps similar DNA with a lower rocker and wider nose for average surf. NSP’s Pro-9, CJ Nelson Designs’ GX1000 and Ibis, and Kai Sallas’ Lava Flow each use their own balance of rocker, rails, bottom contours and fins to turn a longboard more actively. They are useful reference points, not a single specification every performance longboard must copy.",
            ),
            "models": (
                "Firewire Taylor Jensen Pro — rounded pin tail, performance rails, nose concave into double concave and slight vee; made for speed, power and driving turns.",
                "Firewire Taylor Jensen Pro V — an everyday counterpart with lower rocker, more nose area, a squash tail, spiral vee and 2+1 or quad options.",
                "NSP Pro-9 — low-volume performance longboard with a soft-roll-to-vee-to-double-concave bottom and a 4+1 fin cluster.",
                "CJ Nelson Designs GX1000 — a speed-oriented high-performance longboard with performance rails, a concave nose and refined HP rocker.",
                "CJ Nelson Designs Ibis — combines a concave nose, flatter middle, tail kick, defined rails and a 2+1 setup for logging and hard tail turns.",
                "Kai Sallas Lava Flow — pulled-in nose and pin tail, continuous rocker, hard vee bottom and a tail edge for faster, more powerful surf.",
            ),
            "design": "Across these models, the outline is usually more refined at the tail and the rails are thinner, lower and more defined than on a traditional log, so the board holds when loaded on rail. Rocker is tuned for the intended wave: a continuous curve or added nose and tail lift keeps a dedicated HP shape clear on steep drops, while an everyday version may flatten the middle for earlier entry and speed. Bottom contours commonly combine a light nose concave with double concave, vee or spiral vee under the rear foot; they create lift and channel water while helping the board roll rail to rail. Rounded pins, pin tails and squash tails trade hold and release differently, and 2+1, quad or 4+1 fin boxes let the rider tune drive, pivot and looseness.",
            "ideal": "Best for intermediate and advanced surfers who already control a longboard from the tail and can place their feet deliberately. A dedicated HP model comes alive on clean, shoulder-high and larger waves with a defined face, speed and a section to turn against; a flatter, wider everyday version can also work in smaller beach-break surf. Choose it when active carving, top turns, cutbacks and fast down-the-line surfing matter as much as trim and nose time.",
            "tradeoff": "The responsiveness comes from a more exacting balance of volume, rail shape, rocker and fin setup. Compared with a fuller classic or all-around longboard, a focused HP shape usually catches weak waves later, carries less speed through slow water and is less forgiving of a late step or poorly timed turn. It also has more speed and a sharper rail in powerful surf, so it needs clear water, confident control and deliberate equipment choices. Test the size and fin configuration in the waves you actually surf rather than choosing only by a model’s competition pedigree.",
        },
        "ru": {
            "lead": "High-performance лонгборд сочетает работу на канте и диапазон поворотов шортборда с греблей, тримом и возможностью ехать с носа длинной доски.",
            "overview": (
                "High-performance лонгборд — не просто укороченный или зауженный лог. Это длинная доска для активной линии: мощного боттом-тёрна, катбэка в карман, смены направления на липе, а затем трима или нозрайдинга. В этой категории есть как соревновательные шейпы, так и более дружелюбные повседневные модели; их объединяет стремление получить скорость, держак и быстрый отклик от полноразмерного лонгборда.",
                "Современные модели хорошо показывают этот диапазон. Firewire Taylor Jensen Pro — соревновательная доска с round pin; TJ Pro V развивает ту же идею, но получает более плоский рокер и широкий нос для средних условий. NSP Pro-9, CJ Nelson Designs GX1000 и Ibis, а также Kai Sallas Lava Flow по-разному сочетают рокер, рейлы, контуры днища и плавники, чтобы лонгборд активнее поворачивал. Это ориентиры, а не единый рецепт для всех performance-моделей.",
            ),
            "models": (
                "Firewire Taylor Jensen Pro — round pin, performance-рейлы, носовой конкейв, переходящий в двойной конкейв и небольшой vee; сделан для скорости, мощи и поворотов с закладкой на кант.",
                "Firewire Taylor Jensen Pro V — повседневная версия с более плоским рокером, большей площадью носа, сквош-тейлом, spiral vee и вариантами 2+1 или квад.",
                "NSP Pro-9 — малолитражный performance-лонгборд с днищем от мягкого roll к vee и двойному конкейву и кластером плавников 4+1.",
                "CJ Nelson Designs GX1000 — скоростной high-performance лонгборд с performance-рейлами, конкейвом в носу и настроенным HP-рокером.",
                "CJ Nelson Designs Ibis — сочетает носовой конкейв, более плоскую середину, кик тейла, выраженные рейлы и схему 2+1 для логгинга и резких поворотов от тейла.",
                "Kai Sallas Lava Flow — зауженный нос и пин-тейл, непрерывный рокер, жёсткое V-днище и кант в корме для быстрых и мощных волн.",
            ),
            "design": "У этих моделей обычно более собранная корма, а рейлы тоньше, ниже и чётче, чем у традиционного лога: доска лучше держится, когда вы загружаете кант. Рокер настраивают под волну: непрерывная дуга или дополнительный подъём носа и тейла помогают специализированному HP-шейпу не цепляться на крутом дропе, а в повседневной версии середину могут сделать площе для раннего входа и скорости. В днище часто сочетаются лёгкий носовой конкейв и двойной конкейв, vee или spiral vee под задней ногой: они создают подъёмную силу, направляют поток и помогают перекладывать доску с рейла на рейл. Round pin, пин-тейл и сквош-тейл по-разному распределяют держак и отпускание, а боксы 2+1, квад или 4+1 позволяют настроить драйв, поворот и свободу доски.",
            "ideal": "Подходит сёрферам среднего и продвинутого уровня, которые уже уверенно управляют лонгбордом с тейла и осознанно переставляют ноги. Специализированный HP-шейп раскрывается на чистых волнах от плеча и выше, с выраженной стенкой, скоростью и участком для поворота; более плоская и широкая повседневная версия может работать и в небольшом пляжном брейке. Выбирайте его, когда активные дуги, повороты на липе, катбэки и быстрый проезд по стенке так же важны, как трим и время на носу.",
            "tradeoff": "Отзывчивость требует точного баланса объёма, рейлов, рокера и плавников. В сравнении с полным классическим или универсальным лонгбордом сфокусированный HP-шейп обычно позже ловит слабую волну, хуже сохраняет скорость на плоских участках и меньше прощает запоздалый шаг или неточный поворот. На мощной волне у него выше скорость и острее кант, поэтому нужны свободная вода, уверенный контроль и осознанный выбор оборудования. Подбирайте размер и плавники под волны, на которых катаетесь, а не только по соревновательному происхождению модели.",
        },
        "ja": {
            "lead": "ハイパフォーマンス・ロングボードは、パドル、トリム、ノーズライドを保ちながら、ショートボードのようなレールワークとターンの幅を長いボードにもたらします。",
            "overview": (
                "ハイパフォーマンス・ロングボードは、単に短くしたり細くしたログではありません。強いボトムターン、ポケットへのカットバック、リップでの方向転換をつなぎ、その後に前へ歩いてトリムやノーズライドへ移るためのロングボードです。コンペティション向けのシェイプから扱いやすいデイリーモデルまでありますが、共通する目的は、フルレングスのロングボードでスピード、ホールド、素早い反応を得ることです。",
                "現行モデルを見ると、その幅がよく分かります。Firewire Taylor Jensen Proはラウンドピンの競技志向モデルで、TJ Pro Vはロッカーを抑え、ノーズ幅を広げて平均的な波に合わせています。NSP Pro-9、CJ Nelson DesignsのGX1000とIbis、Kai Sallas Lava Flowは、ロッカー、レール、ボトムコンツアー、フィンをそれぞれ異なる比率で組み合わせ、ロングボードをよりアクティブにターンさせます。これらは参考になるモデルであり、すべてのパフォーマンス型が同じ仕様である必要はありません。",
            ),
            "models": (
                "Firewire Taylor Jensen Pro — ラウンドピンテール、パフォーマンスレール、ノーズの浅いコンケーブからダブルコンケーブ、わずかなVeeへ。スピード、パワー、レールを使ったターンのための形です。",
                "Firewire Taylor Jensen Pro V — 控えめなロッカー、広めのノーズ、スカッシュテール、スパイラルVee、2+1またはクアッドの選択肢を持つデイリー向けの派生モデルです。",
                "NSP Pro-9 — ソフトロールからVee、ダブルコンケーブへ続くボトムと4+1フィンクラスターを備えた、低ボリュームのパフォーマンス・ロングボードです。",
                "CJ Nelson Designs GX1000 — パフォーマンスレール、ノーズコンケーブ、洗練されたHPロッカーを備えたスピード重視のハイパフォーマンス・ロングボードです。",
                "CJ Nelson Designs Ibis — ノーズコンケーブ、フラット寄りの中央部、テールキック、はっきりしたレール、2+1セットアップを組み合わせ、ログらしい乗り方と強いテールターンを両立します。",
                "Kai Sallas Lava Flow — 絞ったノーズとピンテール、連続するロッカー、硬めのVボトム、テールのエッジで、速くパワフルな波に対応します。",
            ),
            "design": "これらのモデルは、一般にテール側が洗練され、伝統的なログよりも薄く低く、輪郭のはっきりしたレールを持ちます。レールに荷重したときのホールドを得るためです。ロッカーは波に合わせて調整されます。連続したカーブやノーズとテールのキックを増やした専用HPシェイプは急なドロップで引っかかりにくく、デイリー向けでは中央部をフラットにして早いテイクオフとスピードを狙うこともあります。ボトムは、浅いノーズコンケーブにダブルコンケーブ、Vee、スパイラルVeeを後ろ足の下で組み合わせることが多く、揚力と水流の整理を行い、レール・トゥ・レールの切り替えを助けます。ラウンドピン、ピンテール、スカッシュテールではホールドとリリースの性格が異なり、2+1、クアッド、4+1のボックスはドライブ、ピボット、ルースさの調整を可能にします。",
            "ideal": "テール側からロングボードをコントロールでき、意図して足を置き換えられる中級者から上級者に向いています。専用のHPモデルは、肩からそれ以上のサイズで、はっきりしたフェイス、スピード、ターンを当てるセクションがあるクリーンな波で活きます。ロッカーを抑えた幅広めのデイリーモデルは、小さなビーチブレイクでも使えます。トリムやノーズで過ごす時間と同じくらい、積極的なカービング、リップターン、カットバック、速いダウン・ザ・ラインを重視するときに選ぶ形です。",
            "tradeoff": "反応性は、ボリューム、レール形状、ロッカー、フィンの繊細なバランスから生まれます。幅を残したクラシック型やオールラウンド型と比べると、特化したHPシェイプは力の弱い波ではテイクオフが遅く、フラットな水面で速度を保ちにくく、遅れたステップやタイミングのずれを許容しにくい傾向があります。パワーのある波ではスピードが出てレールも鋭くなるため、空いたライン、確かなコントロール、意図した用具選びが必要です。コンペティションでの実績だけで選ばず、普段乗る波でサイズとフィン設定を試してください。",
        },
    },
    "glider": {
        "en": {
            "lead": "A long, narrow shape designed to build speed and travel a long line across a small wave.",
            "design": "The extended waterline and low rocker reduce drag once the board is moving. A narrow plan shape keeps the outline efficient and encourages a flowing line rather than repeated direction changes.",
            "ideal": "Choose it for soft, clean waves where carrying speed across flat sections matters more than tight turns or walking to the nose.",
            "tradeoff": "The long, narrow outline needs space and a suitable line to work well. It is less nimble in crowded peaks and can be harder to handle in steep shorebreak.",
        },
        "ru": {
            "lead": "Длинная узкая форма, созданная для набора скорости и длинной линии на небольшой волне.",
            "design": "Удлинённая ватерлиния и небольшой рокер снижают сопротивление, когда доска уже разогналась. Узкий outline делает форму эффективной и располагает к плавной линии вместо частых смен направления.",
            "ideal": "Подходит для мягких чистых волн, где важно сохранить скорость на пологих участках, а резкие повороты и выходы на нос не в приоритете.",
            "tradeoff": "Длинному узкому outline нужны пространство и подходящая линия. На загруженном пике он менее манёвренный, а в крутом прибое его сложнее контролировать.",
        },
        "ja": {
            "lead": "小波でスピードを生み、長いラインを走るために設計された、長く細い形です。",
            "design": "長い水線長と低いロッカーが、ボードが動き出した後の抵抗を抑えます。細いアウトラインは効率よく滑り、頻繁に方向を変えるより流れるラインを描きやすくします。",
            "ideal": "フラットなセクションで速度を保つことが大切な、力の弱いきれいな波に向いています。タイトなターンやノーズライディングを優先しないスタイルに適しています。",
            "tradeoff": "長く細いアウトラインを活かすには、スペースと適切なラインが必要です。混雑したピークでは小回りが利きにくく、急なショアブレイクでは扱いが難しくなります。",
        },
    },
}

TAILS = {
    "squash": {
        "en": "squash",
        "ru": "сквош",
        "ja": "スカッシュ"
    },
    "swallow": {
        "en": "swallow",
        "ru": "ласточкин",
        "ja": "スワロー"
    },
    "round": {
        "en": "round",
        "ru": "круглый",
        "ja": "ラウンド"
    },
    "square": {
        "en": "square",
        "ru": "квадратный",
        "ja": "スクエア"
    },
    "pin": {
        "en": "pin",
        "ru": "пин",
        "ja": "ピン"
    },
}

BOARD_FIN_SETUPS = {
    "fish": {
        "en": "twin, quad",
        "ru": "твин, квад",
        "ja": "ツイン、クアッド",
    },
    "shortboard": {
        "en": "thruster, quad",
        "ru": "трастер, квад",
        "ja": "スラスター、クアッド",
    },
    "funboard": {
        "en": "single, 2+1, thruster",
        "ru": "сингл, 2+1, трастер",
        "ja": "シングル、2+1、スラスター",
    },
    "gun": {
        "en": "thruster, quad",
        "ru": "трастер, квад",
        "ja": "スラスター、クアッド",
    },
}

# Area names and label placement on the illustrated overview map.  These are
# navigation areas, not administrative prefectures: a dense coast can then be
# explored on a separate map without overlapping every individual surf spot.
AREAS_META = {
    "asahi": {
        "en": "Asahi",
        "ru": "Асахи",
        "ja": "旭"
    },
    "sosa": {
        "en": "Sosa",
        "ru": "Соса",
        "ja": "匝瑳"
    },
    "sakuta": {
        "en": "Sakuta",
        "ru": "Сакута",
        "ja": "作田"
    },
    "ichinomiya": {
        "en": "Ichinomiya",
        "ru": "Итиномия",
        "ja": "一宮"
    },
    "katsuura": {
        "en": "Katsuura",
        "ru": "Кацуура",
        "ja": "勝浦"
    },
    "fujisawa": {
        "en": "Fujisawa",
        "ru": "Фудзисава",
        "ja": "藤沢"
    },
    "south-boso": {
        "en": "South Boso",
        "ru": "Южный Босо",
        "ja": "南房総"
    },
}

# The comparison and overview share this source of names wherever their
# listings overlap, preventing translated labels from drifting apart.
SPOTS_META = AREAS_META

# The overview groups the coast into navigation areas.  A card describes the
# shared feel of a stretch of shore; individual spot pages carry the more
# precise, local conditions.
AREAS = {
    "asahi":
        {
            "image": "asahi",
            "region": {
                "en": "Chiba · Chiba North",
                "ru": "Тиба · Тиба Кита",
                "ja": "千葉・千葉北"
            },
            "summary":
                {
                    "en": "Iioka’s south-west-facing bend: sandy beach breaks shaped by tetrapods, south swell and more room than crowds.",
                    "ru": "Юго-западный изгиб побережья у Ииоки: песчаные брейки у тетраподов, южный свелл и больше пространства, чем людей.",
                    "ja": "飯岡の南西向きの海岸線。テトラポッド際の砂のブレイク、南寄りのうねり、そして混雑よりも余裕がある場所です。",
                },
        },
    "sosa":
        {
            "image": "sosa",
            "region": {
                "en": "Chiba · Chiba North",
                "ru": "Тиба · Тиба Кита",
                "ja": "千葉・千葉北"
            },
            "summary":
                {
                    "en": "An open east-Chiba coast that catches east-to-south swell; a broad, sandy alternative when the famous peaks are busy.",
                    "ru": "Открытое побережье восточной Тибы, принимающее свелл с востока до юга; широкий песчаный выбор, когда известные пики заняты.",
                    "ja": "東〜南うねりを受ける千葉東部の開けた海岸。有名なピークが混む日に選べる、広い砂のブレイクです。",
                },
        },
    "sakuta":
        {
            "image": "sakuta",
            "region": {
                "en": "Chiba · Chiba North",
                "ru": "Тиба · Тиба Кита",
                "ja": "千葉・千葉北"
            },
            "summary":
                {
                    "en": "A wide, shallow sandy beach with several peaks, soft waves and enough coastline to spread out along the Kujukuri arc.",
                    "ru": "Широкий пологий песчаный пляж с несколькими пиками, мягкой волной и простором всей дуги Кудзюкури.",
                    "ja": "九十九里の弧に広がる、遠浅で幅のある砂浜。穏やかな波と複数のピークがあり、のびのびと入れます。",
                },
        },
    "ichinomiya":
        {
            "image": "ichinomiya",
            "region": {
                "en": "Chiba · Chiba North",
                "ru": "Тиба · Тиба Кита",
                "ja": "千葉・千葉北"
            },
            "summary":
                {
                    "en":
                        "Chiba’s surf centre: mobile sandbanks, east swell, a deep surf culture and consistently busy line-ups from Ichinomiya to Shidashita.",
                    "ru":
                        "Сёрф-центр Тибы: подвижные песчаные банки, восточный свелл, глубокая сёрф-культура и неизменно оживлённые лайн-апы от Итиномии до Сидаситы.",
                    "ja":
                        "千葉のサーフィンの中心地。変化するサンドバー、東うねり、深いサーフカルチャーがあり、一宮から志田下までラインナップはいつも活気があります。",
                },
        },
    "katsuura":
        {
            "image": "katsuura",
            "region": {
                "en": "Chiba · Chiba South",
                "ru": "Тиба · Тиба Минами",
                "ja": "千葉・千葉南"
            },
            "summary":
                {
                    "en":
                        "South-facing Onjuku brings a gentler rhythm: open white sand, south-east to south swell and room beyond the harbour peak.",
                    "ru":
                        "Обращённый на юг Ондзюку — более спокойный ритм: белый песок, юго-восточный и южный свелл, свободное место за пределами пика у гавани.",
                    "ja":
                        "南に開く御宿は少しゆったりした雰囲気。白い砂浜に南東〜南うねりが入り、港のピークを離れると余裕があります。",
                },
        },
    "south-boso":
        {
            # Keep the existing Fujisawa photograph while the overview moves
            # to the new South Boso area.
            "image": "fujisawa",
            "region": {
                "en": "Chiba · South Boso",
                "ru": "Тиба · Южный Босо",
                "ja": "千葉・南房総"
            },
            "summary":
                {
                    "en":
                        "A Pacific-facing stretch around Kamogawa and Chikura: south to south-east swell, varied sandy peaks and a quieter, more open feel at the foot of the Boso Peninsula.",
                    "ru":
                        "Обращённый к Тихому океану берег от Камогавы до Тикуры: южный и юго-восточный свелл, разные песчаные пики и более спокойный простор у оконечности полуострова Босо.",
                    "ja":
                        "鴨川から千倉にかけて太平洋に開く海岸。南〜南東うねり、変化に富む砂のピーク、房総半島の先端らしい開放感が魅力です。",
                },
        },
}

# Area-page copy stays with the structured area data instead of being shared
# indiscriminately by every coastline.  The overview summary above introduces
# an area; this longer text explains how its shore shapes the surf.
AREA_COAST_COPY = {
    "asahi":
        {
            "en":
                "A sandy beach with a gently sloping seabed. Lines of tetrapods run parallel to the shore. Suitable tide levels are low and mid, and more rarely high. The best swell directions run from east through south-southwest. In the north-eastern part (Mansionsita), soft waves suitable for longboards can form. The south-western side of the area is characterised by higher, faster waves, more suitable for mid-length and short boards.",
            "ru":
                "Песчаный пляж с плавным понижением дна. Параллельно берегу расположены гряды тетраподов. Подходящие уровни прилива — низкий и средний, реже высокий. Лучшие направления свелла — с восточного по юго-юго-западный. В северо-восточной части («Мансёнсита») могут формироваться мягкие волны, хорошие для длинных досок. Юго-западная сторона района характеризуется более высокими и быстрыми волнами, подходящими скорее для средних и коротких досок.",
            "ja":
                "緩やかに深くなる砂浜です。海岸と平行にテトラポッドの列が並んでいます。向く潮位はロー〜ミドルで、ハイタイドはまれです。うねりは東から南南西までがよく、北東側のマンション下ではロングボード向きの緩やかな波が立つことがあります。エリア南西側はよりサイズがあり速い波で、ミッドレングスやショートボードにより向いています。",
        },
    "sosa":
        {
            "en":
                "Sosa is part of the long, open Kujukuri shoreline: a broad sandy beach with no headlands to shelter it from east-to-south swell. Sandbars and peaks move along the beach rather than holding to one fixed take-off, so there is usually room to look beyond the busiest cluster. As the surf grows, check the banks and channels before paddling out: the same open coast that spreads the crowd can also set up strong currents.",
            "ru":
                "Соса лежит на длинном открытом берегу Кудзюкури: это широкий песчаный пляж без мысов, защищающих его от свелла с востока и юга. Банки и пики здесь смещаются вдоль берега, а не держатся за одной постоянной точкой, поэтому обычно можно найти место в стороне от самого плотного лайн-апа. С ростом волн сначала оцените банки и каналы: открытый берег, который рассеивает людей, способен создавать и сильные течения.",
            "ja":
                "匝瑳は、東〜南うねりを遮る岬のない、長く開けた九十九里海岸の一部です。砂のバンクとピークは一つの場所に固定されず海岸線に沿って動くため、混む場所から少し離れて探す余地があります。サイズが上がったら、入る前にバンクとカレントを確認しましょう。人が分散する開けた海岸は、強い流れも作りやすい場所です。",
        },
    "sakuta":
        {
            "en":
                "Sakuta is a wide, shallow section of Kujukuri with a sandy bottom and several peaks spread across the beach. Its gradual profile keeps many days approachable, while the bars and tide decide where the cleanest walls appear. North-west wind is the usual cleaner; north-east through south-east swell has an open path into the coast. The wide shore gives surfers a choice of peaks, but it is still worth checking the channels before entering on a larger day.",
            "ru":
                "Сакута — широкий пологий участок Кудзюкури с песчаным дном и несколькими пиками, распределёнными по пляжу. Благодаря плавному профилю многие дни здесь дружелюбны, а банки и прилив определяют, где появятся самые чистые стенки. Обычно волну собирает северо-западный ветер; свелл с северо-востока до юго-востока свободно приходит к берегу. Простор даёт выбор пиков, но в более крупный день всё равно стоит сначала проверить каналы.",
            "ja":
                "作田は、砂地で遠浅な九十九里の広い区間です。ビーチに複数のピークが広がり、緩やかな地形のおかげで入りやすい日が多い一方、きれいなフェイスが出る場所はバンクと潮位で変わります。北西風が整えやすく、北東〜南東のうねりが入りやすい海岸です。ピークを選べる広さはありますが、サイズのある日は先にカレントを確認しましょう。",
        },
    "ichinomiya":
        {
            "en":
                "Ichinomiya is an exposed sandy coast where jetties, river mouths and mobile banks divide a long beach into changing peaks. East swell arrives directly, while west wind is the familiar cleaner. The variety makes the area useful across many conditions, but it also means that the best take-off can move after a tide change or a storm. It is Chiba's busiest surf hub: watch the rotation, choose a peak that suits your level and give regulars space.",
            "ru":
                "Итиномия — открытый песчаный берег, где молы, устья рек и подвижные банки разбивают длинный пляж на меняющиеся пики. Восточный свелл приходит сюда напрямую, а западный ветер обычно выравнивает волну. Разнообразие работает в разных условиях, но лучший пик может сместиться после смены прилива или шторма. Это один из самых оживлённых сёрф-центров Тибы: следите за очередью, выбирайте пик по своему уровню и оставляйте место локалам.",
            "ja":
                "一宮は、堤防、河口、変化するサンドバーが長い砂浜をいくつもの動くピークに分ける開けた海岸です。東うねりが正面から入り、西風が整えやすい条件です。幅広いコンディションに対応できますが、潮位の変化やストームの後には良いテイクオフも移ります。千葉でも特に混むサーフハブなので、順番を見て、自分のレベルに合うピークを選び、ローカルにスペースを譲りましょう。",
        },
    "katsuura":
        {
            "en":
                "This area centres on Onjuku's south-facing crescent of white sand. Harbour works and the river mouth help organise different peaks along an otherwise open beach, and south-east through south swell tends to be the most direct fit. North wind can clean the surface. Compared with the most exposed beaches farther north, the bay often feels more relaxed, yet the harbour and river-mouth channels still deserve a careful look before you paddle out.",
            "ru":
                "Этот район сосредоточен вокруг южной дуги белого песка в Ондзюку. Гавань и устье реки помогают формировать разные пики вдоль в остальном открытого пляжа; лучше всего сюда приходит свелл с юго-востока до юга. Северный ветер способен очистить поверхность. По сравнению с наиболее открытыми пляжами севернее, бухта часто ощущается спокойнее, но перед выходом всё равно внимательно оцените каналы у гавани и устья.",
            "ja":
                "このエリアの中心は、御宿の南に開く白い砂浜の弧です。港と河口が、基本は開けたビーチにいくつかの異なるピークを作ります。南東〜南うねりが合いやすく、北風は面を整えます。北側の特に開けたビーチより穏やかに感じることが多い一方、港と河口まわりのカレントは、入水前に必ずよく確認してください。",
        },
    "fujisawa":
        {
            "en":
                "Kugenuma is a wide, shallow sandy beach shaped by moving bars and the nearby Katase River mouth. South swell is the familiar engine, while north to north-east wind can clean the surface. The gentle profile makes the beach useful for learning and small boards alike, but the same accessible coast draws a dense line-up. Check the river-mouth channels and choose a less crowded peak when the main bank is busy.",
            "ru":
                "Кугэнума — широкий пологий песчаный пляж с подвижными банками и близким устьем реки Катасэ. Главный двигатель здесь — южный свелл, а северный и северо-восточный ветер могут очистить поверхность. Мягкий профиль подходит и для обучения, и для небольших досок, но доступный берег собирает плотный лайн-ап. Проверяйте каналы у устья и, когда главный пик занят, выбирайте менее людный участок.",
            "ja":
                "鵠沼は、動くサンドバーと近くの片瀬川河口によって形づくられる、広く遠浅な砂浜です。南うねりが主な原動力で、北〜北東風が面を整えます。緩やかな地形は練習にも小波用ボードにも向きますが、アクセスのよい海岸だけにラインナップは密になりやすいです。河口のカレントを確認し、メインバンクが混むときは空いているピークを選びましょう。",
        },
    "south-boso":
        {
            "en":
                "South Boso follows the Pacific-facing shore from Wada through Kamogawa towards Shirahama. Sandy beaches, river mouths and occasional reefy sections divide the coast into different peaks, so the same south to south-east swell can work differently from one bay to the next. A west to north-west wind often cleans the surface, but tides, channels and exposed reef still need a careful check before you paddle out.",
            "ru":
                "Южный Босо тянется по обращённому к Тихому океану берегу от Камогавы через Тикуру к Сирахаме. Песчаные пляжи, устья рек и местами рифовые участки разбивают его на разные пики, поэтому один и тот же южный или юго-восточный свелл по-разному работает в соседних бухтах. Западный и северо-западный ветер часто очищают поверхность, но перед выходом всё равно внимательно оцените прилив, каналы и открытый риф.",
            "ja":
                "南房総は、鴨川から千倉を経て白浜へ続く太平洋に開いた海岸です。砂浜、河口、ときにリーフが海岸線を異なるピークに分けるため、同じ南〜南東うねりでも湾ごとに表情が変わります。西〜北西風が面を整えやすい一方、入水前には潮位、カレント、露出したリーフを必ず確認してください。",
        },
}

# Detailed spot pages live inside their parent area.  These deliberately keep
# their compact facts separate from csv/spots.csv, which compares the six
# navigation areas rather than every individual break.
SPOT_FACT_TRANSLATIONS = {
    "ru":
        {
            "labels":
                {
                    "Area": "Район",
                    "Break": "Брейк",
                    "Bottom": "Дно",
                    "Min. Level": "Мин. уровень",
                    "Level": "Уровень",
                    "Working tide": "Подходящий уровень воды",
                    "Season": "Сезон",
                    "Best size": "Лучший размер",
                    "Crowds": "Люди",
                    "Best board": "Подходящая доска",
                },
            "values":
                {
                    "Chiba North · Iioka": "Северная Тиба · Ииока",
                    "Chiba North · Kujukuri": "Северная Тиба · Кудзюкури",
                    "Chiba North · Asahi": "Северная Тиба · Асахи",
                    "Chiba North · Sosa": "Северная Тиба · Соса",
                    "beach break between tetrapods": "бич-брейк между тетраподами",
                    "hollow beach break": "холлоу-бич-брейк",
                    "wide beach break": "широкий бич-брейк",
                    "open beach break": "открытый бич-брейк",
                    "shallow beach break": "пологий бич-брейк",
                    "Sand": "Песчаное",
                    "beginner": "начинающий",
                    "intermediate": "средний",
                    "beginner to advanced, depending on conditions": "от начинающего до продвинутого — по условиям",
                    "beginner to intermediate": "начинающий — средний",
                    "low to high": "от низкого до высокого",
                    "mid to mid-low": "средний — средне-низкий",
                    "medium to high": "от среднего до высокого",
                    "year-round; especially autumn–winter": "круглый год; особенно осень — зима",
                    "autumn–winter": "осень — зима",
                    "chest to shoulder high": "по грудь — по плечи",
                    "waist to chest high": "по пояс — по грудь",
                    "Popular, with room to choose a peak": "Популярно, но можно выбрать пик",
                    "Usually quieter than nearby named peaks": "Обычно спокойнее, чем на ближайших известных пиках",
                    "longboard": "лонгборд",
                    "shortboard": "шортборд",
                    "shortboard, funboard": "шортборд, фанборд",
                    "shortboard, funboard, longboard": "шортборд, фанборд, лонгборд",
                    "longboard, funboard, shortboard": "лонгборд, фанборд, шортборд",
                },
        },
    "ja":
        {
            "labels":
                {
                    "Area": "エリア",
                    "Break": "ブレイク",
                    "Bottom": "海底",
                    "Min. Level": "レベル",
                    "Level": "レベル",
                    "Working tide": "対応する潮位",
                    "Season": "シーズン",
                    "Best size": "ベストサイズ",
                    "Crowds": "混雑",
                    "Best board": "向くボード",
                },
            "values":
                {
                    "Chiba North · Iioka": "千葉北・飯岡",
                    "Chiba North · Kujukuri": "千葉北・九十九里",
                    "Chiba North · Asahi": "千葉北・旭",
                    "Chiba North · Sosa": "千葉北・匝瑳",
                    "beach break between tetrapods": "テトラポッドの間のビーチブレイク",
                    "hollow beach break": "ホローなビーチブレイク",
                    "wide beach break": "広いビーチブレイク",
                    "open beach break": "開けたビーチブレイク",
                    "shallow beach break": "遠浅のビーチブレイク",
                    "Sand": "砂地",
                    "beginner": "初級者以上",
                    "intermediate": "中級者以上",
                    "beginner to advanced, depending on conditions": "初級〜上級（コンディション次第）",
                    "beginner to intermediate": "初級〜中級",
                    "low to high": "ロー〜ハイ",
                    "mid to mid-low": "ミドル〜ミドルロー",
                    "medium to high": "中〜高",
                    "year-round; especially autumn–winter": "通年、特に秋〜冬",
                    "autumn–winter": "秋〜冬",
                    "chest to shoulder high": "ムネ〜カタ",
                    "waist to chest high": "コシ〜ムネ",
                    "Popular, with room to choose a peak": "人気はあるがピークを選べる",
                    "Usually quieter than nearby named peaks": "近くの有名なピークより比較的落ち着く",
                    "longboard": "ロングボード",
                    "shortboard": "ショートボード",
                    "shortboard, funboard": "ショートボード、ファンボード",
                    "shortboard, funboard, longboard": "ショートボード、ファンボード、ロングボード",
                    "longboard, funboard, shortboard": "ロングボード、ファンボード、ショートボード",
                },
        },
}


def localized_spot_facts(rows, lang):
    """Translate the English-only detailed-spot facts during the site build."""
    if lang == "en":
        return rows

    translation = SPOT_FACT_TRANSLATIONS[lang]
    return [(translation["labels"][label], translation["values"][value]) for label, value in rows]


SPOT_DETAILS = {
    "mansionsita":
        {
            "area": "asahi",
            "title": {
                "en": "Mansionsita",
                "ru": "Мансёнсита",
                "ja": "マンション下",
            },
            "summary":
                {
                    "en": "A smaller, gentler beach break between the tetrapods on Iioka’s north-east side.",
                    "ru": "Более мягкий и обычно меньший бич-брейк между тетраподами в северо-восточной части Ииоки.",
                    "ja": "飯岡の北東側、テトラポッドの間で割れる、比較的サイズが小さく穏やかなビーチブレイク。",
                },
            "description":
                {
                    "en":
                        "Mansionsita is often softer than the breaks farther south in Asahi, so longer boards tend to be the natural choice. The sandbanks shift regularly, but when they line up, rides of up to 100 metres are possible. In the north-east corner, a pocket known as ‘Silver’ sits behind the first line of tetrapods and produces small, smooth, forgiving waves, so it often draws many beginners.",
                    "ru":
                        "В Мансёнсите волны часто мягче, чем на спотах южнее в районе Асахи, поэтому здесь естественно выбирать более длинные доски. Рельеф дна регулярно меняется, но иногда при благоприятных условиях возможны длинные проезды протяжённостью до 100 м. Северо-восточный угол закрытый первой грядой тетраподов, называемый «Сильвер», даёт ровные, небольшие и мягкие волны, поэтому часто собирает много начинающих серферов.",
                    "ja":
                        "マンション下は、旭エリアで南にあるポイントよりも波が柔らかいことが多く、長めのボードが自然に合います。海底地形は頻繁に変わりますが、条件が整えば100メートルほどのロングライドができることもあります。北東側の最初のテトラポッド列に守られた一角は「シルバー」と呼ばれ、小さく整った穏やかな波が立つため、初心者が多く集まります。",
                },
            "facts":
                [
                    ("Area", "Chiba North · Iioka"),
                    ("Break", "beach break between tetrapods"),
                    ("Bottom", "Sand"),
                    ("Min. Level", "beginner"),
                    ("Working tide", "low to high"),
                    ("Best board", "longboard"),
                ],
            "amenities": [],
        },
    "shingosita":
        {
            "area":
                "asahi",
            "title": {
                "en": "Shingosita",
                "ru": "Сингосита",
                "ja": "信号下",
            },
            "summary":
                {
                    "en": "A hollow beach break with occasional barrels, shaped by the swell direction and the tetrapods.",
                    "ru": "Холлоу-бич-брейк с возможными трубами; его характер меняется в зависимости от направления свелла и тетраподов.",
                    "ja": "うねりの向きとテトラポッドで波質が変わる、ときにバレルも現れるホローなビーチブレイク。",
                },
            "description":
                {
                    "en":
                        "When the surf has size, faster hollow sections can appear and may suit shortboards; gentler, thicker waves can be better for longboards. Both lefts and rights can run, although the final section often closes out. When the conditions line up, three peaks can form and a tube is possible. Complex currents develop around the tetrapods: choose a paddle-out that stays clear of riders, and take particular care outside the blocks.",
                    "ru":
                        "Когда свелл набирает размер, могут появляться быстрые холлоу-секции, подходящие для шортбордов; при более мягкой и толстой волне лучше подойдёт лонгборд. Здесь возможны и правые, и левые волны, хотя финальная секция часто закрывается. При удачном совпадении условий могут сформироваться три пика и труба. У тетраподов возникают сложные течения: выбирайте выход в воду так, чтобы не мешать катающимся, и особенно внимательно следите за течением с внешней стороны блоков.",
                    "ja":
                        "信号下では、サイズが上がると掘れた速いセクションが現れ、ショートボード向きになることがあります。緩やかで厚めの波ではロングボードにも向きます。レギュラー、グーフィーともに乗れますが、最後のセクションはクローズアウトしやすい傾向があります。条件がそろうと三つのピークができ、チューブになることもあります。テトラポッド周辺には複雑なカレントがあるため、ライディングしている人の妨げにならないルートで沖へ出て、特にブロックのアウト側では流れをよく確認してください。",
                },
            "facts":
                [
                    ("Area", "Chiba North · Iioka"),
                    ("Break", "hollow beach break"),
                    ("Bottom", "Sand"),
                    ("Level", "beginner to advanced, depending on conditions"),
                    ("Season", "year-round; especially autumn–winter"),
                    ("Best size", "chest to shoulder high"),
                    ("Working tide", "mid to mid-low"),
                    ("Best board", "longboard, funboard, shortboard"),
                ],
        },
    "shoppumae":
        {
            "area":
                "asahi",
            "title": {
                "en": "Shoppumae",
                "ru": "Сёппумаэ",
                "ja": "ショップ前",
            },
            "summary":
                {
                    "en": "Sensitive to swell, producing high, fast waves. Suitable for shortboards.",
                    "ru": "Чувствителен к свелу, рождает высокие быстые волны. Подходит для шортбордов.",
                    "ja": "うねりに敏感で、高く速い波が立つ。ショートボードに適している。",
                },
            "description":
                {
                    "en":
                        "The area in front of the Shiosai Hotel is easily accessible — there is free parking, restrooms, and showers. The waves here are higher and steeper than at the spots further north, and they often close out.",
                    "ru":
                        "Область перед гостиницей Сиёсай имеет удобный доступ — есть бесплатная парковка, туалет и душ. Волны здесь выше и круче, чем на спотох севернее, но часто бывает клоз-аут.",
                    "ja":
                        "潮騒ホテルの前のエリアはアクセスが良く、無料駐車場、トイレ、シャワーが完備されています。ここは、さらに北にあるスポットよりも高く、ホレタ波がたちやすく、ダンパーになりやすいです。",
                },
            "amenities": ["parking", "shower", "restroom"],
            "facts":
                [
                    ("Area", "Chiba North · Iioka"),
                    ("Break", "beach break between tetrapods"),
                    ("Bottom", "Sand"),
                    ("Min. Level", "intermediate"),
                    ("Working tide", "medium to high"),
                    ("Best board", "shortboard, funboard"),
                ],
        },
    "sakuta":
        {
            "area":
                "sakuta",
            "title": {
                "en": "Sakuta",
                "ru": "Сакута",
                "ja": "作田",
            },
            "summary":
                {
                    "en": "A broad, gentle beach break beside the Sakuta River, with shifting sandy peaks for a wide range of surfers.",
                    "ru": "Широкий мягкий бич-брейк у реки Сакута с меняющимися песчаными пиками для самого разного уровня.",
                    "ja": "作田川のそばに広がる、緩やかな砂のピークが変化するビーチブレイク。幅広いレベルに合います。",
                },
            "description":
                {
                    "en":
                        "Sakuta is a broad, gently shelving beach where shifting sandbars determine whether the best peak forms beside the groyne or farther down the open stretch. The waves here tend to be soft and full, so the spot is forgiving on smaller days; as the swell builds, the peaks become more defined. Easterly and south-easterly swell reaches the beach cleanly, while westerly to north-westerly winds usually keep the surface tidy. Good weekends can get busy, though the wide beach normally leaves room to spread out. <br><b style='color:darkred'>The right-hand side of the spot, closest to the groyne, is reserved for shortboards and funboards only</b>; the left-hand side is open to everyone.",
                    "ru":
                        "Сакута — широкий пологий пляж, где песчаные банки определяют, окажется ли лучший пик у мола или дальше на открытом берегу. Волна здесь часто мягкая и полная, поэтому в небольшой день она дружелюбна; с ростом размера пики становятся отчётливее. Свелл с востока и юго-востока свободно приходит к пляжу, а западный и северо-западный ветер обычно очищают поверхность. В выходные при хороших условиях на море бывает многолюдно, но на широком пляже обычно можно найти место. <br><b style='color:darkred'>Правая сторона спота, которая ближе к молу, предназначена только для шортбордов и фанбордов</b>, а левая сторона открыта для всех.",
                    "ja":
                        "作田は、砂のバンク次第で堤防脇にピークが立つか、開けたビーチの沖に立つかが変わる、広く遠浅なビーチブレイクです。波は厚めでゆったりと割れやすく、小さい日は乗りやすい一方、サイズが上がるとピークがよりはっきりしてきます。東〜南東うねりが入りやすく、西〜北西風で面が整いやすいスポットです。条件のいい週末は混み合いますが、浜が広いのでピークを選ぶ余地はあります。<br><b style='color:darkred'>堤防寄りの右側はショートボードとファンボード専用です</b>。左側はどなたでも利用できます。",
                },
            "amenities": ["paid_parking", "shower", "restroom"],
            "facts":
                [
                    ("Area", "Chiba North · Kujukuri"),
                    ("Break", "wide beach break"),
                    ("Bottom", "Sand"),
                    ("Level", "beginner to advanced, depending on conditions"),
                    ("Crowds", "Popular, with room to choose a peak"),
                    ("Best board", "shortboard, funboard, longboard"),
                ],
        },
    "motosuka":
        {
            "area":
                "sakuta",
            "title": {
                "en": "Motosuka",
                "ru": "Мотоска",
                "ja": "本須賀",
            },
            "summary":
                {
                    "en": "A quiet, open section of Kujukuri with evenly spaced sandy peaks and room to practise away from the busier breaks.",
                    "ru": "Спокойный открытый участок Кудзюкури с ровно распределёнными песчаными пиками и местом для практики вдали от самых людных брейков.",
                    "ja": "砂のピークが均等に並ぶ、九十九里の静かで開けた区間。混むポイントから離れて練習する余地があります。",
                },
            "description":
                {
                    "en":
                        "Motosuka is an open sandy section of the Kujukuri coast with few fixed landmarks, so the best take-off moves with the banks and tide. North-east to east swell reaches the beach directly and usually produces smaller, manageable waves outside larger systems. The open coast gives more space than the named peaks nearby, but it also means currents can change after a swell. Look for a defined peak and a safe channel before paddling out.",
                    "ru":
                        "Мотоска — открытый песчаный участок Кудзюкури почти без постоянных ориентиров, поэтому лучший тейк-офф перемещается вместе с банками и приливом. Свелл с северо-востока и востока приходит сюда напрямую и вне крупных свеллов обычно даёт небольшие, контролируемые волны. Открытый берег даёт больше пространства, чем ближайшие известные пики, но после свелла течения могут меняться. Перед выходом найдите выраженный пик и безопасный канал.",
                    "ja":
                        "本須賀は、固定された目印が少ない九十九里の開けた砂浜です。良いテイクオフはバンクと潮位に合わせて動きます。北東〜東うねりが直接入り、大きなうねりがない日は扱いやすい小さめの波になりやすい場所です。近くの名前のあるピークより余裕がありますが、ストームの後はカレントも変わります。入水前に形のよいピークと安全なチャンネルを探しましょう。",
                },
            "amenities": ["parking", "shower", "restroom"],
            "facts":
                [
                    ("Area", "Chiba North · Kujukuri"),
                    ("Break", "open beach break"),
                    ("Bottom", "Sand"),
                    ("Level", "beginner to intermediate"),
                    ("Crowds", "Usually quieter than nearby named peaks"),
                    ("Best board", "shortboard, funboard, longboard"),
                ],
        },
    "kanpomae":
        {
            "area":
                "asahi",
            "title": {
                "en": "Kanpomae",
                "ru": "Канпомаэ",
                "ja": "かんぽ前",
            },
            "summary":
                {
                    "en": "A mellow, shallow beach break that stays surfable on smaller days and suits a range of boards.",
                    "ru": "Мягкий пологий бич-брейк: здесь можно кататься и в небольшой день, а выбор досок широк.",
                    "ja": "小波の日でもサーフしやすく、幅広いボードで楽しめる遠浅なビーチブレイク。",
                },
            "description":
                {
                    "en":
                        "Kanpomae, also known as Nakayarihama, is an open sandy beach facing south-south-east. East through south swell reaches the shallow banks, where smaller days tend to be mellow and forgiving enough for longer boards. Once the surf rises above head high, the peaks can become wide and close out more often. The line-up can be busy and has a local character, so watch the break first, follow the established order, and give people space. Check the rightward current when the swell has size.",
                    "ru":
                        "Канпомаэ, также известный как Накаярихама, — открытый песчаный пляж, обращённый на юго-юго-восток. Свелл с востока до юга приходит к пологим банкам; в небольшой день волна здесь обычно мягкая и подходит для длинных досок. При размере выше головы пики становятся шире и чаще закрываются. В лайн-апе бывает многолюдно, а у места выраженный локальный характер: сначала понаблюдайте за волной, соблюдайте порядок и оставляйте другим пространство. При большом свелле следите за течением вправо.",
                    "ja":
                        "かんぽ前は中谷里浜とも呼ばれる、南南東に開いた砂浜です。東〜南うねりが遠浅のバンクに入り、小さい日は厚く穏やかな波になりやすいため、長めのボードにも合います。頭を超えるサイズではピークがワイドになり、クローズアウトも増えます。ラインナップは混みやすくローカル色もあるため、入水前に波を観察し、順番を守って周囲に十分なスペースを譲りましょう。サイズがある日は右へのカレントにも注意が必要です。",
                },
            "amenities": ["parking", "restroom"],
            "facts":
                [
                    ("Area", "Chiba North · Asahi"),
                    ("Break", "shallow beach break"),
                    ("Bottom", "Sand"),
                    ("Level", "beginner to advanced, depending on conditions"),
                    ("Season", "autumn–winter"),
                    ("Best size", "waist to chest high"),
                    ("Best board", "longboard, funboard, shortboard"),
                ],
        },
    "nodehama":
        {
            "area": "sosa",
            "title": {
                "en": "Nodehama",
                "ru": "Нодэхама",
                "ja": "野手浜",
            },
            "summary": {
                "en": "A mellow, shallow beach break in Sosa that stays surfable on smaller south-east swell.",
                "ru": "Мягкий пологий бич-брейк в Сосе, где можно кататься и при небольшом юго-восточном свелле.",
                "ja": "南東うねりの小波の日でもサーフしやすい、匝瑳の遠浅なビーチブレイク。",
            },
            "description": {
                "en": "Nodehama is an open sandy beach facing south-east. It responds to swell from north-east through south-south-west and often has manageable waves even on smaller days. The gently sloping seabed makes the wave soft, with shoulders that do not always stand up strongly, so it is a relaxed option for beginners and longboards. Waist- to chest-high surf is the usual sweet spot; when the waves rise above head high, the peaks can become wide and close out. Check the banks and current before paddling out, and give other surfers room in the line-up.",
                "ru": "Нодэхама — открытый песчаный пляж, обращённый на юго-восток. Он принимает свелл от северо-востока до юго-юго-запада и часто даёт управляемые волны даже в небольшой день. Пологий рельеф дна делает волну мягкой, а плечо не всегда встаёт круто, поэтому место подходит начинающим и лонгбордам. Лучшее окно обычно от пояса до груди; при размере выше головы пики становятся широкими и чаще закрываются. Перед выходом проверьте банки и течение и оставляйте другим место в лайн-апе.",
                "ja": "野手浜は南東に開いた砂浜です。北東〜南南西のうねりに反応し、小波の日でも楽しみやすいポイントです。遠浅の地形で波は厚め、ショルダーも張りにくいため、初級者やロングボードにも向きます。コシ〜ムネ程度が狙い目で、頭を超えるとピークはワイドになりクローズアウトが増えます。入水前にバンクとカレントを確認し、ラインナップでは周囲にスペースを譲りましょう。",
            },
            "amenities": [],
            "facts": [
                ("Area", "Chiba North · Sosa"),
                ("Break", "shallow beach break"),
                ("Bottom", "Sand"),
                ("Level", "beginner to advanced, depending on conditions"),
                ("Best size", "waist to chest high"),
                ("Best board", "longboard, funboard, shortboard"),
            ],
        },
    "horikawa":
        {
            "area": "sosa",
            "title": {
                "en": "Horikawa",
                "ru": "Хорикава",
                "ja": "堀川",
            },
            "summary": {
                "en": "A mellow, shallow beach break in southern Sosa that works well on smaller south-east swell.",
                "ru": "Мягкий пологий бич-брейк на юге Сосы, хорошо работающий при небольшом юго-восточном свелле.",
                "ja": "南東うねりの小波の日でも楽しみやすい、匝瑳南部の遠浅なビーチブレイク。",
            },
            "description": {
                "en": "Horikawa (also called Horikawahama) is an open sandy beach facing south-east. It responds to swell from north-east through south-south-west and can offer a gentle, manageable wave when other nearby breaks are small. The seabed shelves gradually, so the wave is usually soft rather than steep and is friendly to beginners and longer boards. Waist- to chest-high surf is generally the most enjoyable; above head high, peaks tend to become wider and close out more often. Conditions can change along this open coast, so check the banks and current before entering.",
                "ru": "Хорикава, также известная как Хорикавахама, — открытый песчаный пляж, обращённый на юго-восток. Он принимает свелл от северо-востока до юго-юго-запада и может давать мягкую, управляемую волну, когда соседние брейки малы. Дно понижается плавно, поэтому волна обычно не крутая и подходит начинающим и более длинным доскам. Лучше всего обычно от пояса до груди; при размере выше головы пики расширяются и чаще закрываются. На этом открытом берегу условия быстро меняются, поэтому перед входом проверьте банки и течение.",
                "ja": "堀川（堀川浜とも呼ばれます）は南東に開いた砂浜です。北東〜南南西のうねりに反応し、周辺が小さい日にも厚く扱いやすい波が期待できます。海底は遠浅で、波は急というより穏やかになりやすく、初級者や長めのボードにも向きます。コシ〜ムネ程度が楽しみやすく、頭を超えるとピークはワイドになりクローズアウトが増えます。開けた海岸なので、入水前にバンクとカレントを確認しましょう。",
            },
            "amenities": [],
            "facts": [
                ("Area", "Chiba North · Sosa"),
                ("Break", "shallow beach break"),
                ("Bottom", "Sand"),
                ("Level", "beginner to advanced, depending on conditions"),
                ("Best size", "waist to chest high"),
                ("Best board", "longboard, funboard, shortboard"),
            ],
        },
    "ichinomiya":
        {
            "area":
                "ichinomiya",
            "title": {
                "en": "Ichinomiya",
                "ru": "Итиномия",
                "ja": "一宮"
            },
            "summary":
                {
                    "en": "A sandy beach break near Ichinomiya, where the banks and conditions set the usable peaks.",
                    "ru": "Песчаный бич-брейк в Итиномии, где рабочие пики зависят от банок и условий.",
                    "ja": "一宮の砂浜にあるビーチブレイク。バンクとコンディションで使えるピークが変わります。",
                },
            "description":
                {
                    "en":
                        "This spot is sensitive to swells coming from different directions. The waves here are often bigger than at neighboring beaches. It's usually crowded. The central and southern sections between the piers are reserved for shortboards and funboards, while the northern section is open to everyone.",
                    "ru":
                        "Спот чувствителен к свелу с разных направлений. Часто волны здесь выше, чем на соседних пляжах. Обычно бывает многолюдно. Центральная и южная части между молами только для шортбордов и фанбордов, а северная часть открыта для всех.",
                    "ja":
                        "一宮は、幅広い方向からのうねりの影響を受けやすい。波は、近隣のスポットよりも大きくなることが多い。通常、混雑しています。このポイントの中央堤防右～右ヘッドランドにかけてはロングボード不可とされています。",
                },
            "amenities": ["paid_parking", "restroom", "shower"],
            "facts":
                [
                    ("Area", "Chiba North · Sosa"),
                    ("Break", "shallow beach break"),
                    ("Bottom", "Sand"),
                    ("Level", "beginner to advanced, depending on conditions"),
                    ("Season", "autumn–winter"),
                    ("Best size", "waist to chest high"),
                    ("Best board", "longboard, funboard, shortboard"),
                ],
        },
    "taito":
        {
            "area": "ichinomiya",
            "title": {
                "en": "Taito",
                "ru": "Тайто",
                "ja": "太東"
            },
            "summary":
                {
                    "en": "An open beach break south of Ichinomiya, with sandbars that respond quickly to changing swell.",
                    "ru": "Открытый бич-брейк к югу от Итиномии с песчаными банками, быстро меняющимися под свеллом.",
                    "ja": "一宮の南にある開けたビーチブレイク。砂のバンクはうねりの変化に敏感です。",
                },
            "description":
                {
                    "en":
                        "Taito is an exposed sandy stretch where the best peak can move after a swell. Watch the lineup first and locate a channel before paddling out, especially when the surf has size.",
                    "ru":
                        "Тайто — открытый песчаный участок, где лучший пик может сместиться после свелла. Перед выходом понаблюдайте за лайн-апом и найдите канал, особенно в большой день.",
                    "ja":
                        "太東は開けた砂浜で、うねりの後には良いピークの位置が変わることがあります。特にサイズがある日は、まずラインナップを見てチャンネルを確認してから沖へ出ましょう。",
                },
        },
    "onjuku main":
        {
            "area": "katsuura",
            "title": {
                "en": "Onjuku Main",
                "ru": "Ондзюку мэйн",
                "ja": "御宿メイン"
            },
            "summary":
                {
                    "en": "The central beach break at Onjuku, where a broad sandy shoreline offers several changing peaks.",
                    "ru": "Центральный бич-брейк Ондзюку: широкий песчаный берег с несколькими меняющимися пиками.",
                    "ja": "御宿の中央にあるビーチブレイク。広い砂浜に変化するピークがいくつか現れます。",
                },
            "description":
                {
                    "en":
                        "Onjuku Main is a wide sandy beach whose banks and currents change with the swell. Check where the defined peaks are breaking and keep clear of other surfers when choosing a paddle-out route.",
                    "ru":
                        "Ондзюку мэйн — широкий песчаный пляж, где банки и течения меняются вместе со свеллом. Проверьте, где работают выраженные пики, и не пересекайте линии других серферов на выходе в воду.",
                    "ja":
                        "御宿メインは、うねりに合わせてバンクとカレントが変わる広い砂浜です。どこで形のよいピークが割れているかを確認し、沖へ出るときはほかのサーファーのラインを横切らないようにしましょう。",
                },
        },
    "iwawada":
        {
            "area": "katsuura",
            "title": {
                "en": "Onjuku Iwawada",
                "ru": "Ондзюку Ивавада",
                "ja": "御宿 岩和田"
            },
            "summary":
                {
                    "en": "A beach-break section at Iwawada on the eastern side of Onjuku Bay.",
                    "ru": "Участок бич-брейка в Иваваде на восточной стороне бухты Ондзюку.",
                    "ja": "御宿湾の東側、岩和田にあるビーチブレイクの区間です。",
                },
            "description":
                {
                    "en":
                        "The sandbanks at Iwawada can form distinct peaks, but their position and the current depend on recent swell and tide. Assess the conditions from the beach before entering.",
                    "ru":
                        "Песчаные банки Ивавады могут формировать выраженные пики, но их положение и течение зависят от недавнего свелла и прилива. Перед выходом оцените условия с берега.",
                    "ja":
                        "岩和田の砂のバンクははっきりしたピークを作ることがありますが、その位置やカレントは直近のうねりと潮位で変わります。入水前に浜からコンディションを確認しましょう。",
                },
        },
    "wadaura":
        {
            "area": "south-boso",
            "title": {
                "en": "Wadaura",
                "ru": "Вадаура",
                "ja": "和田浦"
            },
            "summary":
                {
                    "en": "A South Boso beach break exposed to the Pacific, with conditions that change across the open shoreline.",
                    "ru": "Бич-брейк Южного Босо, открытый Тихому океану; условия меняются вдоль открытого берега.",
                    "ja": "太平洋に開いた南房総のビーチブレイク。開けた海岸線の中でコンディションが変化します。",
                },
            "description":
                {
                    "en":
                        "Wadaura receives south-easterly to southerly swell along an open stretch of coast. The sand and current shift with the conditions, so look for a defined peak and a safe entry before paddling out.",
                    "ru":
                        "Вадаура принимает юго-восточный и южный свелл на открытом участке побережья. Песок и течение меняются по условиям, поэтому перед выходом найдите выраженный пик и безопасный заход в воду.",
                    "ja":
                        "和田浦には、開けた海岸に南東〜南うねりが入ります。砂の付き方とカレントはコンディションで変わるため、沖へ出る前に形のよいピークと安全な入水場所を探しましょう。",
                },
        },
    "chikura":
        {
            "area": "south-boso",
            "title": {
                "en": "Chikura",
                "ru": "Тикура",
                "ja": "千倉"
            },
            "summary":
                {
                    "en": "A South Boso beach break where bays, headlands and sandbanks make each swell feel different.",
                    "ru": "Бич-брейк Южного Босо, где бухты, мысы и песчаные банки по-разному принимают каждый свелл.",
                    "ja": "入り江、岬、砂のバンクによって、うねりごとに表情が変わる南房総のビーチブレイクです。",
                },
            "description":
                {
                    "en":
                        "Chikura faces the Pacific and can change quickly with swell direction and tide. Observe the break before entering, especially around exposed sections of coastline and any changing current.",
                    "ru":
                        "Тикура выходит к Тихому океану и может быстро меняться с направлением свелла и приливом. Перед выходом понаблюдайте за волной, особенно на открытых участках побережья и при меняющемся течении.",
                    "ja":
                        "千倉は太平洋に面し、うねりの向きと潮位でコンディションがすぐ変わることがあります。入水前に波を観察し、特に開けた海岸の区間と変化するカレントに注意してください。",
                },
        },
}

AREA_FACTS = {
    "asahi":
        {
            "en":
                [
                    ("Coast", "Chiba North · Iioka"), ("Breaks", "Sandy beach breaks and tetrapod peaks"), ("Swell", "E–SSW, best with south in the mix"),
                    ("Clean wind", "NNE"), ("Crowds", "Usually room to spread out")
                ],
            "ru":
                [
                    ("Побережье", "Тиба Кита · Ииока"), ("Брейки", "Песчаные пляжи и пики у тетраподов"), ("Свелл", "В–ЮЮЗ, лучше с южной составляющей"),
                    ("Чистый ветер", "ССВ"), ("Люди", "Обычно есть пространство")
                ],
            "ja": [("海岸", "千葉北・飯岡"), ("ブレイク", "砂のビーチブレイクとテトラポッド際のピーク"), ("うねり", "東〜南南西、南寄りが混じると良い"), ("オフショア", "北北東"), ("混雑", "広がれば比較的余裕がある")],
            "spots": {
                "en": ["Mansionsita", "Shingosita", "Shoppumae", "Kanpomae"],
                "ru": ["Мэнсионсита", "Сингосита", "Сёппумаэ", "Канпомаэ"],
                "ja": ["マンション下", "信号下", "ショップ前", "かんぽ前"]
            },
        },
    "sosa":
        {
            "en":
                [
                    ("Coast", "Chiba North · Sosa"), ("Breaks", "Open sandy beach breaks"), ("Swell", "E–S"), ("Clean wind", "N–NW"),
                    ("Crowds", "Visitors, but a less concentrated line-up")
                ],
            "ru":
                [
                    ("Побережье", "Тиба Кита · Соса"), ("Брейки", "Открытые песчаные бич-брейки"), ("Свелл", "В–Ю"), ("Чистый ветер", "С–СЗ"),
                    ("Люди", "Приезжих много, но лайн-ап менее концентрирован")
                ],
            "ja": [("海岸", "千葉北・匝瑳"), ("ブレイク", "開けた砂のビーチブレイク"), ("うねり", "東〜南"), ("オフショア", "北〜北西"), ("混雑", "人は来るがラインナップは集中しにくい")],
            "spots": {
                "en": ["Nodehama", "Horikawa"],
                "ru": ["Нодэхама", "Хорикава"],
                "ja": ["野手浜", "堀川"]
            },
        },
    "sakuta":
        {
            "en":
                [
                    ("Coast", "Chiba North · Kujukuri"), ("Breaks", "Wide, shallow sandy beach"), ("Swell", "NE–SSE"), ("Clean wind", "NW"),
                    ("Crowds", "Popular, with several peaks to choose from")
                ],
            "ru":
                [
                    ("Побережье", "Тиба Кита · Кудзюкури"), ("Брейки", "Широкий пологий песчаный пляж"), ("Свелл", "СВ–ЮЮВ"), ("Чистый ветер", "СЗ"),
                    ("Люди", "Популярно, но можно выбрать пик")
                ],
            "ja": [("海岸", "千葉北・九十九里"), ("ブレイク", "幅広く遠浅な砂浜"), ("うねり", "北東〜南南東"), ("オフショア", "北西"), ("混雑", "人気はあるがピークを選べる")],
            "spots": {
                "en": ["Sakuta"],
                "ru": ["Сакута"],
                "ja": ["作田"]
            },
        },
    "ichinomiya":
        {
            "en":
                [
                    ("Coast", "Chiba North · Ichinomiya"), ("Breaks", "Mobile sandbanks beside jetties"), ("Swell", "NE–SE, especially east"),
                    ("Clean wind", "W"), ("Crowds", "One of Chiba’s busiest surf hubs")
                ],
            "ru":
                [
                    ("Побережье", "Тиба Кита · Итиномия"), ("Брейки", "Подвижные песчаные банки у молов"), ("Свелл", "СВ–ЮВ, особенно восточный"),
                    ("Чистый ветер", "З"), ("Люди", "Один из самых оживлённых сёрф-центров Тибы")
                ],
            "ja": [("海岸", "千葉北・一宮"), ("ブレイク", "堤防脇にできる変化の速いサンドバー"), ("うねり", "北東〜南東、特に東"), ("オフショア", "西"), ("混雑", "千葉でも有数のサーフハブ")],
            "spots": {
                "en": ["Ichinomiya", "Tsurigasaki / Shidashita"],
                "ru": ["Итиномия", "Цуригасаки / Сидасита"],
                "ja": ["一宮", "釣ヶ崎 / 志田下"]
            },
        },
    "katsuura":
        {
            "en":
                [
                    ("Coast", "Chiba South · Onjuku"), ("Breaks", "Open sandy beach, harbour and river-mouth peaks"), ("Swell", "ESE–SSW, especially SE–S"),
                    ("Clean wind", "N"), ("Crowds", "Calmer beyond the harbour peak")
                ],
            "ru":
                [
                    ("Побережье", "Тиба Минами · Ондзюку"), ("Брейки", "Открытый песчаный пляж, пики у гавани и устья"), ("Свелл", "ВЮВ–ЮЮЗ, особенно ЮВ–Ю"),
                    ("Чистый ветер", "С"), ("Люди", "За пределами пика у гавани спокойнее")
                ],
            "ja": [("海岸", "千葉南・御宿"), ("ブレイク", "開けた砂浜、港と河口のピーク"), ("うねり", "東南東〜南南西、特に南東〜南"), ("オフショア", "北"), ("混雑", "港のピークを離れると落ち着く")],
            "spots": {
                "en": ["Onjuku"],
                "ru": ["Ондзюку"],
                "ja": ["御宿"]
            },
        },
    "fujisawa":
        {
            "en":
                [
                    ("Coast", "Kanagawa · Shonan"), ("Breaks", "Shallow sandy beach and river-mouth bars"), ("Swell", "E–SW, especially south"),
                    ("Clean wind", "N–NE"), ("Crowds", "One of Japan’s busiest line-ups")
                ],
            "ru":
                [
                    ("Побережье", "Канагава · Сёнан"), ("Брейки", "Пологий песчаный пляж и банки у устья"), ("Свелл", "В–ЮЗ, особенно южный"),
                    ("Чистый ветер", "С–СВ"), ("Люди", "Один из самых оживлённых лайн-апов Японии")
                ],
            "ja": [("海岸", "神奈川・湘南"), ("ブレイク", "遠浅の砂浜と河口のサンドバー"), ("うねり", "東〜南西、特に南"), ("オフショア", "北〜北東"), ("混雑", "日本でも特に混むラインナップの一つ")],
            "spots": {
                "en": ["Kugenuma"],
                "ru": ["Кугэнума"],
                "ja": ["鵠沼"]
            },
        },
    "south-boso":
        {
            "en":
                [
                    ("Coast", "Chiba South · Kamogawa to Chikura"), ("Breaks", "Sandy beaches, river mouths and occasional reef"), ("Swell", "S–SE"),
                    ("Clean wind", "W–NW"), ("Crowds", "Varied peaks along an open coast")
                ],
            "ru":
                [
                    ("Побережье", "Южная Тиба · от Каомгавы до Тикуры"), ("Брейки", "Песчаные пляжи, устья и местами риф"), ("Свелл", "Ю–ЮВ"),
                    ("Чистый ветер", "З–СЗ"), ("Люди", "Разные пики вдоль открытого берега")
                ],
            "ja": [("海岸", "千葉南・鴨川〜千倉"), ("ブレイク", "砂浜、河口、ときにリーフ"), ("うねり", "南〜南東"), ("オフショア", "西〜北西"), ("混雑", "開いた海岸に多様なピーク")],
            "spots": {
                "en": ["Wadaura", "Chikura"],
                "ru": ["Вадаура", "Тикура"],
                "ja": ["和田浦", "千倉"]
            },
        },
}

# Real-map geometry is separate from the illustrated overview map.  These
# coordinates are used only on the corresponding area page, where a visitor
# can pan and zoom around the actual coastline.
AREA_MAPS = {
    "asahi":
        {
            "center": (35.6920, 140.6840),
            "zoom": 13,
            "spots":
                [
                    {
                        "id": "mansionsita",
                        "coordinates": (35.695894, 140.722832),
                        "url": "mansionsita/index.html",
                        "en": "Mansionsita (マンション下)",
                        "ru": "Мансёнсита (マンション下)",
                        "ja": "マンション下",
                    },
                    {
                        "id": "shingosita",
                        "coordinates": (35.700724, 140.714960),
                        "url": "shingosita/index.html",
                        "en": "Shingosita (信号下)",
                        "ru": "Сингосита (信号下)",
                        "ja": "信号下",
                    },
                    {
                        "id": "shoppumae",
                        "coordinates": (35.700512, 140.710306),
                        "url": "shoppumae/index.html",
                        "en": "Shoppumae (ショップ前)",
                        "ru": "Сёппумаэ (ショップ前)",
                        "ja": "ショップ前",
                    },
                    {
                        "id": "kanpomae",
                        "coordinates": (35.684181, 140.646435),
                        "url": "kanpomae/index.html",
                        "en": "Kanpomae (かんぽ前)",
                        "ru": "Канпомаэ (かんぽ前)",
                        "ja": "かんぽ前",
                    },
                ],
        },
    "sosa":
        {
            "center": (35.6426, 140.5821),
            "zoom": 13,
            "spots":
                [
                    {
                        "id": "nodehama",
                        "coordinates": (35.651530, 140.595370),
                        "url": "nodehama/index.html",
                        "en": "Nodehama (野手浜)",
                        "ru": "Нодэхама (野手浜)",
                        "ja": "野手浜",
                    },
                    {
                        "id": "horikawa",
                        "coordinates": (35.633730, 140.568840),
                        "url": "horikawa/index.html",
                        "en": "Horikawa (堀川)",
                        "ru": "Хорикава (堀川)",
                        "ja": "堀川",
                    },
                ],
        },
    "sakuta":
        {
            "center": (35.5435, 140.4684),
            "zoom":
                14,
            "spots":
                [
                    {
                        "id": "sakuta",
                        "coordinates": (35.542910, 140.467347),
                        "url": "sakuta/index.html",
                        "en": "Sakuta (作田)",
                        "ru": "Сакута (作田)",
                        "ja": "作田",
                    },
                    {
                        "id": "motosuka",
                        "coordinates": (35.549469, 140.471828),
                        "url": "motosuka/index.html",
                        "en": "Motosuka (本須賀)",
                        "ru": "Мотоска (本須賀)",
                        "ja": "本須賀",
                    },
                ],
        },
    "ichinomiya":
        {
            "center": (35.3580, 140.3920),
            "zoom":
                13,
            "spots":
                [
                    {
                        "id": "ichinomiya",
                        "coordinates": (35.378079, 140.391159),
                        "url": "ichinomiya/index.html",
                        "en": "Ichinomiya (一宮)",
                        "ru": "Итиномия (一宮)",
                        "ja": "一宮",
                    },
                    {
                        "id": "taito",
                        "coordinates": (35.330102, 140.398330),
                        "url": "taito/index.html",
                        "en": "Taito (太東)",
                        "ru": "Тайто (太東)",
                        "ja": "太東",
                    },
                ],
        },
    "katsuura":
        {
            "center": (35.1800, 140.3550),
            "zoom":
                14,
            "spots":
                [
                    {
                        "id": "onjuku main",
                        "coordinates": (35.182143, 140.355927),
                        "url": "onjuku-main/index.html",
                        "en": "Onjuku main (御宿メイン)",
                        "ru": "Ондзюку мэйн (御宿メイン)",
                        "ja": "御宿メイン",
                    },
                    {
                        "id": "iwawada",
                        "coordinates": (35.181301, 140.363602),
                        "url": "iwawada/index.html",
                        "en": "Onjuku Iwawada (御宿 岩和田)",
                        "ru": "Ондзюку Ивавада (御宿 岩和田)",
                        "ja": "御宿 岩和田",
                    },
                ],
        },
    "south-boso":
        {
            "center": (35.0100, 139.9800),
            "zoom":
                12,
            "spots":
                [
                    {
                        "id": "wadaura",
                        "coordinates": (35.043500, 140.012500),
                        "url": "wadaura/index.html",
                        "en": "Wadaura (和田浦)",
                        "ru": "Вадаура (和田浦)",
                        "ja": "和田浦",
                    },
                    {
                        "id": "chikura",
                        "coordinates": (34.978000, 139.955000),
                        "url": "chikura/index.html",
                        "en": "Chikura (千倉)",
                        "ru": "Тикура (千倉)",
                        "ja": "千倉",
                    },
                ],
        },
}

# Individual spot map settings. The spot marker comes from AREA_MAPS above.
# Set "center" to override the initial map center; "amenities" maps an
# English amenity key to either one (latitude, longitude) coordinate or a list
# of coordinates. Map points are independent of the spot's amenities list;
# distant facilities can appear only on the map.
SPOT_MAPS = {
    "shingosita": {
        "zoom": 17,
        "amenities": {}
    },
    "mansionsita": {
        "zoom": 17,
        "amenities": {
            "restroom": (
                35.6929103,
                140.7279291,
            ),
        }
    },
    "shoppumae":
        {
            "zoom": 17,
            "amenities":
                {
                    "restroom": (35.7022824, 140.7102638),
                    "shower": (35.7022824, 140.7102638),
                    "parking": [
                        (35.702220, 140.709436),
                        (35.702392, 140.711008),
                    ],
                }
        },
    "kanpomae": {
        "zoom": 17,
        "amenities": {
            "restroom": (35.686327, 140.650206),
        }
    },
    "nodehama": {
        "zoom": 16,
        "amenities": {},
    },
    "horikawa": {
        "zoom": 16,
        "amenities": {},
    },
    "sakuta": {
        "zoom": 17,
        "amenities": {
            "restroom": (35.545743, 140.465409),
            "shower": (35.545743, 140.465409),
            "paid_parking": (35.545736, 140.466147),
        }
    },
    "motosuka":
        {
            "zoom": 17,
            "amenities":
                {
                    "restroom": (35.5502788, 140.4699726),
                    "shower": (35.550616, 140.469809),
                    "parking": [
                        (35.551446, 140.470238),
                        (35.550054, 140.469037),
                    ]
                }
        },
    "ichinomiya":
        {
            "zoom": 16,
            "amenities":
                {
                    "restroom": [(35.38116110826715, 140.3913171664306), (35.37803680615724, 140.39094934499892)],
                    "shower": [(35.38199651476501, 140.39136973475868), (35.376817758837646, 140.39107780349985)],
                    "paid_parking": [(35.38168787973108, 140.39115197247418), (35.3770039073883, 140.3910357475373)],
                }
        },
    "taito":
        {
            "zoom": 16,
            "amenities":
                {
                    "restroom": (35.329313247513866, 140.39997739631616),
                    "shower": (35.329313247513866, 140.39997739631616),
                    "parking": (35.32887358312741, 140.3995119850874),
                }
        },
    "onjuku main": {
        "zoom": 16,
        "amenities": {}
    },
    "iwawada": {
        "zoom": 16,
        "amenities": {}
    },
    "wadaura": {
        "zoom": 15,
        "amenities": {}
    },
    "chikura": {
        "zoom": 15,
        "amenities": {}
    },
}

# Tag labels are deliberately identical in every language.
TAGS = [
    "beginner",
    "intermediate",
    "advanced",
    "cold-water",
    "warm-water",
    "typhoon-swell",
    "board",
    "small-waves",
    "big-waves",
    "high-volume",
    "mid-length",
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
    # The Chiba artwork is deliberately rotated, so these are hand-placed
    # against its coastline rather than derived from geographic coordinates.
    "width": 1774,
    "height": 887,
    "area_labels":
        {
            # x/y sit just off the shore; rotation follows the local coast.
            # All labels use a right-aligned SVG anchor so their ends retain a
            # consistent small gap from the waterline in every language.
            "asahi": {
                "x": 1440,
                "y": 340,
                "rotation": 32,
                "skew": -11
            },
            "sosa": {
                "x": 1280,
                "y": 325,
                "rotation": 32,
                "skew": -11
            },
            "sakuta": {
                "x": 1120,
                "y": 380,
                "rotation": 32,
                "skew": -11
            },
            "ichinomiya": {
                "x": 980,
                "y": 500,
                "rotation": 32,
                "skew": -11
            },
            "katsuura": {
                "x": 820,
                "y": 690,
                "rotation": 32,
                "skew": -11
            },
            "south-boso": {
                "x": 530,
                "y": 680,
                "rotation": 32,
                "skew": -11
            },
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
    """Read the current area comparison data, ordered north to south."""
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


def load_spot_comparison():
    """Read the individual spots shown in the comparison table."""
    path = os.path.join(ROOT, "csv", "spot-comparison.csv")
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


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


def display_boards():
    """Boards shown in the Chiba gear guide, from longest to shortest."""
    return [row for row in reversed(load_boards()) if row["id"] != "gun"]


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
# The whole multilingual scheme rests on one naming convention:
#     page.html   <->  page_ru.html  <->  page_ja.html
# Nothing else in the site records which language a page is in.
# --------------------------------------------------------------------------

RU_SUFFIX = "_ru.html"
JA_SUFFIX = "_ja.html"


def lang_of(page_file):
    """Language encoded in a page filename; English has no suffix."""
    name = os.path.basename(page_file)
    if name.endswith(RU_SUFFIX):
        return "ru"
    if name.endswith(JA_SUFFIX):
        return "ja"
    return "en"


def local_name(page_file, lang):
    """File name of the same page in a requested language."""
    name = os.path.basename(page_file)
    for suffix in (RU_SUFFIX, JA_SUFFIX):
        if name.endswith(suffix):
            name = name[:-len(suffix)] + ".html"
            break
    return localize(name, lang)


def base_url(page_file):
    """Relative path from the page being rendered up to the site root.

    Returns '' for a page in the root and '../../' for spots/<area>/index.html,
    so templates can link without ever hard-coding an absolute path.
    """
    rel = os.path.relpath(ROOT, os.path.dirname(os.path.abspath(page_file)))
    return "" if rel == "." else rel.replace(os.sep, "/") + "/"


def localize(name, lang):
    """Apply the naming convention to a root-relative link."""
    if lang == "ru":
        return name[:-len(".html")] + RU_SUFFIX
    if lang == "ja":
        return name[:-len(".html")] + JA_SUFFIX
    return name


def page_count_label(count, lang):
    """Return the correctly inflected word for a section page count."""
    if lang == "en":
        return "page" if count == 1 else "pages"
    if lang == "ja":
        return "ページ"
    last_two = count % 100
    last = count % 10
    if 11 <= last_two <= 14:
        return "страниц"
    if last == 1:
        return "страница"
    if 2 <= last <= 4:
        return "страницы"
    return "страниц"


def nav_items(page_file):
    """Navigation entries for the language the current page is written in.

    Navigation never switches language: only the flag link does that.
    """
    lang = lang_of(page_file)
    b = base_url(page_file)
    u = UI[lang]
    items = []
    for name in SECTIONS:
        items.append((b + localize(f"{name}/index.html", lang), SECTION_META[name][lang]["title"]))
    glossary_source = os.path.join(ROOT, localize("glossary/index.html", lang))
    if os.path.exists(glossary_source):
        items.append((b + localize("glossary/index.html", lang), u["nav_glossary"]))
    items += [
        (b + localize("tags/index.html", lang), u["nav_tags"]),
        (b + localize("about.html", lang), u["nav_how"]),
    ]
    return items


def section_url(name, page_file):
    """Link from the current page to a section's index page."""
    lang = lang_of(page_file)
    return base_url(page_file) + localize(f"{name}/index.html", lang)
