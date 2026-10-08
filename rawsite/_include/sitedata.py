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
            "map_caption": "Illustrated map of surf areas in Chiba and Shonan.",
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
            "map_caption": "Иллюстрированная карта районов для сёрфинга в Тибе и Сёнане.",
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
            "map_caption": "千葉と湘南のサーフィンエリアを示す図解地図",
            "table_spot": "スポット",
            "table_region": "エリア",
            "table_break": "ブレイク",
            "table_level": "レベル",
            "table_season": "ベストシーズン",
            "table_swell": "対応するうねり",
            "table_wind": "最適風向",
            "table_size": "一般的なサイズ",
            "table_aug": "水温・8月",
            "table_feb": "水温・2月",
            "table_sort_hint": "列の見出しをクリックすると並べ替えられます。",
            "facts_heading": "ポイント概要",
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
}

# The comparison presents those same six navigation areas. Keeping one source
# of names prevents the map and the table from drifting apart again.
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
    "fujisawa":
        {
            "image": "fujisawa",
            "region": {
                "en": "Kanagawa · Shonan",
                "ru": "Канагава · Сёнан",
                "ja": "神奈川・湘南"
            },
            "summary":
                {
                    "en": "Kugenuma is Shonan’s social beach break: forgiving sandbanks, south swell, surf schools and one of Japan’s liveliest line-ups.",
                    "ru": "Кугэнума — социальный бич-брейк Сёнана: дружелюбные песчаные банки, южный свелл, школы и один из самых оживлённых лайн-апов Японии.",
                    "ja": "鵠沼は湘南らしい社交的なビーチブレイク。乗りやすいサンドバー、南うねり、スクールがそろい、日本でも特ににぎやかなラインナップの一つです。",
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
}

# Detailed spot pages live inside their parent area.  These deliberately keep
# their compact facts separate from csv/spots.csv, which compares the six
# navigation areas rather than every individual break.
SPOT_DETAILS = {
    "shingosita":
        {
            "area": "asahi",
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
                {
                    "en":
                        [
                            ("Area", "Chiba North · Iioka"),
                            ("Break", "hollow beach break"),
                            ("Bottom", "Sand"),
                            ("Level", "beginner to advanced, depending on conditions"),
                            ("Season", "year-round; especially autumn–winter"),
                            ("Best size", "chest to shoulder high"),
                            ("Working tide", "mid to mid-low"),
                            ("Best swell", "S–SE"),
                            ("Clean wind", "N"),
                            ("Best board", "shortboard"),
                        ],
                    "ru":
                        [
                            ("Район", "Северная Тиба · Ииока"),
                            ("Брейк", "холлоу-бич-брейк"),
                            ("Дно", "Песчаное"),
                            ("Уровень", "от начинающего до продвинутого — по условиям"),
                            ("Сезон", "круглый год; особенно осень — зима"),
                            ("Лучший размер", "по грудь — по плечи"),
                            ("Подходящий уровень воды", "средний — средне-низкий"),
                            ("Лучший свелл", "Ю–ЮВ"),
                            ("Чистый ветер", "С"),
                            ("Подходящая доска", "шортборд"),
                        ],
                    "ja":
                        [
                            ("エリア", "千葉北・飯岡"),
                            ("ブレイク", "ホローなビーチブレイク"),
                            ("海底", "砂地"),
                            ("レベル", "初級〜上級（コンディション次第）"),
                            ("シーズン", "通年、特に秋〜冬"),
                            ("ベストサイズ", "ムネ〜カタ"),
                            ("対応する潮位", "ミドル〜ミドルロー"),
                            ("ベストうねり", "南〜南東"),
                            ("オフショア", "北"),
                            ("向くボード", "ショートボード"),
                        ],
                },
        },
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
                {
                    "en":
                        [
                            ("Area", "Chiba North · Iioka"),
                            ("Break", "beach break between tetrapods"),
                            ("Bottom", "Sand"),
                            ("Min. Level", "beginner"),
                            ("Working tide", "low to high"),
                            ("Swell", "E–SSW, especially south"),
                            ("Clean wind", "N–NNE"),
                            ("Best board", "longboard"),
                        ],
                    "ru":
                        [
                            ("Район", "Северная Тиба · Ииока"),
                            ("Брейк", "бич-брейк между тетраподами"),
                            ("Дно", "Песчаное"),
                            ("Мин. Уровень", "начинающий"),
                            ("Подходящий уровень воды", "от низкого до высокого"),
                            ("Свелл", "В–ЮЮЗ, особенно южный"),
                            ("Чистый ветер", "С–ССВ"),
                            ("Подходящая доска", "лонгборд"),
                        ],
                    "ja":
                        [
                            ("エリア", "千葉北・飯岡"),
                            ("ブレイク", "テトラポッドの間のビーチブレイク"),
                            ("海底", "砂地"),
                            ("レベル", "初級者以上"),
                            ("対応する潮位", "ロー〜ハイ"),
                            ("うねり", "東〜南南西、特に南うねり"),
                            ("オフショア", "北〜北北東"),
                            ("向くボード", "ロングボード"),
                        ],
                },
        },
    "shoppumae":
        {
            "area": "asahi",
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
            "amenities":
                {
                    "en": [("Free parking", "parking-free-engraved-v1.png"), ("Shower", "shower-engraved-v1.png"), ("Restroom", "toilet-engraved-v1.png")],
                    "ru": [("Бесплатная парковка", "parking-free-engraved-v1.png"), ("Душ", "shower-engraved-v1.png"), ("Туалет", "toilet-engraved-v1.png")],
                    "ja": [("無料駐車場", "parking-free-engraved-v1.png"), ("シャワー", "shower-engraved-v1.png"), ("トイレ", "toilet-engraved-v1.png")],
                },
            "facts":
                {
                    "en":
                        [
                            ("Area", "Chiba North · Iioka"),
                            ("Break", "beach break between tetrapods"),
                            ("Bottom", "Sand"),
                            ("Min. Level", "intermediate"),
                            ("Working tide", "medium to high"),
                            ("Swell", "NE–SSW, especially south"),
                            ("Clean wind", "NNW-W"),
                            ("Best board", "shortboard"),
                        ],
                    "ru":
                        [
                            ("Район", "Северная Тиба · Ииока"),
                            ("Брейк", "бич-брейк между тетраподами"),
                            ("Дно", "Песчаное"),
                            ("Мин. Уровень", "средний"),
                            ("Подходящий уровень воды", "от среднего до высокого"),
                            ("Свелл", "СВ–ЮЮЗ, особенно южный"),
                            ("Чистый ветер", "ССЗ–З"),
                            ("Подходящая доска", "шортборд"),
                        ],
                    "ja":
                        [
                            ("エリア", "千葉北・飯岡"),
                            ("ブレイク", "テトラポッドの間のビーチブレイク"),
                            ("海底", "砂地"),
                            ("レベル", "中級者以上"),
                            ("対応する潮位", "中〜高"),
                            ("うねり", "北東〜南南西、特に南うねり"),
                            ("オフショア", "北北西〜西"),
                            ("向くボード", "ショートボード"),
                        ],
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
                "en": ["Mansionsita"],
                "ru": ["Мэнсионсита"],
                "ja": ["マンション下"]
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
                "en": ["Kanpomae"],
                "ru": ["Канпомаэ"],
                "ja": ["かんぽ前"]
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
}

# Real-map geometry is separate from the illustrated overview map.  These
# coordinates are used only on the corresponding area page, where a visitor
# can pan and zoom around the actual coastline.
AREA_MAPS = {
    "asahi":
        {
            "center": (35.6991, 140.7173),
            "zoom":
                15,
            "spots":
                [
                    {
                        "id": "shingosita",
                        "coordinates": (35.700525, 140.713401),
                        "url": "shingosita/index.html",
                        "en": "Shingosita (信号下)",
                        "ru": "Сингосита (信号下)",
                        "ja": "信号下",
                    },
                    {
                        "id": "mansionsita",
                        "coordinates": (35.697362, 140.721728),
                        "url": "mansionsita/index.html",
                        "en": "Mansionsita (マンション下)",
                        "ru": "Мансёнсита (マンション下)",
                        "ja": "マンション下",
                    },
                    {
                        "id": "shoppumae",
                        "coordinates": (35.700512, 140.710306),
                        "url": "shoppumae/index.html",
                        "en": "Shoppumae (ショップ前)",
                        "ru": "Сёппумаэ (ショップ前)",
                        "ja": "ショップ前",
                    },
                ],
        },
    "sosa":
        {
            "center": (35.6814, 140.6520),
            "zoom": 14,
            "spots": [{
                "id": "kanpomae",
                "coordinates": (35.684181, 140.646435),
                "en": "Kanpomae",
                "ru": "Канпомаэ",
                "ja": "かんぽ前",
            }, ],
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
                        "en": "Sakuta (作田)",
                        "ru": "Сакута (作田)",
                        "ja": "作田",
                    },
                    {
                        "id": "motosuka",
                        "coordinates": (35.549469, 140.471828),
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
                        "en": "Ichinomiya (一宮)",
                        "ru": "Итиномия (一宮)",
                        "ja": "一宮",
                    },
                    {
                        "id": "taito",
                        "coordinates": (35.330102, 140.398330),
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
                        "en": "Onjuku main (御宿メイン)",
                        "ru": "Ондзюку мэйн (御宿メイン)",
                        "ja": "御宿メイン",
                    },
                    {
                        "id": "iwawada",
                        "coordinates": (35.181301, 140.363602),
                        "en": "Onjuku Iwawada (御宿 岩和田)",
                        "ru": "Ондзюку Ивавада (御宿 岩和田)",
                        "ja": "御宿 岩和田",
                    },
                ],
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
            "fujisawa": {
                "x": 300,
                "y": 255,
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
    items = [(b + localize("index.html", lang), u["nav_home"])]
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
