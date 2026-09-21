"""Japanese vocabulary and classification labels for the Surf Japan glossary.

English keys are stable across translations.  Japanese terms are displayed
first, followed by the canonical English word and established English aliases.
"""

from glossary_data import TERMS as EN_TERMS


def term(title, definition, aliases=()):
    return {"title": title, "definition": definition, "aliases": aliases}


JA_TERMS = {
    # 波
    "surf": term("砕けた波", "浅い場所でせり上がり、急になって砕けたうねり。", ("サーフ",)),
    "swell": term("うねり", "波を生んだ風から離れて伝わる、まとまりのある波のエネルギー。"),
    "groundswell": term("グラウンドスウェル", "遠くの低気圧が生む、周期の長いうねり。"),
    "wind-swell": term("ウインドスウェル", "近くの風によって生まれる、周期の短い波。"),
    "fetch": term("フェッチ", "波を作るあいだ、風が開けた水面の上を吹く距離。"),
    "wave-period": term("波周期", "連続する波の山と山の間の時間。秒で表す。"),
    "swell-direction": term("うねりの向き", "うねりがどの方角から入るかを示す方位。"),
    "set": term("セット", "続けて入る波のまとまり。セット間の波より大きいことが多い。"),
    "lull": term("セット間の静かな時間", "セットとセットの間にある、波が少ない時間。"),
    "peak": term("ピーク", "波の最も高く、最初にブレイクする部分。"),
    "crest": term("波頂", "まだ砕けていない波の一番上の稜線。"),
    "face": term("フェイス", "ブレイクする波の、開いた斜面。"),
    "lip": term("リップ", "前へせり出し、落ちる波の上端。"),
    "curl": term("カール", "丸く巻きながら砕ける波の部分。"),
    "shoulder": term("ショルダー", "カールから離れた、比較的緩やかで開いた波の部分。"),
    "pocket": term("ポケット", "ブレイクする部分に最も近い、急でパワーのある場所。"),
    "trough": term("波の谷", "波の山と山の間で最も低い部分。"),
    "section": term("セクション", "乗れる、または越える必要がある波の一区画。"),
    "flats": term("フラット", "ブレイクするセクションの前にある、フェイスの平らな部分。"),
    "whitewater": term("ホワイトウォーター", "波が砕けたあとに残る、乱れた白い泡。"),
    "foam-ball": term("フォームボール", "バレルの最も深い部分を動く、密度の高い白波。"),
    "left": term("レフト", "岸から見て、サーファーの左側へブレイクする波。"),
    "right": term("ライト", "岸から見て、サーファーの右側へブレイクする波。"),
    "a-frame": term("Aフレーム", "左右両方へきれいにブレイクするピーク。"),
    "closeout": term("クローズアウト", "全体が同時に崩れ、開いたフェイスを残さない波。"),
    "reform": term("リフォーム", "一度砕けてからまた整い、岸寄りで再びブレイクする波。"),
    "double-up": term("ダブルアップ", "二つの波のエネルギーが重なり、急に立ち上がる波。"),
    "wedge": term("ウェッジ", "波が斜めに交わって生まれる、急でしばしばパワフルなピーク。"),
    "mushy": term("マッシー", "緩く、遅く、比較的パワーの弱い状態。"),
    "hollow": term("ホロー", "砕けるときに管状の空間を作るほど急な波。"),
    "peeling": term("きれいに割れる波", "一度に閉じず、波に沿って順にブレイクする状態。"),
    "spilling": term("スピリング波", "波の山がフェイスをやさしく崩れ落ちる波。"),
    "plunging": term("プランジング波", "リップが前へ投げ出され、力強く砕ける波。"),
    "surging": term("サージング波", "フェイスに沿って割れず、急に盛り上がって岸へ押し寄せる波。"),
    "slab": term("スラブ", "浅い岩棚の上で急に割れる、厚くパワフルな波。"),
    "shore-dump": term("ショアダンプ", "岸際で強く閉じるように割れる波。"),
    "big-wave": term("ビッグウェーブ", "大きく速く、結果の重い波。専門的な判断と装備を要する。"),

    # ブレイクと海底
    "beach-break": term("ビーチブレイク", "砂地またはサンドバーの上で割れるブレイク。"),
    "reef-break": term("リーフブレイク", "リーフ、岩棚など硬い海底の上で割れるブレイク。"),
    "point-break": term("ポイントブレイク", "岬や固定された障害物によって形作られるブレイク。"),
    "rivermouth": term("河口のブレイク", "河口近くのブレイク。サンドバーや流れの道筋が形を作ることが多い。"),
    "shorebreak": term("ショアブレイク", "浅い水深の岸近くで割れる波。"),
    "tidal-bore": term("潮津波", "満ち潮が川の流れにぶつかり、川を遡る波。"),
    "wave-pool": term("ウェーブプール", "サーフィンできる人工波を作る施設。"),
    "sandbar": term("サンドバー", "波を持ち上げてブレイクさせる、盛り上がった砂の帯。"),
    "bank": term("バンク", "ブレイクする波の形を作る、サンドバーなど水中の盛り上がり。"),
    "reef": term("リーフ", "ブレイクする波の下にある、サンゴ、岩などの硬い地形。"),
    "rock-shelf": term("岩棚", "波を急に立ち上がらせることがある、浅い岩の段差。"),
    "cobblestones": term("玉石の海底", "固定された起伏のあるブレイクを作ることがある、海底の丸い石。"),
    "bathymetry": term("海底地形", "ブレイクの下にある海底の形と水深。"),
    "headland": term("岬", "海へ突き出た陸地。ポイントブレイクの形を作ることがある。"),

    # コンディション
    "swell-height": term("うねりの高さ", "地形による変化の前、沖合で予報されるうねりの高さ。"),
    "surf-height": term("ブレイク時の波高", "あるスポットで砕ける波の推定高さ。"),
    "significant-wave-height": term("有義波高", "ある海況で高い方から三分の一の波の平均高さ。"),
    "wave-energy": term("波のエネルギー", "うねりが運ぶ力。特に波高と周期の影響を受ける。"),
    "offshore-wind": term("オフショア", "陸から海へ吹く風。フェイスを開いたまま保つことがある。"),
    "onshore-wind": term("オンショア", "海から陸へ吹く風。波をバタつかせ、緩くしやすい。"),
    "cross-shore-wind": term("サイドショア", "まっすぐのオンショアやオフショアではなく、海岸に沿って吹く風。"),
    "glassy": term("グラッシー", "風の筋がほとんどない、滑らかな水面。"),
    "chop": term("チョップ", "水面にできる短く不規則な風波。"),
    "blown-out": term("風で崩れた状態", "風で乱され、きれいに乗れないほどまとまりを失った状態。"),
    "clean": term("クリーン", "風波が少なく、整った状態。"),
    "tide": term("潮汐", "水深とブレイクの働きに影響する海面の高さの変化。"),
    "high-tide": term("満潮", "潮汐の中で海面が最も高い段階。"),
    "low-tide": term("干潮", "潮汐の中で海面が最も低い段階。"),
    "incoming-tide": term("上げ潮", "海面が上がる潮汐の段階。"),
    "outgoing-tide": term("下げ潮", "海面が下がる潮汐の段階。"),
    "rip-current": term("離岸流", "岸から沖へ向かう、強く狭い水の流れ。", ("リップ",)),
    "sweep": term("横流れ", "海岸に沿って、またはラインナップを横切って動く流れ。"),
    "backwash": term("バックウォッシュ", "岸、岩、壁から跳ね返り、入ってくる波へ向かう水。"),

    # スポットのゾーン
    "lineup": term("ラインナップ", "サーファーが来る波を待ち、位置を取る場所。", ("ラインアップ",)),
    "outside": term("アウトサイド", "主なブレイクゾーンより沖側。"),
    "inside": term("インサイド", "主なラインナップより岸側。波がもう一度割れることが多い。"),
    "impact-zone": term("インパクトゾーン", "波が繰り返し、最も強くブレイクする場所。"),
    "channel": term("チャンネル", "ブレイクを抜ける、より深く穏やかな通り道。沖へパドルするためによく使う。"),
    "takeoff-zone": term("テイクオフゾーン", "波をつかまえるためにサーファーが位置を取る場所。"),
    "paddle-out": term("沖へパドルする", "岸からラインナップへ着くためのルートとパドル。"),
    "caught-inside": term("インサイドに捕まる", "砕ける波を越えてアウトサイドへ出られない状態。"),
    "reading-the-lineup": term("ラインナップを読む", "波、流れ、ほかのサーファーを観察し、どこでいつパドルするか判断すること。"),

    # ボード
    "shortboard": term("ショートボード", "切り返しの速さとパフォーマンス系のマニューバーのための、短く反応の良いボード。"),
    "longboard": term("ロングボード", "早いテイクオフ、トリム、グライドのための長いボード。"),
    "fish": term("フィッシュ", "ボリュームがあり、特徴的なスワローテールを持つ短く幅広いボード。"),
    "groveler": term("グロベラー", "力の弱い小波でもスピードを作るためのパフォーマンスボード。"),
    "egg": term("エッグ", "ショートボードとロングボードの中間にある、丸みを持った万能なミッドレングス形状。"),
    "mid-length": term("ミッドレングス", "一般的なショートボードとロングボードの間の長さのボード。"),
    "mini-mal": term("ミニマリブ", "ロングボードらしい乗り味を、より短く扱いやすくしたボード。"),
    "funboard": term("ファンボード", "ロングボードの乗りやすさとショートボードの操作性をつなぐ、安定した万能ボード。"),
    "log": term("ログ", "伝統的で、たいてい重いシングルフィンのロングボード。"),
    "noserider": term("ノーズライダー", "ノーズ近くで乗るために作られたロングボードの形。"),
    "gun": term("ガン", "速く大きい波のための、長く細いボード。"),
    "glider": term("グライダー", "スピードを保ち、長い距離を走るための長く細いボード。"),
    "soft-top": term("ソフトトップ", "デッキとレールが柔らかいフォーム製のボード。初心者によく使われる。"),
    "alaia": term("アライア", "フィンのない、伝統的なハワイの木製ボード。"),
    "asym": term("アシム", "フロントサイドとバックサイドで異なるように調整された、左右非対称のボード形状。"),
    "bonzer": term("ボンザー", "ドライブとホールドを作る、センターフィンとサイドランナーを使うデザイン。"),
    "pu-polyester": term("PU／ポリエステル", "ポリウレタンフォームとポリエステル樹脂を使う一般的な構造。"),
    "eps-epoxy": term("EPS／エポキシ", "発泡ポリスチレン EPS とエポキシ樹脂を使う構造。"),
    "blank": term("ブランク", "グラッシング前の、形を整えたフォームコア。"),
    "stringer": term("ストリンガー", "強度としなりを出すため、ボードの芯に通す木の帯。"),
    "glassing": term("グラッシング", "グラスクロスと樹脂でボードをラミネートすること。"),
    "outline": term("アウトライン", "上から見た、ノーズからテールまでのレールの曲線。"),
    "nose": term("ノーズ", "サーフボードの前端。"),
    "deck": term("デッキ", "サーフボードの上面。"),
    "tail": term("テール", "サーフボードの後端。"),
    "rails": term("レール", "サーフボードの側面の縁。"),
    "rocker": term("ロッカー", "ノーズからテールへ続くボードの反り。"),
    "volume": term("ボリューム", "ボード内部の容積。通常はリットルで表す。"),
    "length": term("長さ", "ボードのノーズからテールまでの寸法。"),
    "width": term("幅", "片方のレールから反対側のレールまでの寸法。"),
    "thickness": term("厚み", "フォームコアを通るボードの縦方向の寸法。"),
    "bottom-contour": term("ボトムコンツアー", "ボード下面に作られた形状。"),
    "concave": term("コンケーブ", "揚力とスピードを生むことがある、くぼんだボトム形状。"),
    "vee": term("Vee", "ストリンガーから両レールへ向かって下がるボトム形状。"),
    "foil": term("フォイル", "中央からノーズ、テール、レールへ向けて、ボードの厚みがどう細くなるか。"),
    "fin": term("フィン", "ボード下面にある、安定させるための板。", ("スケグ",)),
    "fin-box": term("フィンボックス", "取り外し可能なフィンを固定する、ボード側の受け部。"),
    "single-fin": term("シングルフィン", "中央に一枚のフィンを持つボード。"),
    "twin-fin": term("ツインフィン", "両側に二枚のフィンを持つボード。"),
    "two-plus-one": term("2＋1", "センターフィン一枚と小さなサイドフィン二枚の構成。"),
    "thruster": term("スラスター", "センター一枚とサイド二枚からなる三枚フィンの構成。"),
    "quad": term("クアッド", "センターフィンなしの四枚フィン構成。"),
    "leash": term("リーシュ", "ボードとサーファーをつなぐコード。", ("レッグロープ",)),
    "wax": term("ワックス", "グリップのためにデッキへ塗るコーティング。"),
    "traction-pad": term("トラクションパッド", "たいてい後ろ足の下に付ける、凹凸のあるフォームパッド。"),
    "ding": term("ディング", "サーフボードの表面または構造の損傷。"),
    "ding-repair": term("ディングリペア", "水がフォームコアへ入る前に、損傷を塞いで直すこと。"),

    # 乗り方とスタイル
    "shortboarding": term("ショートボード・サーフィン", "素早い方向転換とパフォーマンス系マニューバーを中心にした乗り方。"),
    "longboarding": term("ロングボード・サーフィン", "グライド、トリム、足運び、流れを大切にする乗り方。"),
    "traditional-longboarding": term("トラディショナル・ロングボーディング", "滑らかな足運び、トリム、ノーズライディングを重視する古典的なアプローチ。", ("クラシック・ロングボーディング", "ロギング")),
    "high-performance-longboarding": term("ハイパフォーマンス・ロングボーディング", "鋭いターンとダイナミックなマニューバーをより重視するロングボーディング。"),
    "power-classic": term("パワークラシック", "クラシックな足運びと、より力強く現代的なターンを合わせたスタイル。"),

    # テクニックとマニューバー
    "paddling": term("パドリング", "左右交互の腕のストロークでサーフボードを進めること。"),
    "takeoff": term("テイクオフ", "波をつかまえ、ライディング姿勢へ立ち上がること。", ("ポップアップ",)),
    "angled-takeoff": term("アングルド・テイクオフ", "すでにフェイスに沿って進むよう、斜めから波へ入ること。"),
    "duck-dive": term("ドルフィンスルー", "沖へ出るとき、来る波の下へボードと体を沈めて通すこと。", ("ダックダイブ",)),
    "turtle-roll": term("タートルロール", "ロングボードの下で逆さになり、来る波の下を通すこと。"),
    "trim": term("トリム", "ボードを効率よく走らせる、バランスの取れたラインを走ること。"),
    "pump": term("パンピング", "フェイスを上下して、スピードを作るまたは保つこと。"),
    "stall": term("ストール", "セクションを待つ、またはバレルに留まるために意図して減速すること。"),
    "fade": term("フェード", "ダウンザラインへ向かう前に、いったんブレイクする側へ向けて入ること。"),
    "bottom-turn": term("ボトムターン", "波の下部で行い、ボードをフェイスへ向け直すターン。"),
    "carve": term("カーブ", "レールを使って大きく弧を描くターン。"),
    "cutback": term("カットバック", "ダウンザラインへ進んだあと、ブレイクする側へ戻るターン。"),
    "top-turn": term("トップターン", "フェイスの上部、リップ近くで行うターン。"),
    "snap": term("スナップ", "波の上部での素早く鋭い方向転換。"),
    "floater": term("フローター", "砕けるセクションの上を走り、フェイスへ戻るマニューバー。"),
    "re-entry": term("リエントリー", "リップに当て、すぐにフェイスへ戻るマニューバー。"),
    "off-the-lip": term("オフザリップ", "砕けるリップからボードをフェイス下へ戻すマニューバー。"),
    "aerial": term("エア", "フェイスを離れ、再びフェイスへ着地すること。", ("エアリアル",)),
    "air-reverse": term("エアリバース", "回転し、ボードが一時的に逆向きになる着地をするエア。"),
    "grab": term("グラブ", "空中でボードのレールをつかむこと。"),
    "barrel": term("バレル", "ブレイクする波の内側にできる空洞。", ("チューブ",)),
    "barrel-riding": term("バレルライディング", "ブレイクする波の空洞の中を走ること。"),
    "backdoor": term("バックドア", "ブレイクするセクションの後ろからテイクオフし、チューブの開いた部分へ入ること。"),
    "doggy-door": term("ドギードア", "バレルから抜ける小さな出口。"),
    "kick-out": term("キックアウト", "波の裏側またはリップを越えてライディングを終えること。"),
    "cross-step": term("クロスステップ", "片足をもう一方の足の前へ滑らかに運び、ロングボードの上を歩くこと。"),
    "noseriding": term("ノーズライディング", "ロングボードの前方部分で乗ること。"),
    "hang-five": term("ハングファイブ", "ボード前端から五本の足指を出して行うノーズライディング。"),
    "hang-ten": term("ハングテン", "両足をノーズへ置き、十本すべての足指を前端から出すノーズライディング。"),
    "bail": term("ベイル", "転倒や危険を避けるため、ボードから離れること。"),
    "wipeout": term("ワイプアウト", "ライディング中またはテイクオフ中にボードから落ちること。"),
    "pearling": term("ノーズが刺さる", "ボードのノーズを水へ突っ込み、バランスを失うこと。"),
    "over-the-falls": term("リップに巻かれる", "リップを越え、砕ける波と一緒に落とされること。"),

    # スタンスと上達
    "regular-foot": term("レギュラースタンス", "左足を前にして乗るスタンス。"),
    "goofy-foot": term("グーフィースタンス", "右足を前にして乗るスタンス。"),
    "frontside": term("フロントサイド", "胸を波へ向けて乗ること。"),
    "backside": term("バックサイド", "背中を波へ向けて乗ること。"),
    "switch-stance": term("スイッチスタンス", "普段とは反対の足を前にして乗ること。"),
    "down-the-line": term("ダウンザライン", "波が割れる方向へ、開いたフェイスに沿って走ること。"),
    "beginner": term("ビギナー", "水の状況、パドリング、テイクオフの基礎を身につけている段階のサーファー。"),
    "intermediate": term("中級者", "割れていない波をつかまえ、フェイスに沿って走れるサーファー。"),
    "advanced": term("上級者", "より難しい条件で、迷いのないマニューバーを行えるサーファー。"),
    "expert": term("エキスパート", "複雑でリスクの高い条件を判断し、対応できる経験豊かなサーファー。"),
    "whitewater-practice": term("ホワイトウォーターでの練習", "まだ割れていないグリーンウェーブではなく、すでに割れた波で学ぶこと。"),
    "green-wave": term("グリーンウェーブ", "ホワイトウォーターになる前の、乗ることができる割れていないフェイス。"),

    # 安全とエチケット
    "priority": term("優先権", "波に乗る権利。一般に、ピークに最も近く深い位置にいるサーファーが持つ。", ("ライト・オブ・ウェイ",)),
    "drop-in": term("ドロップイン", "すでに別のサーファーが取った、または乗っている波へ入ること。", ("バーン",)),
    "snaking": term("スネーキング", "ほかのサーファーの内側へ回り込み、波を取ること。"),
    "party-wave": term("パーティーウェーブ", "ふつうは合意の上で、複数のサーファーが共有する波。"),
    "loose-board": term("流れたボード", "手放され、水中でほかの人を危険にさらすボード。"),
    "cleanup-set": term("クリーンアップセット", "さらに沖で割れ、ラインナップ全体を通過する大きめのセット。"),
    "hold-down": term("ホールドダウン", "砕ける波の力で水中に留められること。"),
    "local-rules": term("ローカルルール", "特定のサーフスポットで公表されている、または慣習となっている規則。"),

    # 文化、セッションの言葉、単位
    "dawn-patrol": term("ドーンパトロール", "夜明けに行うサーフセッション。"),
    "quiver": term("クイバー", "異なる波とコンディションのために持つ、サーファーのボードの組み合わせ。"),
    "firing": term("ファイアリング", "非常に良く、クリーンでパワフルな波の状態。"),
    "flat": term("フラット", "乗れる波がない海の状態。"),
    "corduroy": term("コーデュロイ", "岸へ近づく、均等で平行なうねりのライン。"),
    "mysto-spot": term("ミストスポット", "あまり知られていない、または意図して場所を明かさないサーフスポット。"),
    "stoked": term("ストークト", "サーフィンに興奮し、満足していること。"),
    "froth": term("フロス", "サーフィンに対する先走った熱意。"),
    "gnarly": term("ナーリー", "激しい、難しい、または圧倒的にすごいこと。"),
    "shacked": term("シャックト", "バレルの深いところにいること。"),
    "hang-loose": term("ハングルース", "リラックスした、友好的な姿勢を表すハワイの言葉。"),
    "foot": term("フィート", "ボードや波の寸法によく使う長さの単位。", ("ft",)),
    "inch": term("インチ", "ボード寸法に使う小さな長さの単位。", ("in",)),
    "litre": term("リットル", "サーフボードのボリュームに使う標準的な単位。", ("L",)),
    "knot": term("ノット", "海上予報で使う風速の単位。", ("kt",)),
    "wave-height": term("波高", "波について示される高さ。どの測り方かを常に確認する必要がある。"),
}


TREE = [
    {"id": "waves", "title": "波", "note": "波が生まれ、割れ、乗れるフェイスになるまで。", "groups": [
        ("うねりと波の形成", ["surf", "swell", "groundswell", "wind-swell", "fetch", "wave-period", "swell-direction", "set", "lull"]),
        ("波の構造", ["peak", "crest", "face", "lip", "curl", "shoulder", "pocket", "trough", "section", "flats", "whitewater", "foam-ball"]),
        ("形とブレイクの仕方", ["left", "right", "a-frame", "closeout", "reform", "double-up", "wedge", "mushy", "hollow", "peeling", "spilling", "plunging", "surging", "slab", "shore-dump", "big-wave"]),
    ]},
    {"id": "breaks", "title": "サーフブレイク", "note": "波をブレイクさせる場所と、水中の地形。", "groups": [
        ("ブレイクの種類", ["beach-break", "reef-break", "point-break", "rivermouth", "shorebreak", "tidal-bore", "wave-pool"]),
        ("海底と海岸線", ["sandbar", "bank", "reef", "rock-shelf", "cobblestones", "bathymetry", "headland"]),
    ]},
    {"id": "conditions", "title": "サーフコンディション", "note": "その日のブレイクの働きを決める、予報と海況の要素。", "groups": [
        ("うねりと予報", ["swell-height", "surf-height", "significant-wave-height", "wave-period", "swell-direction", "wave-energy"]),
        ("風と水面", ["offshore-wind", "onshore-wind", "cross-shore-wind", "glassy", "chop", "blown-out", "clean"]),
        ("潮と流れ", ["tide", "high-tide", "low-tide", "incoming-tide", "outgoing-tide", "rip-current", "sweep", "backwash"]),
    ]},
    {"id": "spots-zones", "title": "スポットと水面のゾーン", "note": "ブレイクとそこにいる人の中で、サーファーが使う共通の地図。", "groups": [
        ("水面のゾーン", ["lineup", "outside", "inside", "impact-zone", "channel", "takeoff-zone"]),
        ("沖へのルート", ["paddle-out", "caught-inside", "reading-the-lineup"]),
    ]},
    {"id": "surfboards", "title": "サーフボード", "note": "ボードの系統、構造、デザイン、フィン、そして使い続けるための装備。", "groups": [
        ("ボードの種類と形", ["shortboard", "longboard", "fish", "groveler", "egg", "mid-length", "mini-mal", "funboard", "log", "noserider", "gun", "glider", "soft-top", "alaia", "asym", "bonzer"]),
        ("構造と素材", ["pu-polyester", "eps-epoxy", "blank", "stringer", "glassing"]),
        ("ボードの構成とデザイン", ["outline", "nose", "deck", "tail", "rails", "rocker", "volume", "length", "width", "thickness", "bottom-contour", "concave", "vee", "foil"]),
        ("フィンとフィンセッティング", ["fin", "fin-box", "single-fin", "twin-fin", "two-plus-one", "thruster", "quad"]),
        ("アクセサリーと手入れ", ["leash", "wax", "traction-pad", "ding", "ding-repair"]),
    ]},
    {"id": "ways-of-riding", "title": "乗り方", "note": "ボードを起点にした乗り方と、二つの主なロングボードのスタイル。", "groups": [
        ("ボードを起点にした乗り方", ["shortboarding", "longboarding"]),
        ("ロングボードのスタイル", ["traditional-longboarding", "high-performance-longboarding", "power-classic"]),
    ]},
    {"id": "techniques", "title": "テクニックとマニューバー", "note": "波へ入り、スピードを見つけ、ラインを変え、ライディングを終えるための動き。", "groups": [
        ("波へ入る・沖へ出る", ["paddling", "takeoff", "angled-takeoff", "duck-dive", "turtle-roll"]),
        ("スピードとライン", ["trim", "pump", "stall", "fade", "bottom-turn"]),
        ("ターンとリップ", ["carve", "cutback", "top-turn", "snap", "floater", "re-entry", "off-the-lip"]),
        ("エアとチューブ", ["aerial", "air-reverse", "grab", "barrel", "barrel-riding", "backdoor", "doggy-door", "kick-out"]),
        ("ロングボードの足運び", ["cross-step", "noseriding", "hang-five", "hang-ten"]),
        ("転倒と退出", ["bail", "wipeout", "pearling", "over-the-falls"]),
    ]},
    {"id": "orientation", "title": "スタンス、方向、位置", "note": "サーファーと波がどちらを向き、どちらへ進むかを表す言葉。", "groups": [
        ("スタンス", ["regular-foot", "goofy-foot", "switch-stance"]),
        ("波の上での方向", ["frontside", "backside", "left", "right", "down-the-line"]),
    ]},
    {"id": "progression", "title": "レベルと上達", "note": "サーファーの経験と、学ぶ準備ができた波を表す、公式ではない便利な説明。", "groups": [
        ("経験", ["beginner", "intermediate", "advanced", "expert"]),
        ("練習に向く波", ["whitewater-practice", "green-wave"]),
    ]},
    {"id": "safety-etiquette", "title": "安全とエチケット", "note": "優先権、共有する空間、落ち着いた判断が必要なリスクについての言葉。", "groups": [
        ("ラインナップを共有する", ["priority", "drop-in", "snaking", "party-wave", "loose-board"]),
        ("危険と判断", ["cleanup-set", "hold-down", "local-rules"]),
    ]},
    {"id": "culture-language", "title": "文化、セッションの言葉、単位", "note": "セッションで使う表現、サーフスラング、予報やボードラックで見る単位。", "groups": [
        ("セッションの言葉", ["dawn-patrol", "quiver", "firing", "flat", "corduroy", "mysto-spot"]),
        ("サーフスラング", ["stoked", "froth", "gnarly", "shacked", "hang-loose"]),
        ("単位", ["foot", "inch", "litre", "knot", "wave-height"]),
    ]},
]


def localized_terms():
    """Combine Japanese text with stable English links and aliases."""
    if set(JA_TERMS) != set(EN_TERMS):
        missing = set(EN_TERMS) ^ set(JA_TERMS)
        raise ValueError(f"Japanese glossary keys are out of sync: {sorted(missing)}")
    result = {}
    for key, english in EN_TERMS.items():
        japanese = JA_TERMS[key]
        aliases = tuple(dict.fromkeys((*japanese["aliases"], english["title"], *english["aliases"])))
        result[key] = {**english, **japanese, "aliases": aliases}
    return result
