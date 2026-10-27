"""Longboard page content, organized in display order by board type and language.

The family page and each board type live here. Each board contains its card
text and image, followed by the page lead, overview, reference models,
design, conditions, and limitations. Model facts, history, dimensions and
sources live with that model. Edit text here; templates handle presentation.
Published dimensions describe the named variant.
"""

FAMILY = {
    "en": {
        "meta_title": "Longboard — shapes for trim, noseriding and glide",
        "meta_description": "Longboards are a family of boards: classic trim models, all-around and noseriding boards, performance longboards and gliders.",
        "title": "Longboard",
        "lead": "A family of boards built to make the most of trim, glide and small clean waves.",
        "overview": [
            "A longboard is not a single board shape but a family of shapes for different styles of surfing. Their shared trait is a long rail line: it helps you catch waves earlier, hold trim and carry through flatter sections where a shorter board loses speed. Length, outline, rocker and volume all have a marked effect on how a board feels.",
            "A classic longboard suits steady trim; a noseriding board has more area under the front foot; an all-around longboard balances early entry, trim and confident turns; a performance longboard makes it easier to link turns; and a glider uses an extended rail line for long, effortless glide. These are different ways to surf the small, clean waves of Chiba and Shonan — not stages on a ladder of ability.",
            "More length also means more responsibility. A longboard is slower to change direction, harder to handle through shorebreak, and can cause serious injury in a collision. Keep a safe distance from other surfers."
        ],
        "facts": {
            "length": "8&prime;0&Prime;–12&prime;0&Prime;",
            "width": "21&Prime;–24&frac12;&Prime;",
            "thickness": "2&frac12;&Prime;–3&frac14;&Prime;",
            "volume": "55–120&nbsp;L",
            "fins": "Single · 2+1 · Thruster",
            "waves": "1–6&nbsp;ft"
        }
    },
    "ru": {
        "meta_title": "Лонгборд — формы для трима, нозрайдинга и глайда",
        "meta_description": "Лонгборды — семейство досок: классические, универсальные, для нозрайдинга, перформанс-модели и глайдеры.",
        "title": "Лонгборд",
        "lead": "Длинные доски для плавного скольжения, поворотов и катания на носу.",
        "overview": [
            "Лонгборды бывают разной формы и подходят для разных стилей катания. Благодаря длине на них легче поймать волну и пройти пологий участок, где короткая доска теряет скорость. Ширина, изгиб и объём тоже заметно меняют поведение доски.",
            "Классический лонгборд подходит для плавного скольжения; у нозрайдера больше площади под передней ногой; универсальный лонгборд сочетает ранний вход в волну, трим и уверенные повороты; перформанс-лонгборд легче закладывает повороты, а длинный узкий глайдер позволяет долго скользить без частых поворотов. Это разные способы кататься на небольших чистых волнах Тибы и Сёнана, а не ступени мастерства.",
            "Большая длина требует и большей ответственности. Лонгборд медленнее реагирует на смену направления, с ним труднее пройти прибой, а при столкновении он может серьёзно травмировать. Держите достаточное расстояние от других сёрферов."
        ],
        "facts": {
            "length": "8&prime;0&Prime;–12&prime;0&Prime;",
            "width": "21&Prime;–24&frac12;&Prime;",
            "thickness": "2&frac12;&Prime;–3&frac14;&Prime;",
            "volume": "55–120&nbsp;L",
            "fins": "Сингл · 2+1 · трёхплавниковая",
            "waves": "1–6&nbsp;ft"
        }
    },
    "ja": {
        "meta_title": "ロングボード — トリム、ノーズライド、グライドのためのシェイプ",
        "meta_description": "クラシック、オールラウンド、ノーズライダー、パフォーマンス、グライダーなど、ロングボードのさまざまな形を紹介します。",
        "title": "ロングボード",
        "lead": "小波でのグライドからノーズライド、ターンまで楽しめるさまざまなロングボード。",
        "overview": [
            "ロングボードは一つの決まった形ではなく、さまざまなスタイルのサーフィンに対応するさまざまなシェイプがあります。共通するのは長いレールライン。早く波をつかみ、トリムを保ち、短いボードでは失速しやすい緩やかなセクションを走り抜けやすくします。長さ、アウトライン、ロッカー、浮力によって、乗り味は大きく変わります。",
            "クラシックは安定したトリム向き。ノーズライド向けのボードは前足の下に広い面積があり、オールラウンドは早いテイクオフ、トリム、安定したターンをバランスよく備えます。パフォーマンス・ロングボードはターンをつなげやすく、グライダーは長いレールラインで楽に長く走れます。これは千葉や湘南の小さくきれいな波を楽しむ、それぞれ異なる方法で、スキルの序列ではありません。",
            "長いボードほど周囲との距離に気を配る必要があります。ロングボードは方向転換に時間がかかり、ショアブレイクでは扱いにくく、衝突すれば大きなけがにつながることもあります。他のサーファーとは安全な距離を保ってください。"
        ],
        "facts": {
            "length": "8&prime;0&Prime;–12&prime;0&Prime;",
            "width": "21&Prime;–24&frac12;&Prime;",
            "thickness": "2&frac12;&Prime;–3&frac14;&Prime;",
            "volume": "55–120&nbsp;L",
            "fins": "シングル・2+1・スラスター",
            "waves": "1–6&nbsp;ft"
        }
    }
}

LONGBOARDS = {
    "classic": {
        "id": "classic",
        "image": "classic-v2",
        "en": {
            "page_title": "Classic / Traditional",
            "meta_title": "Classic / Traditional — Longboard shapes",
            "meta_description": "A traditional longboard for relaxed trim, flowing lines and classic footwork.",
            "title": "Classic / Traditional",
            "summary": "A full outline with balanced nose, tail and rocker for stable trim and smooth turns.",
            "lead": "A traditional longboard for smooth, unhurried rides and walking along the board.",
            "overview": [
                "A classic longboard is long and wide, with plenty of float. It paddles well and catches waves early. Once on the wave, it carries speed smoothly and offers room to move your feet along the board.",
                "Classic longboards and noseriders overlap, but a classic board can be designed for a range of styles, from relaxed cruising to flowing turns. These models show some of that variety."
            ],
            "models": [
                {
                    "name": "Donald Takayama 60’s Model",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/60-s-donald-takayama-model/",
                    "description": "A single-fin board for smooth rides, turns and walking to the nose.",
                    "history": "The model recalls the style of 1960s longboarding.",
                    "history_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/60-s-donald-takayama-model/",
                    "dimensions": "9′5″ × 22¾″ × 3″",
                    "spec_notes": "Traditional volan fibreglass.",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/60-s-donald-takayama-model/"
                },
                {
                    "name": "McTavish Noosa ’66",
                    "url": "https://www.mctavish.com.au/products/94-noosa-84",
                    "description": "A traditional board with rounded sides and a gently curved bottom, made for smooth, fast rides on small waves.",
                    "history": "Bob McTavish traces this design to boards he developed on Queensland points in the mid-1960s.",
                    "history_source": "https://www.mctavish.com.au/products/94-noosa-84",
                    "dimensions": "9′4″ × 23″ × 3″",
                    "spec_notes": "½″ cedar stringer.",
                    "spec_source": "https://www.mctavish.com.au/products/94-noosa-84"
                },
                {
                    "name": "Bing Classic 3 Stringer",
                    "url": "https://www.usedsurf.jp/gallery/surf-board/5383",
                    "description": "A narrower nose and a wider rear section give this traditional design a focus on speed along the wave.",
                    "history": "Bing based this model on one of its 1960s speed-oriented designs.",
                    "history_source": "https://bingsurf.com/collections/classic-3-stringer",
                    "dimensions": "9′6″ × 23″ × 3″",
                    "spec_notes": "No nose concave.",
                    "spec_source": "https://bingsurf.com/collections/classic-3-stringer"
                },
                {
                    "name": "Bing Pintail Lightweight",
                    "url": "https://bingsurf.com/products/17829-106-pintail-lightweight",
                    "description": "A lighter board with a rounded, tapered tail for flowing turns.",
                    "history": "Dick Brewer designed the Pintail Lightweight in the late 1960s; Matt Calvani later updated it. In a 2022 review of that later version, a Cleanline Surf reviewer noted its responsiveness to small movements and lighter feel when turning.",
                    "history_source": "https://www.cleanlinesurf.com/blogs/surf/bing-pintail-lightweight-longboard-review",
                    "dimensions": "9′0″ × 22½″ × 3″",
                    "spec_notes": "Softer sides toward the nose, a sharper edge near the tail and one fin; two layers of fibreglass on the deck and one underneath.",
                    "spec_source": "https://surfmarket.jp/brand/bing/pintail-lightweight/"
                },
                {
                    "name": "Modern Retro",
                    "url": "https://us.surfindustries.com/products/modern-retro-pu-longboard",
                    "description": "A modern take on a traditional board, with a wide nose and a stable shape for smooth rides.",
                    "history": "In a 2014 test, journalist Hans Aschim found the 9′1″ Retro paddled easily and caught small waves early. GSI designer Corey Davis explained that the bottom helps the board turn without stepping all the way back.",
                    "history_source": "https://coolhunting.com/design/retro-longboard-modern-surfboards/",
                    "dimensions": "9′1″ × 23½″ × 3¼″",
                    "volume": "78.5 L",
                    "spec_notes": "PU version; nose concave, V-shaped bottom farther back; a single fin.",
                    "spec_source": "https://us.surfindustries.com/products/modern-retro-pu-longboard"
                }
            ],
            "design": "The nose is usually rounded, and the middle stays wide for a long distance, providing a stable place to stand and walk. Tail shapes vary: some are broad and square, while others taper to a rounded point. The illustration shows one broad-tailed example. A gentle curve from nose to tail helps the board glide; the sides are often rounded and the board usually has one large fin. Construction varies, and many traditional boards are relatively heavy.",
            "ideal": "At its best on small to medium waves that break gradually, a classic longboard feels smooth and steady. It suits long rides along the wave, gentle turns and moving up and down the board.",
            "tradeoff": "Its length and weight can make it harder to carry and slower to turn. A flatter board can also be less forgiving when entering a steep wave, while a traditional heavy build takes more effort to move around."
        },
        "ru": {
            "page_title": "Классический / традиционный",
            "meta_title": "Классический / традиционный — форма лонгборда",
            "meta_description": "Традиционный лонгборд для спокойного трима, плавных линий и классической работы ног.",
            "title": "Классический / традиционный",
            "summary": "Широкая форма с плавным изгибом от носа к хвосту — для ровного скольжения и мягких поворотов.",
            "lead": "Традиционный лонгборд для спокойного скольжения, плавных поворотов и перемещения по доске.",
            "overview": [
                "Классический лонгборд — длинная и широкая доска с хорошей плавучестью. На ней удобно грести и рано ловить волну. Во время катания доска плавно сохраняет скорость, а её длина позволяет перемещаться по ней.",
                "Классические лонгборды и нозрайдеры во многом похожи, но классическая доска может быть рассчитана на разные стили: от спокойного скольжения до плавных поворотов. Модели ниже показывают это разнообразие."
            ],
            "models": [
                {
                    "name": "Donald Takayama 60’s Model",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/60-s-donald-takayama-model/",
                    "description": "Доска с одним плавником для плавного катания, поворотов и проходов к носу.",
                    "history": "Модель выполнена в стиле лонгбордов 1960-х.",
                    "history_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/60-s-donald-takayama-model/",
                    "dimensions": "9′5″ × 22¾″ × 3″",
                    "spec_notes": "Традиционная стеклоткань volan.",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/60-s-donald-takayama-model/"
                },
                {
                    "name": "McTavish Noosa ’66",
                    "url": "https://www.mctavish.com.au/products/94-noosa-84",
                    "description": "Традиционная доска с округлыми бортами и слегка выпуклым днищем для плавного скольжения на небольших волнах.",
                    "history": "В основе модели — доски, которые Боб Мактавиш разрабатывал в середине 1960-х на волнах Квинсленда.",
                    "history_source": "https://www.mctavish.com.au/products/94-noosa-84",
                    "dimensions": "9′4″ × 23″ × 3″",
                    "spec_notes": "Стрингер из кедра толщиной ½″.",
                    "spec_source": "https://www.mctavish.com.au/products/94-noosa-84"
                },
                {
                    "name": "Bing Classic 3 Stringer",
                    "url": "https://www.usedsurf.jp/gallery/surf-board/5383",
                    "description": "Традиционная форма с более узким носом и широкой задней частью, рассчитанная на скорость вдоль волны.",
                    "history": "Эта модель Bing основана на скоростной форме 1960-х.",
                    "history_source": "https://bingsurf.com/collections/classic-3-stringer",
                    "dimensions": "9′6″ × 23″ × 3″",
                    "spec_notes": "Без углубления на днище под носом.",
                    "spec_source": "https://bingsurf.com/collections/classic-3-stringer"
                },
                {
                    "name": "Bing Pintail Lightweight",
                    "url": "https://bingsurf.com/products/17829-106-pintail-lightweight",
                    "description": "Облегчённая доска с зауженным округлым хвостом для плавных поворотов.",
                    "history": "Дик Брюер создал Pintail Lightweight в конце 1960-х; позднее Мэтт Калвани обновил модель. Автор обзора Cleanline Surf за 2022 год отметил, что обновлённая доска хорошо откликается на небольшие движения и легко поворачивает.",
                    "history_source": "https://www.cleanlinesurf.com/blogs/surf/bing-pintail-lightweight-longboard-review",
                    "dimensions": "9′0″ × 22½″ × 3″",
                    "spec_notes": "Мягкие края ближе к носу, более чёткая кромка у хвоста и один плавник; два слоя стеклоткани сверху и один снизу.",
                    "spec_source": "https://surfmarket.jp/brand/bing/pintail-lightweight/"
                },
                {
                    "name": "Modern Retro",
                    "url": "https://us.surfindustries.com/products/modern-retro-pu-longboard",
                    "description": "Современная версия традиционной доски: широкий нос и устойчивая форма для спокойного катания.",
                    "history": "В тесте 2014 года журналист Ханс Ашим отметил, что на Retro 9′1″ легко грести и рано ловить небольшие волны. Дизайнер GSI Кори Дэвис объяснял, что форма днища помогает поворачивать, не отходя к самому хвосту.",
                    "history_source": "https://coolhunting.com/design/retro-longboard-modern-surfboards/",
                    "dimensions": "9′1″ × 23½″ × 3¼″",
                    "volume": "78.5 L",
                    "spec_notes": "Версия PU; углубление под носом, далее V-образное днище; один плавник.",
                    "spec_source": "https://us.surfindustries.com/products/modern-retro-pu-longboard"
                }
            ],
            "design": "Нос обычно округлый, а середина долго остаётся широкой — на доске удобно стоять и перемещаться. Хвост может быть широким и почти квадратным или сужаться к округлому концу. На иллюстрации показан один из вариантов с широким хвостом. Плавный изгиб доски от носа к хвосту помогает скольжению; края часто округлые, а плавник обычно один и большой. Конструкция бывает разной, но традиционные доски нередко довольно тяжёлые.",
            "ideal": "Лучше всего классический лонгборд чувствует себя на небольших и средних волнах, которые постепенно разбиваются. Он подходит для длинных спокойных проездов вдоль волны, мягких поворотов и перемещения по доске.",
            "tradeoff": "Длинную тяжёлую доску сложнее переносить и поворачивать. Более плоская доска также может хуже подходить для входа на крутую волну, а тяжёлая традиционная доска требует больше усилий в поворотах."
        },
        "ja": {
            "page_title": "クラシック / トラディショナル",
            "meta_title": "クラシック / トラディショナル — ロングボードの形",
            "meta_description": "落ち着いたトリム、流れるライン、伝統的なフットワークを楽しむロングボードです。",
            "title": "クラシック / トラディショナル",
            "summary": "幅のあるアウトラインと、バランスの取れたノーズ、テール、ロッカー。安定したトリムと滑らかなターン向きです。",
            "lead": "穏やかな滑走、滑らかなターン、ボード上の移動を楽しむ伝統的なロングボードです。",
            "overview": [
                "クラシック・ロングボードは長く幅があり、浮力の大きいボードです。パドリングしやすく、早めに波をつかめます。波に乗ると滑らかに速度を保ち、ボード上で足を動かす余裕があります。",
                "クラシックとノーズライダーには重なる部分がありますが、クラシックにはゆったりした滑走から滑らかなターンまでさまざまなタイプがあります。以下のモデルはその一例です。"
            ],
            "models": [
                {
                    "name": "Donald Takayama 60’s Model",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/60-s-donald-takayama-model/",
                    "description": "シングルフィンで、滑らかなグライドやターン、ノーズへの移動を楽しめます。",
                    "history": "タカヤマのこのモデルは、1960年代のロングボードのスタイルを受け継いでいます。",
                    "history_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/60-s-donald-takayama-model/",
                    "dimensions": "9′5″ × 22¾″ × 3″",
                    "spec_notes": "伝統的なボランクロス。",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/60-s-donald-takayama-model/"
                },
                {
                    "name": "McTavish Noosa ’66",
                    "url": "https://www.mctavish.com.au/products/94-noosa-84",
                    "description": "丸みのあるレールと緩やかなボトム形状を持ち、小波でも滑らかに走る伝統的なボード。",
                    "history": "ボブ・マクタビッシュが1960年代半ばにクイーンズランドのポイントで磨いた形を基にしています。",
                    "history_source": "https://www.mctavish.com.au/products/94-noosa-84",
                    "dimensions": "9′4″ × 23″ × 3″",
                    "spec_notes": "厚さ½″のシダーストリンガー。",
                    "spec_source": "https://www.mctavish.com.au/products/94-noosa-84"
                },
                {
                    "name": "Bing Classic 3 Stringer",
                    "url": "https://www.usedsurf.jp/gallery/surf-board/5383",
                    "description": "細めのノーズと幅広い後方を持ち、波に沿って速度を出す伝統的な形。",
                    "history": "Bingの1960年代のスピード重視の形を基にしたモデル。",
                    "history_source": "https://bingsurf.com/collections/classic-3-stringer",
                    "dimensions": "9′6″ × 23″ × 3″",
                    "spec_notes": "ノーズコンケーブはありません。",
                    "spec_source": "https://bingsurf.com/collections/classic-3-stringer"
                },
                {
                    "name": "Bing Pintail Lightweight",
                    "url": "https://bingsurf.com/products/17829-106-pintail-lightweight",
                    "description": "丸く絞ったテールと軽めの構造で滑らかに曲がれます。",
                    "history": "ディック・ブリューワーが1960年代後半に設計し、後にマット・カルバーニが改良。Cleanline Surfの2022年のレビューでは、改良版は小さな動きにも反応し、軽快にターンできると評価されています。",
                    "history_source": "https://www.cleanlinesurf.com/blogs/surf/bing-pintail-lightweight-longboard-review",
                    "dimensions": "9′0″ × 22½″ × 3″",
                    "spec_notes": "ノーズ側は丸みのあるレール、テール付近は明確なエッジ。シングルフィンで、デッキに二層、ボトムに一層のクロス。",
                    "spec_source": "https://surfmarket.jp/brand/bing/pintail-lightweight/"
                },
                {
                    "name": "Modern Retro",
                    "url": "https://us.surfindustries.com/products/modern-retro-pu-longboard",
                    "description": "幅広いノーズと安定した形を持つ、伝統的なボードの現代版。",
                    "history": "2014年の試乗で記者ハンス・アシムは、9′1″のRetroはパドルしやすく小波を早くつかめると評価。GSIのデザイナー、コーリー・デイビスは、底の形が最後尾まで下がらずに方向転換する助けになると説明しました。",
                    "history_source": "https://coolhunting.com/design/retro-longboard-modern-surfboards/",
                    "dimensions": "9′1″ × 23½″ × 3¼″",
                    "volume": "78.5 L",
                    "spec_notes": "PU仕様。ノーズはコンケーブ、後方はVボトム。シングルフィン。",
                    "spec_source": "https://us.surfindustries.com/products/modern-retro-pu-longboard"
                }
            ],
            "design": "ノーズは通常丸く、中央部は長く幅を保つため、立ったり歩いたりする場所が広くなります。テールは幅広い四角形に近いものから、丸く細くなるものまであります。イラストは幅広いテールの一例です。ロッカーは控えめで、レールは丸みを帯び、シングルフィンを使うことが多いです。構造はさまざまですが、伝統的なボードは重めのものが多くあります。",
            "ideal": "小さめから中程度の、ゆっくり崩れる波で持ち味を発揮します。波に沿った長く穏やかな滑走、滑らかなターン、ボード上の移動に向いています。",
            "tradeoff": "長く重いボードは持ち運びや方向転換に力が必要です。ロッカーの少ないボードは急な波でノーズが刺さりやすく、重いモデルほどターンにも力が必要です。"
        }
    },
    "all-around": {
        "id": "all-around",
        "image": "all-around",
        "en": {
            "page_title": "All-around",
            "meta_title": "All-around — Longboard shapes",
            "meta_description": "A versatile longboard that balances early entry, easy trim and controlled turns.",
            "title": "All-around",
            "summary": "A balanced outline with a full nose and rounded tail; moderate rocker combines early entry and trim with confident turns.",
            "lead": "A versatile longboard that balances early entry, easy trim and controlled turns.",
            "overview": [
                "An all-around longboard is a versatile choice for surfers who want to catch waves early, glide along the face and turn without focusing on one style. Its generous size helps with paddling and catching waves, while a more responsive tail gives the board room to grow with its rider.",
                "There is no sharp boundary between categories: some models lean toward traditional longboarding, others toward performance surfing. The examples below show that range."
            ],
            "models": [
                {
                    "name": "Walden Magic Model",
                    "url": "https://www.waldensurfboards.com/pages/magic-model-board-page",
                    "description": "An influential modern all-rounder with concave-to-vee bottom and responsive rails; also suited to nose riding.",
                    "history": "Steve Walden’s Magic Model became his brand’s bestseller from the early 1980s.",
                    "history_source": "https://www.waldensurfboards.com/pages/magic-model-board-page",
                    "dimensions": "9′0″ × 22¼″ × 3¼″",
                    "volume": "78 L",
                    "spec_notes": "Surftech Tuflite version; nose concave, double concave and a V toward the tail.",
                    "spec_source": "https://www.ridershack.com/collections/surfboards/products/walden-magic-model-90"
                },
                {
                    "name": "Modern Golden Rule",
                    "url": "https://au.surfindustries.com/products/modern-golden-rule-pu-longboard",
                    "description": "A user-friendly design with a pulled-in nose, parallel middle and tapered tail for smooth turns.",
                    "dimensions": "9′1″ × 23⅛″ × 3¼″",
                    "volume": "75 L",
                    "spec_notes": "PU version; a gently V-shaped bottom changing to double concave and V at the tail; 2+1 fins.",
                    "spec_source": "https://us.surfindustries.com/products/modern-golden-rule-pu-longboard"
                },
                {
                    "name": "Critical Slide All Rounder",
                    "url": "https://au.surfindustries.com/products/the-critical-slide-society-all-rounder-longboard",
                    "description": "A full-nosed, stable outline with low entry rocker and a tail designed for smooth direction changes.",
                    "dimensions": "9′0″ × 23″ × 3″",
                    "volume": "67 L",
                    "spec_notes": "PU version; soft V through the front and middle, V with double concave at the tail; a single fin.",
                    "spec_source": "https://au.surfindustries.com/products/the-critical-slide-society-all-rounder-longboard"
                },
                {
                    "name": "Creative Army 5 Sugars",
                    "url": "https://www.surfgarage.eu/products/creative-army-five-sugars-pu-longboard",
                    "description": "A versatile longboard with a full nose and enough response for turns.",
                    "history": "Creative Army founder and world longboard champion Josh Constable describes his brand’s Five Sugars as easy to paddle, smooth along the wave and good at turning on both beach and point breaks.",
                    "history_source": "https://us.surfindustries.com/blogs/ground-swell/life-is-better-when-you-surf-josh-constable",
                    "dimensions": "9′1″ × 23¼″ × 2¹³⁄₁₆″",
                    "volume": "68.8 L",
                    "spec_notes": "PU version; concave under the nose and gently rounded V toward the tail; 2+1 fins.",
                    "spec_source": "https://watermanstore.co.nz/products/creative-army-five-sugars-pu-double-stringer"
                },
                {
                    "name": "Torq 24/7",
                    "url": "https://www.torq-surfboards.com/longboard/24-7.html",
                    "description": "An everyday all-rounder with a wide nose, straight middle and narrower tail for smooth turns.",
                    "dimensions": "9′0″ × 23″ × 3⅛″",
                    "volume": "73 L",
                    "spec_notes": "Low nose curve, flatter middle and raised tail; shown in ACT, TEC and TET constructions.",
                    "spec_source": "https://www.torq-surfboards.com/longboard/24-7.html"
                }
            ],
            "design": "Most have a rounded nose, plenty of room to stand and a tail that narrows toward the back. Rounded, squash and pin tails are all found in this category; the illustration shows just one rounded-square example. The board usually has a gentle curve from nose to tail, with a little more lift at the back. The rails are often fuller in the middle and more defined near the tail. The bottom may be V-shaped or concave, and either a single fin or a 2+1 setup can work.",
            "ideal": "At home on small to medium waves that break gradually. Its mix of easy paddling, steady gliding and manageable turns makes it a versatile first longboard when sized to the surfer.",
            "tradeoff": "A narrower, more responsive model may feel less steady than a broad beginner board. An all-around shape also gives less support at the nose than a dedicated noserider and usually turns less sharply than a performance board. Size, construction and fins make a real difference."
        },
        "ru": {
            "page_title": "Универсальный (all-around)",
            "meta_title": "Универсальный (all-around) — форма лонгборда",
            "meta_description": "Универсальный лонгборд, который сочетает ранний вход в волну, лёгкий трим и контролируемые повороты.",
            "title": "Универсальный (all-around)",
            "summary": "Округлый нос, широкая середина и умеренный изгиб помогают рано ловить волну и плавно поворачивать.",
            "lead": "Универсальный лонгборд, который сочетает ранний вход в волну, лёгкий трим и контролируемые повороты.",
            "overview": [
                "Универсальный лонгборд подходит тем, кто хочет рано ловить волну, скользить вдоль неё и поворачивать, не ограничивая себя одним стилем. Благодаря размеру на нём легче грести и ловить волны, а более отзывчивый хвост позволяет кататься активнее.",
                "Чёткой границы у категории нет: одни модели ближе к классическому лонгборду, другие — к доскам для манёвренного катания. Модели ниже показывают этот диапазон."
            ],
            "models": [
                {
                    "name": "Walden Magic Model",
                    "url": "https://www.waldensurfboards.com/pages/magic-model-board-page",
                    "description": "Одна из самых известных универсальных моделей: форма днища и края доски помогают поворачивать, а широкий нос позволяет кататься и спереди.",
                    "history": "Magic Model Стива Уолдена стала самой продаваемой доской его марки с начала 1980-х.",
                    "history_source": "https://www.waldensurfboards.com/pages/magic-model-board-page",
                    "dimensions": "9′0″ × 22¼″ × 3¼″",
                    "volume": "78 L",
                    "spec_notes": "Версия Surftech Tuflite; углубление под носом, двойное углубление и V-образное днище к хвосту.",
                    "spec_source": "https://www.ridershack.com/collections/surfboards/products/walden-magic-model-90"
                },
                {
                    "name": "Modern Golden Rule",
                    "url": "https://au.surfindustries.com/products/modern-golden-rule-pu-longboard",
                    "description": "Нос немного уже, середина сохраняет ширину, а хвост плавно сужается — такая форма помогает закладывать мягкие повороты.",
                    "dimensions": "9′1″ × 23⅛″ × 3¼″",
                    "volume": "75 L",
                    "spec_notes": "Версия PU; мягкое V-образное днище переходит в двойное углубление и V у хвоста; плавники 2+1.",
                    "spec_source": "https://us.surfindustries.com/products/modern-golden-rule-pu-longboard"
                },
                {
                    "name": "Critical Slide All Rounder",
                    "url": "https://au.surfindustries.com/products/the-critical-slide-society-all-rounder-longboard",
                    "description": "Устойчивая доска с широким носом и небольшим подъёмом передней части; плавно меняет направление.",
                    "dimensions": "9′0″ × 23″ × 3″",
                    "volume": "67 L",
                    "spec_notes": "Версия PU; мягкое V-образное днище спереди и в середине, V с двойным углублением у хвоста; один плавник.",
                    "spec_source": "https://au.surfindustries.com/products/the-critical-slide-society-all-rounder-longboard"
                },
                {
                    "name": "Creative Army 5 Sugars",
                    "url": "https://www.surfgarage.eu/products/creative-army-five-sugars-pu-longboard",
                    "description": "Широкий нос позволяет перемещаться вперёд, а форма хвоста помогает поворачивать.",
                    "history": "Создатель марки Creative Army и чемпион мира по лонгборду Джош Констабл отмечает лёгкую греблю Five Sugars, плавное скольжение и повороты на разных типах волн. Это оценка создателя марки.",
                    "history_source": "https://us.surfindustries.com/blogs/ground-swell/life-is-better-when-you-surf-josh-constable",
                    "dimensions": "9′1″ × 23¼″ × 2¹³⁄₁₆″",
                    "volume": "68.8 L",
                    "spec_notes": "Версия PU; углубление спереди и мягкое V-образное днище сзади; плавники 2+1.",
                    "spec_source": "https://watermanstore.co.nz/products/creative-army-five-sugars-pu-double-stringer"
                },
                {
                    "name": "Torq 24/7",
                    "url": "https://www.torq-surfboards.com/longboard/24-7.html",
                    "description": "Доска на каждый день: широкий нос, почти прямая середина и более узкий хвост для плавных поворотов.",
                    "dimensions": "9′0″ × 23″ × 3⅛″",
                    "volume": "73 L",
                    "spec_notes": "Невысокий изгиб носа, плоская середина и приподнятый хвост; версии ACT, TEC и TET.",
                    "spec_source": "https://www.torq-surfboards.com/longboard/24-7.html"
                }
            ],
            "design": "У такой доски обычно округлый нос, широкая середина и сужающийся хвост. Форма хвоста бывает разной; на иллюстрации показан один из вариантов с округло-квадратным концом. Изгиб от носа к хвосту чаще умеренный, причём хвост может быть приподнят сильнее. Края доски обычно округлые в середине и более чёткие ближе к хвосту. Днище может быть V-образным или с продольными углублениями. Встречаются доски как с одним плавником, так и с большим центральным и двумя боковыми.",
            "ideal": "Хорошо чувствует себя на небольших и средних волнах, которые постепенно разбиваются. Сочетание лёгкой гребли, устойчивого скольжения и плавных поворотов делает такую доску удобным первым лонгбордом, если её размер подходит сёрферу.",
            "tradeoff": "Более узкая и манёвренная модель может быть менее устойчивой, чем широкая учебная доска. Универсальный лонгборд также уступает нозрайдеру в катании на носу, а перформанс-доске — в резких поворотах. Многое зависит от размера, конструкции и плавников."
        },
        "ja": {
            "page_title": "オールラウンド",
            "meta_title": "オールラウンド — ロングボードの形",
            "meta_description": "早いテイクオフ、扱いやすいトリム、コントロールしやすいターンをバランスよく備えたロングボードです。",
            "title": "オールラウンド",
            "summary": "バランスの取れたアウトラインに、幅を残したノーズと丸みのあるテール。ほどよいロッカーが早いテイクオフ、トリム、安定したターンを両立します。",
            "lead": "早いテイクオフ、扱いやすいトリム、コントロールしやすいターンをバランスよく備えたロングボードです。",
            "overview": [
                "オールラウンド・ロングボードは、波を早めにつかみ、フェイスを滑り、ターンも楽しみたい人に向く一本です。長さと浮力がパドリングを助け、反応のよいテールならより積極的なターンにも対応できます。",
                "このカテゴリーに明確な境界はありません。伝統的なノーズライド寄りのモデルも、パフォーマンス寄りのモデルもあります。以下のモデルは、その幅広さを示しています。"
            ],
            "models": [
                {
                    "name": "Walden Magic Model",
                    "url": "https://www.waldensurfboards.com/pages/magic-model-board-page",
                    "description": "コンケーブからVeeへ変わるボトムと反応のよいレールを備えた代表的な現代の万能モデル。ノーズライドも可能。",
                    "history": "スティーブ・ウォルデンのMagic Modelは1980年代初めからブランドの人気モデルになりました。",
                    "history_source": "https://www.waldensurfboards.com/pages/magic-model-board-page",
                    "dimensions": "9′0″ × 22¼″ × 3¼″",
                    "volume": "78 L",
                    "spec_notes": "Surftech Tuflite仕様。ノーズコンケーブからダブルコンケーブ、テール側のV字へ変化。",
                    "spec_source": "https://www.ridershack.com/collections/surfboards/products/walden-magic-model-90"
                },
                {
                    "name": "Modern Golden Rule",
                    "url": "https://au.surfindustries.com/products/modern-golden-rule-pu-longboard",
                    "description": "やや絞ったノーズ、平行な中央部、細くなるテールで滑らかにターンできる扱いやすいモデル。",
                    "dimensions": "9′1″ × 23⅛″ × 3¼″",
                    "volume": "75 L",
                    "spec_notes": "PU仕様。緩やかなV字からダブルコンケーブ、テールのV字へ変化。フィンは2+1。",
                    "spec_source": "https://us.surfindustries.com/products/modern-golden-rule-pu-longboard"
                },
                {
                    "name": "Critical Slide All Rounder",
                    "url": "https://au.surfindustries.com/products/the-critical-slide-society-all-rounder-longboard",
                    "description": "幅広いノーズと安定したアウトライン、低いエントリーロッカーで滑らかに方向転換。",
                    "dimensions": "9′0″ × 23″ × 3″",
                    "volume": "67 L",
                    "spec_notes": "PU仕様。前方と中央は緩やかなV字、テールはV字とダブルコンケーブ。シングルフィン。",
                    "spec_source": "https://au.surfindustries.com/products/the-critical-slide-society-all-rounder-longboard"
                },
                {
                    "name": "Creative Army 5 Sugars",
                    "url": "https://www.surfgarage.eu/products/creative-army-five-sugars-pu-longboard",
                    "description": "幅広いノーズを持ち、ターンもしやすい万能モデル。",
                    "history": "Creative Army創設者で世界ロングボード王者のジョシュ・コンスタブルは、Five Sugarsのパドルのしやすさ、滑らかな滑走、ビーチとポイントでのターンを評価しています。",
                    "history_source": "https://us.surfindustries.com/blogs/ground-swell/life-is-better-when-you-surf-josh-constable",
                    "dimensions": "9′1″ × 23¼″ × 2¹³⁄₁₆″",
                    "volume": "68.8 L",
                    "spec_notes": "PU仕様。ノーズコンケーブから後方の緩やかなV字へ。フィンは2+1。",
                    "spec_source": "https://watermanstore.co.nz/products/creative-army-five-sugars-pu-double-stringer"
                },
                {
                    "name": "Torq 24/7",
                    "url": "https://www.torq-surfboards.com/longboard/24-7.html",
                    "description": "幅広いノーズ、まっすぐな中央、細めのテールを持つ、普段使いの万能モデル。",
                    "dimensions": "9′0″ × 23″ × 3⅛″",
                    "volume": "73 L",
                    "spec_notes": "低めのノーズ、平らな中央、上がったテール。ACT・TEC・TET仕様。",
                    "spec_source": "https://www.torq-surfboards.com/longboard/24-7.html"
                }
            ],
            "design": "丸みのあるノーズと幅を残した中央部で立ちやすく、テールはターンしやすいようにやや絞られています。テールにはさまざまな形があり、イラストはラウンドスクエアの一例です。ロッカーは全体に控えめから中程度で、テール側に少し反りを加えたものもあります。レールは中央では厚めで丸く、テールに向かって薄くはっきりした形になることが多いです。ボトムにはV字やコンケーブなどがあり、フィンはシングルと2+1の両方が見られます。",
            "ideal": "小さめから中程度の、ゆっくり崩れる波に向いています。パドリングしやすく、滑走も安定し、ターンにも対応できるため、体格に合ったサイズなら最初のロングボードとしても使えます。",
            "tradeoff": "細身でよく動くモデルは、幅広いビギナー向けボードより安定感が少ない場合があります。ノーズライドでは専用のノーズライダーに、鋭いターンではパフォーマンス型に及びません。サイズや構造、フィンによっても乗り味は変わります。"
        }
    },
    "noserider": {
        "id": "noserider",
        "image": "noserider-v3",
        "en": {
            "page_title": "Noserider",
            "meta_title": "Noserider — Longboard shapes",
            "meta_description": "A longboard shaped to stay settled while you move forward and ride near the nose.",
            "title": "Noserider",
            "summary": "A wide nose gives room for the feet; the tail can be broad or tapered, with its shape helping the board stay on the wave.",
            "lead": "A longboard made for walking forward and riding from the nose.",
            "overview": [
                "A noserider is a longboard made for walking toward the front and riding near the tip. Its wide nose offers room for the surfer’s feet. The shape of the board and its fin help it stay positioned on the wave when weight moves forward.",
                "Many noseriders are also classic longboards. These models put particular emphasis on riding near the nose; In The Pink combines nose riding with more active turns."
            ],
            "models": [
                {
                    "name": "Bing Original Noserider",
                    "url": "https://howlerbros.com/products/bing-original-noserider-9-4",
                    "description": "A landmark 1960s noserider with a deep concave beneath its wide nose.",
                    "history": "Bing Copeland and Donald Takayama designed the original in 1965 for David Nuuhiwa.",
                    "history_source": "https://bingsurf.com/collections/original-noserider",
                    "dimensions": "9′6″ × 23″ × 3¹⁄₁₆″",
                    "spec_notes": "Traditional 10 oz volan fibreglass.",
                    "spec_source": "https://bingsurf.com/collections/original-noserider"
                },
                {
                    "name": "Donald Takayama Classic Noserider",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/classic-noserider/",
                    "description": "A traditional, heavily built single-fin board for nose riding.",
                    "history": "Takayama developed this design in the 1960s for the era’s focus on nose riding.",
                    "history_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/classic-noserider/",
                    "dimensions": "9′6″ × 22¾″ × 3″",
                    "spec_notes": "Heavy volan fibreglass.",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/classic-noserider/"
                },
                {
                    "name": "Donald Takayama Model T",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/single-fin-longboards/model-t/",
                    "description": "A wide-nosed board combining rides near the nose with smooth turns.",
                    "history": "Joel Tudor developed the Model T with Donald Takayama. Longboard champion Justin Quintal praised its balanced shape and ease of riding, pointing to its central wide point and gently curved profile.",
                    "history_source": "https://www.surfer.com/news/how-to-buy-your-first-longboard",
                    "dimensions": "9′6″ × 23″ × 3″",
                    "spec_notes": "Square tail; rounded sides; a single fin.",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/single-fin-longboards/model-t/"
                },
                {
                    "name": "Bing Continental",
                    "url": "https://bingsurf.com/collections/continental/",
                    "description": "A wide board with nearly parallel rails, nose concave and a pronounced tail kick.",
                    "history": "Bing shaper Matt Calvani developed the Continental with team rider Mick Rodgers.",
                    "history_source": "https://bingsurf.com/collections/continental/",
                    "dimensions": "9′6″ × 23.5″ × 3.06″",
                    "volume": "78.1 L",
                    "spec_notes": "The nose concave is 5⁄16″ deep (about 8 mm).",
                    "spec_source": "https://bingsurf.com/collections/continental/"
                },
                {
                    "name": "Donald Takayama In The Pink",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/progressive-longboards/in-the-pink",
                    "description": "A more versatile noserider that combines riding near the nose with active turns and uses a large centre fin and two smaller side fins.",
                    "history": "Surftech also makes this Takayama design; the shaper and company worked together for over 20 years.",
                    "history_source": "https://surftech.com/products/in-the-pink-tuflite-pro",
                    "dimensions": "9′6″ × 23⅛″ × 3⅛″",
                    "spec_notes": "Recommended centre fin: 7¼″ or 8¼″, with side fins.",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/progressive-longboards/in-the-pink"
                }
            ],
            "design": "A wide, rounded nose provides room to stand near the front. Many noseriders have long, nearly parallel sides; the tail can be broad or taper inward, as in the illustration. Many have soft, rounded rails and one large fin. Some have concave under the nose and extra lift at the tail. Together, these features can help the board stay in position as the surfer moves forward, though designs and waves vary.",
            "ideal": "Noseriders suit clean waves that break gradually and have a long, open face. They are made for smooth rides, moving along the board and spending time near the nose.",
            "tradeoff": "A noserider can paddle well and feel stable, but its length and often substantial weight make it slower to turn and harder to carry. Riding near the nose still depends on the wave, position and timing as well as the board."
        },
        "ru": {
            "page_title": "Нозрайдер",
            "meta_title": "Нозрайдер — форма лонгборда",
            "meta_description": "Лонгборд, рассчитанный на устойчивость, когда вы перемещаетесь вперёд и катаетесь у самого носа.",
            "title": "Нозрайдер",
            "summary": "Широкий нос даёт место для ног, а форма хвоста помогает удерживаться на волне во время катания с носа.",
            "lead": "Лонгборд для проходов вперёд и катания с носа.",
            "overview": [
                "Нозрайдер — лонгборд, на котором можно пройти вперёд и кататься с носа. Широкий нос даёт место для ног, а форма доски и плавник помогают ей сохранять положение на волне, когда вес переносится вперёд.",
                "Многие нозрайдеры одновременно являются классическими лонгбордами. Модели ниже особенно хорошо подходят для катания с носа; In The Pink сочетает его с более активными поворотами."
            ],
            "models": [
                {
                    "name": "Bing Original Noserider",
                    "url": "https://howlerbros.com/products/bing-original-noserider-9-4",
                    "description": "Знаменитый нозрайдер с глубоким углублением на днище под носом.",
                    "history": "Бинг Коупленд и Дональд Такаяма разработали оригинал в 1965 году для Дэвида Нуухивы.",
                    "history_source": "https://bingsurf.com/collections/original-noserider",
                    "dimensions": "9′6″ × 23″ × 3¹⁄₁₆″",
                    "spec_notes": "Традиционная стеклоткань volan плотностью 10 унций.",
                    "spec_source": "https://bingsurf.com/collections/original-noserider"
                },
                {
                    "name": "Donald Takayama Classic Noserider",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/classic-noserider/",
                    "description": "Традиционная тяжёлая доска с одним плавником для катания с носа.",
                    "history": "Такаяма разработал эту форму в 1960-х, когда катание на носу было особенно популярно.",
                    "history_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/classic-noserider/",
                    "dimensions": "9′6″ × 22¾″ × 3″",
                    "spec_notes": "Плотная стеклоткань volan.",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/classic-noserider/"
                },
                {
                    "name": "Donald Takayama Model T",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/single-fin-longboards/model-t/",
                    "description": "Доска с широким носом, сочетающая катание с носа и плавные повороты.",
                    "history": "Джоэл Тюдор разработал Model T вместе с Дональдом Такаяма. Чемпион по лонгборду Джастин Квинтал высоко оценил её сбалансированную форму и простоту управления, отметив широкую середину и небольшой изгиб.",
                    "history_source": "https://www.surfer.com/news/how-to-buy-your-first-longboard",
                    "dimensions": "9′6″ × 23″ × 3″",
                    "spec_notes": "Квадратный хвост, округлые края; один плавник.",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/single-fin-longboards/model-t/"
                },
                {
                    "name": "Bing Continental",
                    "url": "https://bingsurf.com/collections/continental/",
                    "description": "Широкая доска с почти параллельными бортами, углублением под носом и заметно приподнятым хвостом.",
                    "history": "Шейпер Bing Мэтт Калвани разработал Continental вместе с командным райдером Миком Роджерсом.",
                    "history_source": "https://bingsurf.com/collections/continental/",
                    "dimensions": "9′6″ × 23.5″ × 3.06″",
                    "volume": "78.1 L",
                    "spec_notes": "Глубина вогнутости днища под носом — 5⁄16″ (около 8 мм).",
                    "spec_source": "https://bingsurf.com/collections/continental/"
                },
                {
                    "name": "Donald Takayama In The Pink",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/progressive-longboards/in-the-pink",
                    "description": "Более универсальный нозрайдер для катания с носа и активных поворотов, с большим центральным и двумя небольшими боковыми плавниками.",
                    "history": "Модель выпускается также в конструкции Surftech; компания сотрудничала с Такаяма более 20 лет.",
                    "history_source": "https://surftech.com/products/in-the-pink-tuflite-pro",
                    "dimensions": "9′6″ × 23⅛″ × 3⅛″",
                    "spec_notes": "Рекомендуемый центральный плавник — 7¼″ или 8¼″, с боковыми плавниками.",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/progressive-longboards/in-the-pink"
                }
            ],
            "design": "Широкий округлый нос даёт место для ног впереди доски. У многих нозрайдеров борта на значительном участке почти параллельны; хвост может быть широким или сужаться, как на иллюстрации. Борта часто округлые, а плавник обычно один и большой. У некоторых досок под носом есть углубление на днище, а хвост сильнее загнут вверх. Вместе эти особенности могут помогать доске сохранять положение, когда сёрфер перемещается вперёд, хотя формы досок и волн различаются.",
            "ideal": "Нозрайдер подходит для чистых волн, которые постепенно разбиваются и оставляют длинную открытую стенку. Он создан для плавного скольжения, перемещения по доске и катания с носа.",
            "tradeoff": "На нозрайдере обычно легко грести, и он может быть устойчивым. При этом его длина и зачастую большой вес затрудняют переноску и замедляют повороты. Катание на носу зависит не только от доски, но и от волны, положения на ней и своевременного перемещения."
        },
        "ja": {
            "page_title": "ノーズライダー",
            "meta_title": "ノーズライダー — ロングボードの形",
            "meta_description": "前方へ歩き、ノーズ付近で波に乗るときの安定性を重視したロングボードです。",
            "title": "ノーズライダー",
            "summary": "幅広いノーズは足を置きやすく、テールには幅広い形も絞った形もあります。波に合わせてノーズライドを楽しむボードです。",
            "lead": "ボードの前方へ歩き、ノーズライディングを楽しむためのロングボードです。",
            "overview": [
                "ノーズライダーは、ボードの前方へ歩き、ノーズに立って波に乗るためのロングボードです。幅広いノーズには足を置く余裕があり、ボードの形とフィンが、体重を前に移したときも波の上で安定しやすい乗り味を生みます。",
                "ノーズライダーの多くはクラシック・ロングボードでもあります。以下はノーズライディングを特に重視したモデルです。In The Pinkはノーズでの安定感と軽快なターンを両立しています。"
            ],
            "models": [
                {
                    "name": "Bing Original Noserider",
                    "url": "https://howlerbros.com/products/bing-original-noserider-9-4",
                    "description": "幅広いノーズの裏に深いコンケーブを備えた、1960年代を代表するノーズライダー。",
                    "history": "1965年にビング・コープランドとドナルド・タカヤマがデイビッド・ヌイーヴァのために設計。",
                    "history_source": "https://bingsurf.com/collections/original-noserider",
                    "dimensions": "9′6″ × 23″ × 3¹⁄₁₆″",
                    "spec_notes": "伝統的な10オンスのボランクロス。",
                    "spec_source": "https://bingsurf.com/collections/original-noserider"
                },
                {
                    "name": "Donald Takayama Classic Noserider",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/classic-noserider/",
                    "description": "重めのラミネートとシングルフィンを備えた伝統的なノーズライダー。",
                    "history": "1960年代のノーズライドのためにタカヤマが考案した形。",
                    "history_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/classic-noserider/",
                    "dimensions": "9′6″ × 22¾″ × 3″",
                    "spec_notes": "厚いボランクロス。",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/dt-classics/classic-noserider/"
                },
                {
                    "name": "Donald Takayama Model T",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/single-fin-longboards/model-t/",
                    "description": "幅広いノーズのボード。ノーズでの滑走と滑らかなターンを両立。",
                    "history": "ジョエル・チューダーがドナルド・タカヤマと開発。ロングボード王者ジャスティン・クインタルは、最も幅の広い位置が中央にあり、反りが穏やかな、バランスのよい扱いやすい形と評価しました。",
                    "history_source": "https://www.surfer.com/news/how-to-buy-your-first-longboard",
                    "dimensions": "9′6″ × 23″ × 3″",
                    "spec_notes": "スクエアテール、丸い側面、シングルフィン。",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/single-fin-longboards/model-t/"
                },
                {
                    "name": "Bing Continental",
                    "url": "https://bingsurf.com/collections/continental/",
                    "description": "ほぼ平行なレール、ノーズコンケーブ、反りを強めたテールを持つ幅広いボード。",
                    "history": "Bingのシェイパー、マット・カルバーニがライダーのミック・ロジャースと開発。",
                    "history_source": "https://bingsurf.com/collections/continental/",
                    "dimensions": "9′6″ × 23.5″ × 3.06″",
                    "volume": "78.1 L",
                    "spec_notes": "ノーズコンケーブの深さは5⁄16″（約8 mm）。",
                    "spec_source": "https://bingsurf.com/collections/continental/"
                },
                {
                    "name": "Donald Takayama In The Pink",
                    "url": "https://www.surfboardsbydonaldtakayama.com/surfboards/progressive-longboards/in-the-pink",
                    "description": "ノーズライドを重視しながら、積極的なターンも楽しめるモデル。中央に大きなフィン、両側に小さなフィンを使います。",
                    "history": "このタカヤマのモデルはSurftechの構造でも製造されています。タカヤマと同社の協力関係は20年以上続きました。",
                    "history_source": "https://surftech.com/products/in-the-pink-tuflite-pro",
                    "dimensions": "9′6″ × 23⅛″ × 3⅛″",
                    "spec_notes": "推奨センターフィンは7¼″または8¼″で、サイドフィンと組み合わせます。",
                    "spec_source": "https://www.surfboardsbydonaldtakayama.com/surfboards/progressive-longboards/in-the-pink"
                }
            ],
            "design": "幅広く丸いノーズは前方に立つための足場になります。多くのモデルはレールラインが長く、ほぼ平行で、テールは幅広いものやイラストのように細くなるものがあります。レールは丸みを帯び、センターフィンを一本使うことが多いです。ノーズコンケーブや強めのテールロッカーを備えたモデルもあります。これらの特徴は、サーファーが前に移動したときに位置を保つ助けになりますが、ボードや波の形はさまざまです。",
            "ideal": "ゆっくりと崩れ、長く開いたフェイスのある波に向いています。滑らかなグライドとボード上の移動、ノーズライディングを楽しめます。",
            "tradeoff": "パドリングしやすく安定感がありますが、長く重いことが多いため、持ち運びや方向転換には力が必要です。ノーズライディングのしやすさは、ボードだけでなく波の形やポジション、前へ出るタイミングにも左右されます。"
        }
    },
    "performance": {
        "id": "performance",
        "image": "performance",
        "en": {
            "page_title": "High-performance longboard",
            "meta_title": "High-performance longboard — Longboard shapes",
            "meta_description": "A high-performance longboard is designed for sharper turns and a more dynamic ride, giving you more control on steeper waves.",
            "title": "Performance",
            "summary": "A pulled-in nose and tail with more rocker for tighter turns and quicker changes of direction.",
            "lead": "A high-performance longboard is designed for sharper turns and a more dynamic ride, giving you more control on steeper waves.",
            "overview": [
                "A high-performance longboard is a full-length board built for active, responsive surfing with a shortboard feel. It lets you make sharper turns, change direction quickly and work the steeper part of the wave, while still leaving room for footwork and noseriding. These boards are aimed mainly at advanced surfers who are confident on a longboard and want a more dynamic ride.",
                "High-performance longboards range from boards for everyday fun to dedicated competition models. Well-known designs cover both ends of that range."
            ],
            "models": [
                {
                    "name": "Firewire Taylor Jensen Pro",
                    "url": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro",
                    "description": "a competition-focused model for speed, powerful turns and dynamic surfing in good waves.",
                    "history": "Dan Mann and Taylor Jensen developed it together; Jensen has ridden it to world titles.",
                    "history_source": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro",
                    "dimensions": "9′0″ × 22⅛″ × 2⅝″",
                    "volume": "61 L",
                    "spec_notes": "I-Bolic Volcanic version; nose concave, double concave toward the tail, finishing in V.",
                    "spec_source": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro"
                },
                {
                    "name": "Firewire Taylor Jensen Pro V",
                    "url": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro-v",
                    "description": "built for everyday fun, including smaller, weaker waves, with easy direction changes and good speed through flatter sections.",
                    "history": "Jensen and Dan Mann developed it together; Firewire introduced its I-Bolic version in 2024.",
                    "history_source": "https://www.firewiresurfboards.com/blogs/news/introducing-the-tj-pro-tj-pro-v",
                    "dimensions": "9′0″ × 22⅛″ × 2⅝″",
                    "volume": "62 L",
                    "spec_notes": "I-Bolic Volcanic version; flatter curve and wider nose than TJ Pro; squash tail.",
                    "spec_source": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro-v"
                },
                {
                    "name": "NSP Pro-9",
                    "url": "https://www.nspsurfboards.com/product/surf/pro-9-cse/",
                    "description": "for active surfing across a range of conditions, from relaxed trim and noseriding to fast, powerful turns.",
                    "history": "Hawaiian shaper Carl Schaper designed the Pro-9 for NSP.",
                    "history_source": "https://www.nspsurfboards.com/product/technology/cse/pro-9-cse/",
                    "dimensions": "9′1″ × 22″ × 2¾″",
                    "volume": "62.9 L",
                    "spec_notes": "CSE version; rounded bottom into V and double concave; five fin boxes.",
                    "spec_source": "https://www.nspsurfboards.com/product/surf/pro-9-cse/"
                },
                {
                    "name": "CJ Nelson Designs GX1000 / Ibis",
                    "url": "https://thunderboltsurf.com/cj-nelson-designs/ibis/",
                    "description": "for surfers who enjoy speed and maneuverability, combining sharp turns with classic longboard glide and noseriding.",
                    "history": "CJ Nelson designed the Ibis with shaper Ryan Engle.",
                    "history_source": "https://thunderboltsurf.com/cj-nelson-designs/ibis/",
                    "dimensions": "9′0″ × 23″ × 3″",
                    "volume": "66.74 L",
                    "spec_notes": "Ibis; nose concave and 2+1 fin boxes.",
                    "spec_source": "https://thunderboltsurf.com/cj-nelson-designs/ibis/"
                },
                {
                    "name": "Kai Sallas Lava Flow",
                    "url": "https://thunderboltsurf.jp/products/lava-flow",
                    "description": "for fast, powerful waves, deep carving turns and barrel riding; especially suited to head-high to double-overhead surf.",
                    "history": "Lava Flow is shaped by Hawaiian longboarder Kai Sallas.",
                    "history_source": "https://thunderboltsurf.jp/products/lava-flow",
                    "dimensions": "9′0″ × 22¼″ × 2⅝″",
                    "volume": "61.3 L",
                    "spec_notes": "Thunderbolt Silver version; V-shaped bottom, pointed tail and 2+1 fin boxes.",
                    "spec_source": "https://thunderboltsurf.jp/products/lava-flow"
                }
            ],
            "design": "Across these models, the outline is usually more refined at the tail and the rails are thinner, lower and more defined than on a traditional log, so the board holds when loaded on rail. Rocker is matched to the waves the board is designed for. A continuous curve, or extra lift at the nose and tail, helps a dedicated high-performance board follow a steep wave face on takeoff without burying its nose. An everyday version may be flatter through the middle, helping it catch waves earlier and carry speed through softer sections. Bottom contours commonly combine a light nose concave with double concave, vee or spiral vee under the rear foot; they create lift and channel water while helping the board roll rail to rail. Rounded pins, pin tails and squash tails trade hold and release differently, and 2+1, quad or 4+1 fin boxes let the rider tune drive, pivot and looseness.",
            "diagrams": [
                {
                    "filename": "rocker-bottom-shape.png",
                    "title": "Rocker and bottom contours",
                    "alt": "Side profile of a high-performance longboard with a dashed baseline and three linked transverse sections: shallow single concave at the nose, double concave at the middle and vee at the tail.",
                    "caption": "Compared with a classic or noserider longboard, this shape carries more nose and tail rocker, with a fast, flatter-running centre. Thin, foiled rails engage and release more easily. The bottom transitions from a shallow single concave under the nose to a double concave through the middle, then fades into vee in the fin area for quicker rail-to-rail transitions."
                },
                {
                    "filename": "fin-options.png",
                    "title": "Fin options",
                    "alt": "Two diagrams of a longboard tail: one with a 2 plus 1 fin configuration and one with a five-box 4 plus 1 configuration.",
                    "caption": "A 2+1 setup balances drive and pivot. A five-box layout can be tuned as a single, 2+1, thruster or quad."
                }
            ],
            "ideal": "Best for intermediate and advanced surfers who already control a longboard from the tail and can place their feet deliberately. A dedicated HP model comes alive on clean, shoulder-high and larger waves with a defined face, speed and a section to turn against; a flatter, wider everyday version can also work in smaller beach-break surf. Choose it when active carving, top turns, cutbacks and fast down-the-line surfing matter as much as trim and nose time.",
            "tradeoff": "The responsiveness comes from a more exacting balance of volume, rail shape, rocker and fin setup. Compared with a fuller classic or all-around longboard, a focused HP shape usually catches weak waves later, carries less speed through slow water and is less forgiving of a late step or poorly timed turn. It also has more speed and a sharper rail in powerful surf, so it needs clear water, confident control and deliberate equipment choices. Test the size and fin configuration in the waves you actually surf rather than choosing only by a model’s competition pedigree."
        },
        "ru": {
            "page_title": "High-performance лонгборд",
            "meta_title": "High-performance лонгборд — форма лонгборда",
            "meta_description": "High-performance лонгборд — это более манёвренный лонгборд для активного катания: на нём легче делать резкие повороты и кататься на крутых волнах.",
            "title": "Перформанс",
            "summary": "Зауженные нос и корма, более выраженный рокер — для более резких поворотов и быстрой смены направления.",
            "lead": "Перформанс-лонгборд создан для активного катания: он быстрее меняет направление и позволяет делать резкие повороты на крутой волне.",
            "overview": [
                "Перформанс-лонгборд сочетает длину обычного лонгборда с более резкими и быстрыми поворотами. На нём можно активно кататься на крутых участках волны, при этом перемещаться по доске и выходить на нос. Такой тип больше подходит тем, кто уже уверенно управляет лонгбордом.",
                "Одни модели рассчитаны на повседневное катание, другие — на соревнования. Среди досок ниже есть примеры обоих направлений."
            ],
            "models": [
                {
                    "name": "Firewire Taylor Jensen Pro",
                    "url": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro",
                    "description": "модель с соревновательным уклоном для скорости, мощных поворотов и активного катания на хороших волнах.",
                    "history": "Дэн Манн и Тейлор Дженсен разработали её вместе; Дженсен выигрывал на ней мировые титулы.",
                    "history_source": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro",
                    "dimensions": "9′0″ × 22⅛″ × 2⅝″",
                    "volume": "61 L",
                    "spec_notes": "Версия I-Bolic Volcanic; углубление под носом, двойное у хвоста и V-образное днище на выходе.",
                    "spec_source": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro"
                },
                {
                    "name": "Firewire Taylor Jensen Pro V",
                    "url": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro-v",
                    "description": "для повседневного катания, в том числе на небольших и слабых волнах; легко меняет направление и проходит пологие участки.",
                    "history": "Дженсен и Дэн Манн разработали её вместе; версию I-Bolic Firewire представила в 2024 году.",
                    "history_source": "https://www.firewiresurfboards.com/blogs/news/introducing-the-tj-pro-tj-pro-v",
                    "dimensions": "9′0″ × 22⅛″ × 2⅝″",
                    "volume": "62 L",
                    "spec_notes": "Версия I-Bolic Volcanic; более плоский изгиб и широкий нос, чем у TJ Pro; округло-квадратный хвост.",
                    "spec_source": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro-v"
                },
                {
                    "name": "NSP Pro-9",
                    "url": "https://www.nspsurfboards.com/product/surf/pro-9-cse/",
                    "description": "для активного катания в разных условиях: от спокойного скольжения и нозрайдинга до быстрых, мощных поворотов.",
                    "history": "Гавайский шейпер Карл Шейпер разработал Pro-9 для NSP.",
                    "history_source": "https://www.nspsurfboards.com/product/technology/cse/pro-9-cse/",
                    "dimensions": "9′1″ × 22″ × 2¾″",
                    "volume": "62.9 L",
                    "spec_notes": "Версия CSE; округлое днище переходит в V и двойное углубление; пять боксов для плавников.",
                    "spec_source": "https://www.nspsurfboards.com/product/surf/pro-9-cse/"
                },
                {
                    "name": "CJ Nelson Designs GX1000 / Ibis",
                    "url": "https://thunderboltsurf.com/cj-nelson-designs/ibis/",
                    "description": "для любителей скорости и манёвров, которые хотят сочетать резкие повороты с классическим скольжением и катанием с носа.",
                    "history": "CJ Нельсон разработал Ibis вместе с шейпером Райаном Энглом.",
                    "history_source": "https://thunderboltsurf.com/cj-nelson-designs/ibis/",
                    "dimensions": "9′0″ × 23″ × 3″",
                    "volume": "66.74 L",
                    "spec_notes": "Ibis: углубление под носом, боксы для плавников 2+1.",
                    "spec_source": "https://thunderboltsurf.com/cj-nelson-designs/ibis/"
                },
                {
                    "name": "Kai Sallas Lava Flow",
                    "url": "https://thunderboltsurf.jp/products/lava-flow",
                    "description": "для быстрых и мощных волн, глубоких поворотов и катания в трубах; особенно подходит для волн от высоты головы до двойного роста.",
                    "history": "Lava Flow создана гавайским лонгбордером Каем Салласом.",
                    "history_source": "https://thunderboltsurf.jp/products/lava-flow",
                    "dimensions": "9′0″ × 22¼″ × 2⅝″",
                    "volume": "61.3 L",
                    "spec_notes": "Версия Thunderbolt Silver; V-образное днище, зауженный хвост и боксы 2+1.",
                    "spec_source": "https://thunderboltsurf.jp/products/lava-flow"
                }
            ],
            "design": "По сравнению с классическим лонгбордом у таких досок обычно более узкий хвост и более тонкие, чётко очерченные борта. Благодаря этому доску легче поставить на борт в повороте. Продольный изгиб доски, или рокер, подбирают под волны, для которых она предназначена. У модели для крутых волн он может плавно проходить по всей длине либо быть сильнее выраженным у носа и хвоста. Это помогает входить в крутую волну, не зарывая нос доски. У доски для повседневного катания середину могут сделать более плоской, чтобы раньше ловить волны и сохранять скорость на пологих участках. На днище могут сочетаться углубление под носом, двойное углубление ближе к хвосту и V-образный участок сзади. Эти формы влияют на скорость и на то, как доска переходит с одного борта на другой. Хвост бывает округло-зауженным, заострённым или сквош; встречаются разные схемы плавников, включая 2+1 и четыре плавника.",
            "diagrams": [
                {
                    "filename": "rocker-bottom-shape.png",
                    "title": "Рокер и контуры днища",
                    "alt": "Боковой профиль high-performance лонгборда с пунктирной базовой линией и тремя связанными поперечными сечениями: неглубокий одинарный конкейв в носу, двойной конкейв в середине и vee в тейле.",
                    "caption": "По сравнению с классическим лонгбордом или noserider, у этой формы больше рокера в носу и тейле, а центральная часть остаётся более плоской и быстрой. Тонкие фойленные рейлы легче входят в поворот и освобождаются из воды. Днище переходит от неглубокого одинарного конкейва под носом к двойному конкейву в середине, затем — к vee в зоне плавников для более быстрой перекладки с рейла на рейл."
                },
                {
                    "filename": "fin-options.png",
                    "title": "Варианты плавников",
                    "alt": "Две схемы кормы лонгборда: 2+1 и пять боксов 4+1.",
                    "caption": "Схема 2+1 сочетает драйв и поворот. Пять боксов позволяют настроить доску как сингл, 2+1, трастер или квад."
                }
            ],
            "ideal": "Подходит сёрферам среднего и продвинутого уровня, которые уверенно управляют лонгбордом с хвоста и свободно перемещаются по доске. Специализированные модели лучше раскрываются на чистых волнах от высоты плеча с достаточно крутой стенкой для поворотов. Более широкие модели с меньшим изгибом подходят и для небольших волн. Такой лонгборд позволяет сочетать быстрое катание вдоль волны, резкие повороты и проходы к носу.",
            "tradeoff": "Более узкая и изогнутая доска обычно позже ловит слабую волну и хуже сохраняет скорость на пологих участках, чем широкий классический или универсальный лонгборд. Она быстрее реагирует на движения сёрфера, поэтому неточные действия сильнее сказываются на ходе. Размер и схема плавников заметно меняют её поведение."
        },
        "ja": {
            "page_title": "ハイパフォーマンス・ロングボード",
            "meta_title": "ハイパフォーマンス・ロングボード — ロングボードの形",
            "meta_description": "ハイパフォーマンス・ロングボードは、シャープなターンやアクティブなライディングを楽しむためのロングボード。波の斜面が急な場面でも、ボードをコントロールしやすいのが特徴です。",
            "title": "パフォーマンス",
            "summary": "絞ったノーズとテール、強めのロッカー。よりタイトなターンと素早い切り返しに向きます。",
            "lead": "ハイパフォーマンス・ロングボードは、シャープなターンやアクティブなライディングを楽しむためのロングボード。波の斜面が急な場面でも、ボードをコントロールしやすいのが特徴です。",
            "overview": [
                "ハイパフォーマンス・ロングボードは、ロングボードの長さを活かしながら、ショートボードのようなアクティブな動きを楽しめるボードです。シャープなターンや素早い切り返しで波の切り立った部分を攻めつつ、ボードの上を歩いたり、ノーズライドを楽しんだりすることもできます。ロングボードを自在に操り、さらにダイナミックなライディングを目指す上級者に向いています。",
                "ハイパフォーマンス・ロングボードには、普段のサーフィンを楽しむためのモデルから、大会での使用を想定したモデルまであります。よく知られたモデルにも、それぞれの楽しみ方に合ったものがそろっています。"
            ],
            "models": [
                {
                    "name": "Firewire Taylor Jensen Pro",
                    "url": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro",
                    "description": "大会での使用を重視したモデル。良い波でスピードに乗り、力強いターンやダイナミックなライディングを楽しめます。",
                    "history": "ダン・マンとテイラー・ジェンセンが開発した競技モデル。ジェンセンはこのボードで世界タイトルを獲得。",
                    "history_source": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro",
                    "dimensions": "9′0″ × 22⅛″ × 2⅝″",
                    "volume": "61 L",
                    "spec_notes": "I-Bolic Volcanic仕様。ノーズコンケーブからテールのダブルコンケーブ、最後はV字へ。",
                    "spec_source": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro"
                },
                {
                    "name": "Firewire Taylor Jensen Pro V",
                    "url": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro-v",
                    "description": "小さな波や力の弱い波でも、普段のサーフィンを楽しむためのモデル。軽快に方向を変えられ、波の緩いセクションでもスピードを保ちやすいのが特徴です。",
                    "history": "ジェンセンとダン・マンが日常の波向けに開発。Firewireは2024年にI-Bolic版を発表。",
                    "history_source": "https://www.firewiresurfboards.com/blogs/news/introducing-the-tj-pro-tj-pro-v",
                    "dimensions": "9′0″ × 22⅛″ × 2⅝″",
                    "volume": "62 L",
                    "spec_notes": "I-Bolic Volcanic仕様。TJ Proより緩い反りと幅広いノーズ、スカッシュテール。",
                    "spec_source": "https://www.firewiresurfboards.com/products/prestige-taylor-jensen-pro-v"
                },
                {
                    "name": "NSP Pro-9",
                    "url": "https://www.nspsurfboards.com/product/surf/pro-9-cse/",
                    "description": "幅広いコンディションでアクティブに乗りたい人に。ゆったりしたトリムやノーズライドから、スピードを活かした力強いターンまで楽しめます。",
                    "history": "ハワイのシェイパー、カール・シェイパーがNSPのために設計。",
                    "history_source": "https://www.nspsurfboards.com/product/technology/cse/pro-9-cse/",
                    "dimensions": "9′1″ × 22″ × 2¾″",
                    "volume": "62.9 L",
                    "spec_notes": "CSE仕様。丸いボトムからV字とダブルコンケーブへ。フィンボックスは五つ。",
                    "spec_source": "https://www.nspsurfboards.com/product/surf/pro-9-cse/"
                },
                {
                    "name": "CJ Nelson Designs GX1000 / Ibis",
                    "url": "https://thunderboltsurf.com/cj-nelson-designs/ibis/",
                    "description": "スピードと軽快な動きを楽しみたい人に。シャープなターンと、ロングボードらしいグライドやノーズライドを組み合わせて乗れます。",
                    "history": "CJ・ネルソンがシェイパーのライアン・イングルと設計。",
                    "history_source": "https://thunderboltsurf.com/cj-nelson-designs/ibis/",
                    "dimensions": "9′0″ × 23″ × 3″",
                    "volume": "66.74 L",
                    "spec_notes": "Ibis：ノーズコンケーブ、2+1フィンボックス。",
                    "spec_source": "https://thunderboltsurf.com/cj-nelson-designs/ibis/"
                },
                {
                    "name": "Kai Sallas Lava Flow",
                    "url": "https://thunderboltsurf.jp/products/lava-flow",
                    "description": "速くパワフルな波で、深いカービングターンやバレルライドを楽しむためのモデル。特に頭からダブルオーバーヘッドの波に向いています。",
                    "history": "ハワイのロングボーダー、カイ・サラスがシェイプ。",
                    "history_source": "https://thunderboltsurf.jp/products/lava-flow",
                    "dimensions": "9′0″ × 22¼″ × 2⅝″",
                    "volume": "61.3 L",
                    "spec_notes": "Thunderbolt Silver仕様。Vボトム、絞ったテール、2+1フィンボックス。",
                    "spec_source": "https://thunderboltsurf.jp/products/lava-flow"
                }
            ],
            "design": "これらのモデルは、伝統的なログよりテールを絞り、薄くエッジの立ったレールを持つものが多く、ターンでレールを入れやすくなっています。ロッカーは、想定する波に合わせて変えます。掘れた波へのテイクオフを想定したモデルでは、ノーズからテールまで滑らかに反らせるか、ノーズとテールの反りを強めることで、ボードが急な斜面に沿いやすくなり、ノーズも刺さりにくくなります。一方、普段使いのモデルでは中央部のロッカーを抑え、波を早くつかみ、緩いセクションでもスピードを保ちやすくすることがあります。ボトムは、浅いノーズコンケーブにダブルコンケーブ、Vee、スパイラルVeeを後ろ足の下で組み合わせることが多く、スピードを生み、左右のレールの切り替えを助けます。ラウンドピン、ピン、スカッシュなど、テールの形によってターンの感触も変わります。フィンも2+1やクアッドなど、さまざまな設定があります。",
            "diagrams": [
                {
                    "filename": "rocker-bottom-shape.png",
                    "title": "ロッカーとボトム形状",
                    "alt": "点線の基準線と三つの断面を備えたハイパフォーマンス・ロングボードの側面図。ノーズの浅いシングルコンケーブ、中央部のダブルコンケーブ、テールのVeeを示す。",
                    "caption": "クラシックやノーズライダーのロングボードと比べると、ノーズとテールのロッカーは強めで、中央部は速さを保つため比較的フラットです。薄くフォイルしたレールは水を捉えやすく、抜けも軽くします。ボトムはノーズ下の浅いシングルコンケーブから、中央部にかけてダブルコンケーブへ移り、フィン周辺ではVeeへ抜けるため、レール・トゥ・レールの切り替えが速くなります。"
                },
                {
                    "filename": "fin-options.png",
                    "title": "フィンの選択肢",
                    "alt": "ロングボードのテールを上から見た二つの図。2+1と5ボックスの4+1を示している。",
                    "caption": "2+1はドライブとピボットのバランスを取ります。5ボックスならシングル、2+1、スラスター、クアッドに調整できます。"
                }
            ],
            "ideal": "テール側からロングボードをコントロールでき、意図して足を置き換えられる中級者から上級者に向いています。専用のHPモデルは、肩からそれ以上のサイズで、はっきりしたフェイス、スピード、ターンを当てるセクションがあるクリーンな波で活きます。ロッカーを抑えた幅広めのデイリーモデルは、小さなビーチブレイクでも使えます。トリムやノーズで過ごす時間と同じくらい、積極的なカービング、リップターン、カットバック、速いダウン・ザ・ラインを重視するときに選ぶ形です。",
            "tradeoff": "反応性は、ボリューム、レール形状、ロッカー、フィンの繊細なバランスから生まれます。幅を残したクラシック型やオールラウンド型と比べると、特化したHPシェイプは力の弱い波ではテイクオフが遅く、波の緩いセクションで速度を保ちにくく、遅れたステップやタイミングのずれを許容しにくい傾向があります。パワーのある波ではスピードが出てレールも鋭くなるため、十分なスペースと確かなコントロールが必要です。サイズやフィン設定によって乗り味も変わります。"
        }
    },
    "glider": {
        "id": "glider",
        "image": "glider",
        "en": {
            "page_title": "Glider",
            "meta_title": "Glider — Longboard shapes",
            "meta_description": "A long, narrow shape designed to build speed and travel a long line across a small wave.",
            "title": "Glider",
            "summary": "A long, narrow plan shape with low rocker, built to carry speed and cover distance on a small wave.",
            "lead": "A long, narrow shape designed to build speed and travel a long line across a small wave.",
            "design": "The extended waterline and low rocker reduce drag once the board is moving. A narrow plan shape keeps the outline efficient and encourages a flowing line rather than repeated direction changes.",
            "ideal": "Choose it for soft, clean waves where carrying speed across flat sections matters more than tight turns or walking to the nose.",
            "tradeoff": "The long, narrow outline needs space and a suitable line to work well. It is less nimble in crowded peaks and can be harder to handle in steep shorebreak."
        },
        "ru": {
            "page_title": "Глайдер",
            "meta_title": "Глайдер — форма лонгборда",
            "meta_description": "Длинная узкая форма, созданная для набора скорости и длинной линии на небольшой волне.",
            "title": "Глайдер",
            "summary": "Длинная узкая доска с небольшим изгибом: легко скользит и сохраняет скорость на пологой волне.",
            "lead": "Длинная узкая форма, созданная для набора скорости и длинной линии на небольшой волне.",
            "design": "Длина и небольшой изгиб помогают доске сохранять скорость. Узкая форма лучше подходит для длинных плавных проездов, чем для частых поворотов.",
            "ideal": "Глайдер особенно хорош на чистых пологих волнах, где важно сохранять скорость между участками с большей силой.",
            "tradeoff": "Длинной узкой доске нужны пространство и ровная линия движения. Среди других сёрферов ей сложнее маневрировать, а в крутом прибое — управлять ею."
        },
        "ja": {
            "page_title": "グライダー",
            "meta_title": "グライダー — ロングボードの形",
            "meta_description": "小波でスピードを生み、長いラインを走るために設計された、長く細い形です。",
            "title": "グライダー",
            "summary": "長く細いアウトラインと穏やかなロッカー。小波でスピードを保ち、長い距離を走るための形です。",
            "lead": "小波でスピードを生み、長いラインを走るために設計された、長く細い形です。",
            "design": "長さと控えめなロッカーがスピードを保ちやすくします。細身のアウトラインは、細かくターンを重ねるよりも、長いラインを滑るスタイルに向いています。",
            "ideal": "フラットなセクションで速度を保つことが大切な、力の弱いきれいな波に向いています。タイトなターンやノーズライディングを優先しないスタイルに適しています。",
            "tradeoff": "長く細いアウトラインを活かすには、スペースと適切なラインが必要です。混雑したピークでは小回りが利きにくく、急なショアブレイクでは扱いが難しくなります。"
        }
    }
}
