"""Single source for individual surf spots, in area/map display order.

Add one SPOTS entry and three small language page wrappers to publish a spot.
The key is also its URL slug (spaces become hyphens). Every record needs area and
title; a detailed page also needs coordinates, summary and description. Translated text uses en/ru/ja keys.
Optional fields: facts (localized label/value pairs), swell/wind (clockwise
compass ranges), comparison values, amenities (card icons), map (zoom/center
and amenity coordinates), bluesky. Missing conditions are shown as unknown;
missing map settings use the spot coordinates and zoom 16.
"""

SPOTS = {
    "mansionsita":
        {
            "area": "asahi",
            "title": {
                "en": "Mansionsita",
                "ru": "Мансёнсита",
                "ja": "マンション下"
            },
            "coordinates": [35.695894, 140.722832],
            "summary":
                {
                    "en": "A smaller, gentler beach break between the tetrapods on Iioka’s north-east side.",
                    "ru": "Более мягкий и обычно меньший бич-брейк между тетраподами в северо-восточной части Ииоки.",
                    "ja": "飯岡の北東側、テトラポッドの間で割れる、比較的サイズが小さく穏やかなビーチブレイク。",
                },
            "description":
                {
                    "en":
                        "Mansionsita is often softer than the breaks farther south in Asahi, so longer boards tend to be the natural choice. The sandbanks shift regularly, but when they line up, rides of up to 100 metres are possible. In the north-east corner, a pocket known as ‘Silver’ sits behind the first line of tetrapods and produces small, smooth, forgiving waves, so it often draws many beginners.  Its name is linked to the Japanese term used for older people. The spot can get crowded on weekends.",
                    "ru":
                        "В Мансёнсите волны часто мягче, чем на спотах южнее в районе Асахи, поэтому здесь естественно выбирать более длинные доски. Рельеф дна регулярно меняется, но иногда при благоприятных условиях возможны длинные проезды протяжённостью до 100 м. Северо-восточный угол закрытый первой грядой тетраподов, называемый «Сильвер», даёт ровные, небольшие и мягкие волны, поэтому часто собирает много начинающих серферов. Название «Сильвер» происходит от японского прилагательного, обозначающего принадлежность к людям старшего возраста. В выходные спот бывает многолюден.",
                    "ja":
                        "マンション下は、旭エリアで南にあるポイントよりも波が柔らかいことが多く、長めのボードが自然に合います。海底地形は頻繁に変わりますが、条件が整えば100メートルほどのロングライドができることもあります。北東側の最初のテトラポッド列に守られた一角は「シルバー」と呼ばれ、小さく整った穏やかな波が立つため、初心者が多く集まります。「シルバー」という名前は、高齢者を指す言葉とのつながりに由来しています。週末は混雑することがあります。",
                },
            "facts":
                {
                    "en":
                        [
                            ["Area", "Chiba North · Iioka"],
                            ["Break", "beach break between tetrapods"],
                            ["Bottom", "Sand"],
                            ["Min. Level", "beginner"],
                            ["Working tide", "low to high"],
                            ["Best board", "longboard"],
                        ],
                    "ru":
                        [
                            ["Район", "Северная Тиба · Ииока"],
                            ["Брейк", "бич-брейк между тетраподами"],
                            ["Дно", "Песчаное"],
                            ["Мин. уровень", "начинающий"],
                            ["Подходящий уровень воды", "от низкого до высокого"],
                            ["Подходящая доска", "лонгборд"],
                        ],
                    "ja": [
                        ["エリア", "千葉北・飯岡"],
                        ["ブレイク", "テトラポッドの間のビーチブレイク"],
                        ["海底", "砂地"],
                        ["レベル", "初級者以上"],
                        ["対応する潮位", "ロー〜ハイ"],
                        ["向くボード", "ロングボード"],
                    ],
                },
            "region": "chiba-north",
            "break_type": "beach",
            "size_ft_typical": "1-3",
            "water_aug_c": 26,
            "water_feb_c": 14,
            "swell": "E-SW",
            "wind": "N-ENE",
            "amenities": [],
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3mypagtfack22",
                "hours": 72
            },
            "map": {
                "zoom": 17,
                "amenities": {
                    "restroom": [35.6929103, 140.7279291]
                }
            },
        },
    "shingosita":
        {
            "area": "asahi",
            "title": {
                "en": "Shingosita",
                "ru": "Сингосита",
                "ja": "信号下"
            },
            "coordinates": [35.700724, 140.71496],
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
                            ["Area", "Chiba North · Iioka"],
                            ["Break", "hollow beach break"],
                            ["Bottom", "Sand"],
                            ["Level", "beginner to advanced, depending on conditions"],
                            ["Season", "year-round; especially autumn–winter"],
                            ["Best size", "chest to shoulder high"],
                            ["Working tide", "mid to mid-low"],
                            ["Best board", "longboard, funboard, shortboard"],
                        ],
                    "ru":
                        [
                            ["Район", "Северная Тиба · Ииока"],
                            ["Брейк", "холлоу-бич-брейк"],
                            ["Дно", "Песчаное"],
                            ["Уровень", "от начинающего до продвинутого — по условиям"],
                            ["Сезон", "круглый год; особенно осень — зима"],
                            ["Лучший размер", "по грудь — по плечи"],
                            ["Подходящий уровень воды", "средний — средне-низкий"],
                            ["Подходящая доска", "лонгборд, фанборд, шортборд"],
                        ],
                    "ja":
                        [
                            ["エリア", "千葉北・飯岡"],
                            ["ブレイク", "ホローなビーチブレイク"],
                            ["海底", "砂地"],
                            ["レベル", "初級〜上級（コンディション次第）"],
                            ["シーズン", "通年、特に秋〜冬"],
                            ["ベストサイズ", "ムネ〜カタ"],
                            ["対応する潮位", "ミドル〜ミドルロー"],
                            ["向くボード", "ロングボード、ファンボード、ショートボード"],
                        ],
                },
            "region": "chiba-north",
            "break_type": "beach",
            "size_ft_typical": "3-5",
            "water_aug_c": 26,
            "water_feb_c": 14,
            "swell": "ESE-SSW",
            "wind": "NNW-NE",
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3mypdpqpjrc25",
                "hours": 72
            },
            "map": {
                "zoom": 17,
                "amenities": {}
            },
        },
    "shoppumae":
        {
            "area": "asahi",
            "title": {
                "en": "Shoppumae",
                "ru": "Сёппумаэ",
                "ja": "ショップ前"
            },
            "coordinates": [35.700512, 140.710306],
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
            "facts":
                {
                    "en":
                        [
                            ["Area", "Chiba North · Iioka"],
                            ["Break", "beach break between tetrapods"],
                            ["Bottom", "Sand"],
                            ["Min. Level", "intermediate"],
                            ["Working tide", "medium to high"],
                            ["Best board", "shortboard, funboard"],
                        ],
                    "ru":
                        [
                            ["Район", "Северная Тиба · Ииока"],
                            ["Брейк", "бич-брейк между тетраподами"],
                            ["Дно", "Песчаное"],
                            ["Мин. уровень", "средний"],
                            ["Подходящий уровень воды", "от среднего до высокого"],
                            ["Подходящая доска", "шортборд, фанборд"],
                        ],
                    "ja": [
                        ["エリア", "千葉北・飯岡"],
                        ["ブレイク", "テトラポッドの間のビーチブレイク"],
                        ["海底", "砂地"],
                        ["レベル", "中級者以上"],
                        ["対応する潮位", "中〜高"],
                        ["向くボード", "ショートボード、ファンボード"],
                    ],
                },
            "region": "chiba-north",
            "break_type": "beach",
            "size_ft_typical": "3-5",
            "water_aug_c": 26,
            "water_feb_c": 14,
            "swell": "ESE-SSW",
            "wind": "NNW-NE",
            "amenities": ["parking", "shower", "restroom"],
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3myrp3co3x22b",
                "hours": 72
            },
            "map":
                {
                    "zoom": 17,
                    "amenities":
                        {
                            "restroom": [35.7022824, 140.7102638],
                            "shower": [35.7022824, 140.7102638],
                            "parking": [[35.70222, 140.709436], [35.702392, 140.711008]],
                        },
                },
        },
    "kanpomae":
        {
            "area": "asahi",
            "title": {
                "en": "Kanpomae",
                "ru": "Канпомаэ",
                "ja": "かんぽ前"
            },
            "coordinates": [35.684181, 140.646435],
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
            "facts":
                {
                    "en":
                        [
                            ["Area", "Chiba North · Asahi"],
                            ["Break", "shallow beach break"],
                            ["Bottom", "Sand"],
                            ["Level", "beginner to advanced, depending on conditions"],
                            ["Season", "autumn–winter"],
                            ["Best size", "waist to chest high"],
                            ["Best board", "longboard, funboard, shortboard"],
                        ],
                    "ru":
                        [
                            ["Район", "Северная Тиба · Асахи"],
                            ["Брейк", "пологий бич-брейк"],
                            ["Дно", "Песчаное"],
                            ["Уровень", "от начинающего до продвинутого — по условиям"],
                            ["Сезон", "осень — зима"],
                            ["Лучший размер", "по пояс — по грудь"],
                            ["Подходящая доска", "лонгборд, фанборд, шортборд"],
                        ],
                    "ja":
                        [
                            ["エリア", "千葉北・旭"],
                            ["ブレイク", "遠浅のビーチブレイク"],
                            ["海底", "砂地"],
                            ["レベル", "初級〜上級（コンディション次第）"],
                            ["シーズン", "秋〜冬"],
                            ["ベストサイズ", "コシ〜ムネ"],
                            ["向くボード", "ロングボード、ファンボード、ショートボード"],
                        ],
                },
            "region": "chiba-north",
            "break_type": "beach",
            "size_ft_typical": "2-4",
            "water_aug_c": 26,
            "water_feb_c": 14,
            "swell": "ENE-SSW",
            "wind": "WNW-N",
            "amenities": ["parking", "restroom"],
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3myrpj5thns2i",
                "hours": 72
            },
            "map": {
                "zoom": 17,
                "amenities": {
                    "restroom": [35.686327, 140.650206]
                }
            },
        },
    "nodehama":
        {
            "area": "sosa",
            "title": {
                "en": "Nodehama",
                "ru": "Нодэхама",
                "ja": "野手浜"
            },
            "coordinates": [35.65153, 140.59537],
            "summary":
                {
                    "en": "A mellow, shallow beach break in Sosa that stays surfable on smaller south-east swell.",
                    "ru": "Мягкий пологий бич-брейк в Сосе, где можно кататься и при небольшом юго-восточном свелле.",
                    "ja": "南東うねりの小波の日でもサーフしやすい、匝瑳の遠浅なビーチブレイク。",
                },
            "description":
                {
                    "en":
                        "Nodehama is an open sandy beach facing south-east. It responds to swell from north-east through south-south-west and often has manageable waves even on smaller days. The gently sloping seabed makes the wave soft, with shoulders that do not always stand up strongly, so it is a relaxed option for beginners and longboards. Waist- to chest-high surf is the usual sweet spot; when the waves rise above head high, the peaks can become wide and close out. Check the banks and current before paddling out, and give other surfers room in the line-up.",
                    "ru":
                        "Нодэхама — открытый песчаный пляж, обращённый на юго-восток. Он принимает свелл от северо-востока до юго-юго-запада и часто даёт управляемые волны даже в небольшой день. Пологий рельеф дна делает волну мягкой, а плечо не всегда встаёт круто, поэтому место подходит начинающим и лонгбордам. Лучшее окно обычно от пояса до груди; при размере выше головы пики становятся широкими и чаще закрываются. Перед выходом проверьте банки и течение и оставляйте другим место в лайн-апе.",
                    "ja":
                        "野手浜は南東に開いた砂浜です。北東〜南南西のうねりに反応し、小波の日でも楽しみやすいポイントです。遠浅の地形で波は厚め、ショルダーも張りにくいため、初級者やロングボードにも向きます。コシ〜ムネ程度が狙い目で、頭を超えるとピークはワイドになりクローズアウトが増えます。入水前にバンクとカレントを確認し、ラインナップでは周囲にスペースを譲りましょう。",
                },
            "facts":
                {
                    "en":
                        [
                            ["Area", "Chiba North · Sosa"],
                            ["Break", "shallow beach break"],
                            ["Bottom", "Sand"],
                            ["Level", "beginner to advanced, depending on conditions"],
                            ["Best size", "waist to chest high"],
                            ["Best board", "longboard, funboard, shortboard"],
                        ],
                    "ru":
                        [
                            ["Район", "Северная Тиба · Соса"],
                            ["Брейк", "пологий бич-брейк"],
                            ["Дно", "Песчаное"],
                            ["Уровень", "от начинающего до продвинутого — по условиям"],
                            ["Лучший размер", "по пояс — по грудь"],
                            ["Подходящая доска", "лонгборд, фанборд, шортборд"],
                        ],
                    "ja":
                        [
                            ["エリア", "千葉北・匝瑳"],
                            ["ブレイク", "遠浅のビーチブレイク"],
                            ["海底", "砂地"],
                            ["レベル", "初級〜上級（コンディション次第）"],
                            ["ベストサイズ", "コシ〜ムネ"],
                            ["向くボード", "ロングボード、ファンボード、ショートボード"],
                        ],
                },
            "region": "chiba-north",
            "break_type": "beach",
            "size_ft_typical": "1-4",
            "water_aug_c": 26,
            "water_feb_c": 14,
            "swell": "NE-SSW",
            "wind": "WNW-N",
            "amenities": [],
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3myrqsyhvbs2i",
                "hours": 72
            },
            "map": {
                "zoom": 16
            },
        },
    "horikawa":
        {
            "area": "sosa",
            "title": {
                "en": "Horikawa",
                "ru": "Хорикава",
                "ja": "堀川"
            },
            "coordinates": [35.63373, 140.56884],
            "summary":
                {
                    "en": "A mellow, shallow beach break in southern Sosa that works well on smaller south-east swell.",
                    "ru": "Мягкий пологий бич-брейк на юге Сосы, хорошо работающий при небольшом юго-восточном свелле.",
                    "ja": "南東うねりの小波の日でも楽しみやすい、匝瑳南部の遠浅なビーチブレイク。",
                },
            "description":
                {
                    "en":
                        "Horikawa (also called Horikawahama) is an open sandy beach facing south-east. It responds to swell from north-east through south-south-west and can offer a gentle, manageable wave when other nearby breaks are small. The seabed shelves gradually, so the wave is usually soft rather than steep and is friendly to beginners and longer boards. Waist- to chest-high surf is generally the most enjoyable; above head high, peaks tend to become wider and close out more often. Conditions can change along this open coast, so check the banks and current before entering.",
                    "ru":
                        "Хорикава, также известная как Хорикавахама, — открытый песчаный пляж, обращённый на юго-восток. Он принимает свелл от северо-востока до юго-юго-запада и может давать мягкую, управляемую волну, когда соседние брейки малы. Дно понижается плавно, поэтому волна обычно не крутая и подходит начинающим и более длинным доскам. Лучше всего обычно от пояса до груди; при размере выше головы пики расширяются и чаще закрываются. На этом открытом берегу условия быстро меняются, поэтому перед входом проверьте банки и течение.",
                    "ja":
                        "堀川（堀川浜とも呼ばれます）は南東に開いた砂浜です。北東〜南南西のうねりに反応し、周辺が小さい日にも厚く扱いやすい波が期待できます。海底は遠浅で、波は急というより穏やかになりやすく、初級者や長めのボードにも向きます。コシ〜ムネ程度が楽しみやすく、頭を超えるとピークはワイドになりクローズアウトが増えます。開けた海岸なので、入水前にバンクとカレントを確認しましょう。",
                },
            "facts":
                {
                    "en":
                        [
                            ["Area", "Chiba North · Sosa"],
                            ["Break", "shallow beach break"],
                            ["Bottom", "Sand"],
                            ["Level", "beginner to advanced, depending on conditions"],
                            ["Best size", "waist to chest high"],
                            ["Best board", "longboard, funboard, shortboard"],
                        ],
                    "ru":
                        [
                            ["Район", "Северная Тиба · Соса"],
                            ["Брейк", "пологий бич-брейк"],
                            ["Дно", "Песчаное"],
                            ["Уровень", "от начинающего до продвинутого — по условиям"],
                            ["Лучший размер", "по пояс — по грудь"],
                            ["Подходящая доска", "лонгборд, фанборд, шортборд"],
                        ],
                    "ja":
                        [
                            ["エリア", "千葉北・匝瑳"],
                            ["ブレイク", "遠浅のビーチブレイク"],
                            ["海底", "砂地"],
                            ["レベル", "初級〜上級（コンディション次第）"],
                            ["ベストサイズ", "コシ〜ムネ"],
                            ["向くボード", "ロングボード、ファンボード、ショートボード"],
                        ],
                },
            "region": "chiba-north",
            "break_type": "beach",
            "size_ft_typical": "1-4",
            "water_aug_c": 26,
            "water_feb_c": 14,
            "swell": "NE-SSW",
            "wind": "WNW-N",
            "amenities": ["parking", "shower", "restroom"],
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3myrqvjxsfs2i",
                "hours": 72
            },
            "map":
                {
                    "zoom": 16,
                    "amenities":
                        {
                            "restroom": [35.63544448765501, 140.56805614571354],
                            "shower": [35.63544448765501, 140.56805614571354],
                            "parking": [35.63558078986152, 140.56813542541934],
                        },
                },
        },
    "motosuka":
        {
            "area": "sakuta",
            "title": {
                "en": "Motosuka",
                "ru": "Мотоска",
                "ja": "本須賀"
            },
            "coordinates": [35.549469, 140.471828],
            "summary":
                {
                    "en": "A quiet, open section of Kujukuri with evenly spaced sandy peaks and room to practise away from the busier breaks.",
                    "ru": "Спокойный открытый участок Кудзюкури с ровно распределёнными песчаными пиками и местом для практики вдали от самых людных брейков.",
                    "ja": "砂のピークが均等に並ぶ、九十九里の静かで開けた区間。混むポイントから離れて練習する余地があります。",
                },
            "description":
                {
                    "en":
                        "Motosuka is an open sandy section of the Kujukuri coast with few fixed landmarks, so the best take-off moves with the banks and tide. North-east to east swell reaches the beach directly and usually produces smaller, manageable waves outside larger systems. There are no wind protection in the form of breakwaters, so crosshore winds can ruin the surface.",
                    "ru":
                        "Мотоска — открытый песчаный участок Кудзюкури почти без постоянных ориентиров, поэтому лучший тейк-офф перемещается вместе с банками и приливом. Свелл с северо-востока и востока приходит сюда напрямую и вне крупных свеллов обычно даёт небольшие волны.  Нет защиты от ветра в виде молов, поэтому боковой ветер может испортить поверхность.",
                    "ja":
                        "本須賀は、固定された目印が少ない九十九里の開けた砂浜です。良いテイクオフはバンクと潮位に合わせて動きます。北東〜東うねりが直接入り、大きなうねりがない日は扱いやすい小さめの波になりやすい場所です。防波堤のような風よけがないため、風の影響を受けやすいです。",
                },
            "facts":
                {
                    "en":
                        [
                            ["Area", "Chiba North · Sakuta"],
                            ["Break", "open beach break"],
                            ["Bottom", "Sand"],
                            ["Level", "beginner to intermediate"],
                            ["Crowds", "Usually quieter than nearby spots"],
                            ["Best board", "shortboard, funboard, longboard"],
                        ],
                    "ru":
                        [
                            ["Район", "Северная Тиба · Сакута"],
                            ["Брейк", "открытый бич-брейк"],
                            ["Дно", "Песчаное"],
                            ["Уровень", "начинающий — средний"],
                            ["Люди", "Обычно спокойнее, чем на ближайших спотах"],
                            ["Подходящая доска", "шортборд, фанборд, лонгборд"],
                        ],
                    "ja":
                        [
                            ["エリア", "千葉北・作田"],
                            ["ブレイク", "開けたビーチブレイク"],
                            ["海底", "砂地"],
                            ["レベル", "初級〜中級"],
                            ["混雑", "普段は近くのスポットより比較的落ち着いている"],
                            ["向くボード", "ショートボード、ファンボード、ロングボード"],
                        ],
                },
            "region": "chiba-north",
            "break_type": "beach",
            "size_ft_typical": "1-3",
            "water_aug_c": 26,
            "water_feb_c": 14,
            "swell": "NE-S",
            "wind": "WSW-NW",
            "amenities": ["parking", "shower", "restroom"],
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3mywskdtams2r",
                "hours": 72
            },
            "map":
                {
                    "zoom": 17,
                    "amenities":
                        {
                            "restroom": [35.5502788, 140.4699726],
                            "shower": [35.550616, 140.469809],
                            "parking": [[35.551446, 140.470238], [35.550054, 140.469037]],
                        },
                },
        },
    "sakuta":
        {
            "area": "sakuta",
            "title": {
                "en": "Sakuta",
                "ru": "Сакута",
                "ja": "作田"
            },
            "coordinates": [35.54291, 140.467347],
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
            "facts":
                {
                    "en":
                        [
                            ["Area", "Chiba North · Kujukuri"],
                            ["Break", "wide beach break"],
                            ["Bottom", "Sand"],
                            ["Level", "beginner to advanced, depending on conditions"],
                            ["Crowds", "Popular, with room to choose a peak"],
                            ["Best board", "shortboard, funboard, longboard"],
                        ],
                    "ru":
                        [
                            ["Район", "Северная Тиба · Кудзюкури"],
                            ["Брейк", "широкий бич-брейк"],
                            ["Дно", "Песчаное"],
                            ["Уровень", "от начинающего до продвинутого — по условиям"],
                            ["Люди", "Популярно, но можно выбрать пик"],
                            ["Подходящая доска", "шортборд, фанборд, лонгборд"],
                        ],
                    "ja":
                        [
                            ["エリア", "千葉北・九十九里"],
                            ["ブレイク", "広いビーチブレイク"],
                            ["海底", "砂地"],
                            ["レベル", "初級〜上級（コンディション次第）"],
                            ["混雑", "人気はあるがピークを選べる"],
                            ["向くボード", "ショートボード、ファンボード、ロングボード"],
                        ],
                },
            "region": "chiba-north",
            "break_type": "beach",
            "size_ft_typical": "2-4",
            "water_aug_c": 26,
            "water_feb_c": 14,
            "swell": "NE-S",
            "wind": "WSW-NW",
            "amenities": ["paid_parking", "shower", "restroom"],
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3mywsoky35s2r",
                "hours": 72
            },
            "map":
                {
                    "zoom": 17,
                    "amenities": {
                        "restroom": [35.545743, 140.465409],
                        "shower": [35.545743, 140.465409],
                        "paid_parking": [35.545736, 140.466147],
                    },
                },
        },
    "katagai-gyokou":
        {
            "area": "sakuta",
            "title": {
                "en": "Katagai Gyokou",
                "ru": "Катагай-гёко",
                "ja": "片貝漁港"
            },
            "coordinates": [35.534475, 140.461475],
            "summary":
                {
                    "en": "A sheltered, gently shelving longboard break between two long breakwaters.",
                    "ru": "Защищённый пологий бич-брейк между двумя длинными молами, ориентированный прежде всего на лонгборд.",
                    "ja": "二本の長い堤防に挟まれた、遠浅でロングボード向きのビーチブレイク。",
                },
            "description":
                {
                    "en":
                        "\n                        <p>This stretch of sandy beach sits between two long moles, helping to keep its gently shelving bottom more even than at exposed spots. When the swell arrives at an angle from the north or south, it can produce long, mellow waves. A straight easterly swell often produces wide, fast-closing waves and closeouts.</p>\n                        <p>The moles also provide shelter from cross-shore winds, so the surface often stays cleaner than at nearby exposed breaks. Katagai Gyokou is primarily a longboard spot, though it can also suit beginners when the waves are small.</p>\n                        <p>The main drawback is the distance from the designated parking area. Driving into or parking inside the fishing port is prohibited; use the car park on the Katagai Shintei side.</p>\n                        ",
                    "ru":
                        "\n                        <p>Этот участок песчаного пляжа расположен между двумя длинными молами, благодаря чему пологое дно здесь обычно остаётся более равномерным, чем на открытых спотах. При свелле, приходящем под углом с севера или юга, могут образовываться мягкие длинные волны. Прямой восточный свелл часто формирует широкие, быстро закрывающиеся волны и клоуз-ауты.</p>\n                        <p>Молы защищают спот от бокового ветра, поэтому поверхность здесь нередко остаётся чище, чем на соседних открытых участках. Катагай-гёко подходит прежде всего для лонгборда, а при небольших волнах — и для начинающих.</p>\n                        <p>Главный минус спота — удалённость от разрешённой парковки. Въезд и парковка на территории рыболовного порта запрещены: машину следует оставлять на парковке со стороны Катагай-Синтэй.</p>\n                        ",
                    "ja":
                        "\n                        <p>北側と南側の長い堤防に挟まれた砂浜で、開けたポイントに比べ、遠浅の海底地形が比較的均一です。北または南に振れたうねりが入ると、メローでロングライドしやすい波になることがあります。東うねりが正面から入ると、ワイドで速くつながる波やダンパーになりがちです。</p>\n\n                        <p>堤防がサイドショアを遮るため、周辺の開けたポイントより面が整いやすいのも特徴です。片貝漁港は主にロングボード向きで、スモールコンディションならビギナーにも適しています。</p>\n                        <p>難点は、利用可能な駐車場からポイントまで距離があることです。漁港内への一般車両の進入・駐車は禁止されているため、片貝新堤側の駐車場を利用してください。</p>\n                        ",
                },
            "facts":
                {
                    "en":
                        [
                            ["Area", "Chiba North · Kujukuri"],
                            ["Break", "shallow beach break"],
                            ["Bottom", "Sand"],
                            ["Level", "beginner to intermediate"],
                            ["Working tide", "medium to high"],
                            ["Crowds", "Crowded when conditions are good, especially on holidays"],
                            ["Best board", "longboard"],
                        ],
                    "ru":
                        [
                            ["Район", "Северная Тиба · Кудзюкури"],
                            ["Брейк", "пологий бич-брейк"],
                            ["Дно", "Песчаное"],
                            ["Уровень", "начинающий — средний"],
                            ["Подходящий уровень воды", "от среднего до высокого"],
                            ["Люди", "Многолюдно, когда условия хорошие, особенно в праздники"],
                            ["Подходящая доска", "лонгборд"],
                        ],
                    "ja":
                        [
                            ["エリア", "千葉北・九十九里"],
                            ["ブレイク", "遠浅のビーチブレイク"],
                            ["海底", "砂地"],
                            ["レベル", "初級〜中級"],
                            ["対応する潮位", "中〜高"],
                            ["混雑", "コンディションが良いと混雑しやすく、休日は特に混む"],
                            ["向くボード", "ロングボード"],
                        ],
                },
            "region": "chiba-north",
            "break_type": "beach",
            "size_ft_typical": "2-4",
            "water_aug_c": 26,
            "water_feb_c": 14,
            "swell": "ENE-SSE",
            "wind": "SW-N",
            "amenities": ["paid_parking", "shower", "restroom"],
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3mywspp6y4k2r",
                "hours": 72
            },
            "map":
                {
                    "zoom": 17,
                    "amenities":
                        {
                            "restroom": [35.532770905049816, 140.45410860259494],
                            "shower": [35.532770905049816, 140.45410860259494],
                            "paid_parking": [35.53179848999983, 140.45300578018222],
                        },
                },
        },
    "ichinomiya":
        {
            "area": "ichinomiya",
            "title": {
                "en": "Ichinomiya",
                "ru": "Итиномия",
                "ja": "一宮"
            },
            "coordinates": [35.378079, 140.391159],
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
            "facts":
                {
                    "en":
                        [
                            ["Area", "Chiba North · Ichinomiya"],
                            ["Break", "shallow beach break"],
                            ["Bottom", "Sand"],
                            ["Level", "beginner to advanced, depending on conditions"],
                            ["Season", "autumn–winter"],
                            ["Best size", "waist to chest high"],
                            ["Best board", "longboard, funboard, shortboard"],
                        ],
                    "ru":
                        [
                            ["Район", "Северная Тиба · Итиномия"],
                            ["Брейк", "пологий бич-брейк"],
                            ["Дно", "Песчаное"],
                            ["Уровень", "от начинающего до продвинутого — по условиям"],
                            ["Сезон", "осень — зима"],
                            ["Лучший размер", "по пояс — по грудь"],
                            ["Подходящая доска", "лонгборд, фанборд, шортборд"],
                        ],
                    "ja":
                        [
                            ["エリア", "千葉北・一宮"],
                            ["ブレイク", "遠浅のビーチブレイク"],
                            ["海底", "砂地"],
                            ["レベル", "初級〜上級（コンディション次第）"],
                            ["シーズン", "秋〜冬"],
                            ["ベストサイズ", "コシ〜ムネ"],
                            ["向くボード", "ロングボード、ファンボード、ショートボード"],
                        ],
                },
            "region": "chiba-north",
            "break_type": "beach",
            "size_ft_typical": "3-5",
            "water_aug_c": 26,
            "water_feb_c": 14,
            "swell": "NNE-SSE",
            "wind": "SW-NW",
            "amenities": ["paid_parking", "restroom", "shower"],
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3mywsrdesos2r",
                "hours": 72
            },
            "map":
                {
                    "zoom": 16,
                    "amenities":
                        {
                            "restroom": [[35.38116110826715, 140.3913171664306], [35.37803680615724, 140.39094934499892]],
                            "shower": [[35.38199651476501, 140.39136973475868], [35.376817758837646, 140.39107780349985]],
                            "paid_parking": [[35.38168787973108, 140.39115197247418], [35.3770039073883, 140.3910357475373]],
                        },
                },
        },
    "taito":
        {
            "area": "ichinomiya",
            "title": {
                "en": "Taito",
                "ru": "Тайто",
                "ja": "太東"
            },
            "coordinates": [35.330102, 140.39833],
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
            "facts":
                {
                    "en":
                        [
                            ["Area", "Chiba North · Ichinomiya"],
                            ["Break", "shallow beach break"],
                            ["Bottom", "Sand"],
                            ["Level", "beginner to advanced, depending on conditions"],
                            ["Season", "autumn–winter"],
                            ["Best size", "waist to chest high"],
                            ["Best board", "longboard, funboard"],
                        ],
                    "ru":
                        [
                            ["Район", "Северная Тиба · Итиномия"],
                            ["Брейк", "пологий бич-брейк"],
                            ["Дно", "Песчаное"],
                            ["Уровень", "от начинающего до продвинутого — по условиям"],
                            ["Сезон", "осень — зима"],
                            ["Лучший размер", "по пояс — по грудь"],
                            ["Подходящая доска", "лонгборд, фанборд"],
                        ],
                    "ja":
                        [
                            ["エリア", "千葉北・一宮"],
                            ["ブレイク", "遠浅のビーチブレイク"],
                            ["海底", "砂地"],
                            ["レベル", "初級〜上級（コンディション次第）"],
                            ["シーズン", "秋〜冬"],
                            ["ベストサイズ", "コシ〜ムネ"],
                            ["向くボード", "ロングボード、ファンボード"],
                        ],
                },
            "region": "chiba-north",
            "break_type": "beach",
            "size_ft_typical": "1-5",
            "water_aug_c": 26,
            "water_feb_c": 14,
            "swell": "N-E",
            "wind": "SE-W",
            "amenities": ["parking", "restroom", "shower"],
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3mywst4mosk2r",
                "hours": 72
            },
            "map":
                {
                    "zoom": 16,
                    "amenities":
                        {
                            "restroom": [35.329313247513866, 140.39997739631616],
                            "shower": [35.329313247513866, 140.39997739631616],
                            "parking": [35.32887358312741, 140.3995119850874],
                        },
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
            "coordinates": [35.181301, 140.363602],
            "summary":
                {
                    "en": "A beach-break section at Iwawada on the eastern side of Onjuku Bay.",
                    "ru": "Участок бич-брейка в Иваваде на восточной стороне бухты Ондзюку.",
                    "ja": "御宿湾の東側、岩和田にあるビーチブレイクの区間です。",
                },
            "description":
                {
                    "en": "The sandbanks at Iwawada can form distinct peaks, but their position and the current depend on recent swell and tide. ",
                    "ru": "Песчаные банки Ивавады могут формировать выраженные пики, но их положение и течение зависят от недавнего свелла и прилива.",
                    "ja": "岩和田の砂のバンクははっきりしたピークを作ることがありますが、その位置やカレントは直近のうねりと潮位で変わります。",
                },
            "region": "chiba-south",
            "break_type": "beach",
            "size_ft_typical": "2-4",
            "water_aug_c": 26,
            "water_feb_c": 15,
            "swell": "ESE-SSW",
            "wind": "NW-NE",
            "amenities": ["parking", "shower"],
            "bluesky": {
                "post": "https://bsky.app/profile/pyotr777.bsky.social/post/3mywst4mosk2r",
                "hours": 72
            },
            "map": {
                "zoom": 17,
                "amenities": {
                    "shower": [35.18128195489381, 140.36532702737455],
                    "paid_parking": [35.18195330428178, 140.3638844437407]
                }
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
            "coordinates": [35.182143, 140.355927],
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
            "region": "chiba-south",
            "break_type": "beach",
            "size_ft_typical": "2-4",
            "water_aug_c": 26,
            "water_feb_c": 15,
            "swell": "ESE-SSW",
            "wind": "N",
            "map": {
                "zoom": 17,
                "amenities": {}
            },
        },
    "onjuku gyokou":
        {
            "area": "katsuura",
            "title": {
                "en": "Onjuku gyokou",
                "ru": "Ондзюку гёко",
                "ja": "御宿 漁港"
            },
            "coordinates": [35.18115873531658, 140.3508022825051],
            "summary":
                {
                    "en": "A beach-break section near fishing port on the western side of Onjuku Bay.",
                    "ru": "Участок бич-брейка рядом с рыбным портом на западной стороне залива Ондзюку.",
                    "ja": "御宿湾の西側、漁港近くのビーチブレイクの区間です。",
                },
            "description":
                {
                    "en": "The sandbanks at Onjuku gyokou can form distinct peaks, but their position and the current depend on swell and tide. ",
                    "ru": "Песчаные банки Ондзюку гёко могут формировать выраженные пики, но их положение и течение зависят от свелла и прилива.",
                    "ja": "御宿漁港の砂のバンクははっきりしたピークを作ることがありますが、その位置やカレントはうねりと潮位で変わります。",
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
            "coordinates": [35.0435, 140.0125],
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
            "region": "chiba-south",
            "break_type": "beach",
            "size_ft_typical": "2-5",
            "water_aug_c": 26,
            "water_feb_c": 15,
            "swell": "SE-S",
            "wind": "W-NW",
            "map": {
                "zoom": 15,
                "amenities": {}
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
            "coordinates": [34.978, 139.955],
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
            "region": "chiba-south",
            "break_type": "beach",
            "size_ft_typical": "2-5",
            "water_aug_c": 26,
            "water_feb_c": 15,
            "swell": "SE-S",
            "wind": "W-NW",
            "map": {
                "zoom": 15,
                "amenities": {}
            },
        },
    # "tsurigasaki": {
    #     "area": "ichinomiya",
    #     "title": {
    #         "en": "Tsurigasaki / Shidashita",
    #         "ru": "Цуригасаки / Сидасита",
    #         "ja": "釣ヶ崎 / 志田下"
    #     },
    # },
    # "kugenuma": {
    #     "area": "fujisawa",
    #     "title": {
    #         "en": "Kugenuma",
    #         "ru": "Кугэнума",
    #         "ja": "鵠沼"
    #     }
    # },
}


def spots_in_area(area):
    """Return (id, record) pairs in catalogue order."""
    return [(spot_id, spot) for spot_id, spot in SPOTS.items() if spot["area"] == area]


def spot_url(spot_id):
    """Relative page URL, or None for a spot only named in an area guide."""
    if "description" not in SPOTS[spot_id]:
        return None
    return spot_id.replace(" ", "-") + "/index.html"


def map_label(spot, lang):
    title = spot["title"][lang]
    return title if lang == "ja" else f'{title} ({spot["title"]["ja"]})'
