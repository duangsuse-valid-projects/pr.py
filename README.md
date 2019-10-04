# pr.py

Simple utility generating random Chinese text

## Sample

```bash
$ ~/Projects/pr.py% ./pr.py 
Read File sao.txt costs 0.07763399980831309ms
  chr   n
0   ，  86
1   的  76
2   。  49
3   一  31
4   是  30
5  \n  26
6   着  20
7   ；  20
8   了  19
9   这  18
                n
count  474.000000
mean     2.978903
std      6.590689
min      1.000000
25%      1.000000
50%      1.000000
75%      2.000000
max     86.000000
Count Char Freq of length 1412(27 lines) costs 0.020307957000113674s
```

> Be quiet

```
args += -q | --quiet
```

> Don't show word class by default

```
args += --no-word-class | -nwc
```

> Limit line generation

```
args += --line-max n
```

> Use file for text input (`-` means `/dev/stdin`)

```
args += --file path | -f path
```

### Generation Loop

```bash
~/Projects/pr.py% python3 pr.py loop -nwc --line-max 10 -llen 1 -rlen 1
Read File sao.txt costs 0.06807299996580696ms
  chr   n
0   ，  86
1   的  76
2   。  49
3   一  31
4   是  30
5  \n  26
6   着  20
7   ；  20
8   了  19
9   这  18
                n
count  474.000000
mean     2.978903
std      6.590689
min      1.000000
25%      1.000000
50%      1.000000
75%      2.000000
max     86.000000
Count Char Freq of length 1412(27 lines) costs 0.015024187000108213s
==      Char Based      ==
，的。一是
着；了这子有里月上不也在荷塘人莲叶地我光树像采路些过处可花如而天晚高好个色水然想见出曲以又时静今起们已歌去小杨柳和没却很淡只爱热闹下什么都风远声流但—影头样儿门折白少面多道阴片自到便要事说女层中星来清与般雾轻为睡低得约南船几心忽日走满另渐笑妻迷糊眠悄大带条更四许蓊郁旁知名森虽还己独茫觉定现 受用无边香田亭点开打粒碧缕仿佛似候动传那肩并密底脉住能薄照楞弯近最将重漏看烟隐江早年荡季节《》：于七颇宁院坐乘凉总该番吧亮升墙外马孩欢经听屋拍闰⑴哼披衫沿煤屑幽僻夜加寂寞长⑵字怕背手踱⑶超平常世界冷群居苍由做话理妙且弥望⑷⑸舞裙间零缀袅娜⑹羞涩朵正明珠刚浴美微送楼渺丝颤闪电霎本挨宛凝波痕⑺遮颜致⑻泻青浮牛乳洗笼纱梦云所朗恰酣固别味隔丛生灌木落参差斑驳黑峭鬼稀疏倩画均匀谐旋律梵婀玲⑼奏围段空隙特留例乍团丰姿⑽辨梢山意罢缝两灯精渴眼数蝉蛙它情旧俗乎就六朝盛从诗略她唱艳梁元帝赋妖童媛⑾舟鷁首⑿徐回兼羽杯⒀棹⒁移藻挂欲萍尔其纤腰束素⒂迁延顾步⒃夏始春余嫩初恐沾裳浅畏倾敛裾⒄当嬉游景真趣惜福消记西洲句秋弄若算“”行令惦猛抬前推进息熟久九二北京华园
Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
Loading model cost 0.557 seconds.
Prefix dict has been built succesfully.
                                                words  line_len  word_len_sum  word_len_avg
0   [这, 几天, 心里, 颇, 不, 宁静, 。, 今晚, 在, 院子, 里, 坐, 着, 乘...       114            76      1.500000
1                                                  []         0             0      0.000000
2   [沿着, 荷塘, ，, 是, 一条, 曲折, 的, 小, 煤屑, 路, 。, 这是, 一条,...       116            77      1.506494
3                                                  []         0             0      0.000000
4   [路上, 只, 我, 一个, 人, ，, 背着手, 踱, ⑶, 着, 。, 这, 一片, 天...       154           114      1.350877
5                                                  []         0             0      0.000000
6                                              [荷塘月色]         4             1      4.000000
7   [荷塘月色, 曲曲折折, 的, 荷塘, 上面, ，, 弥望, ⑷, 的, 是, 田田, ⑸,...       227           150      1.513333
8                                                  []         0             0      0.000000
9   [月光, 如, 流水, 一般, ，, 静静地, 泻, 在, 这, 一片, 叶子, 和, 花,...       205           138      1.485507
10                                                 []         0             0      0.000000
11  [荷塘, 的, 四面, ，, 远远近近, ，, 高高低低, 都, 是, 树, ，, 而, 杨...       182           118      1.542373
12                                                 []         0             0      0.000000
13  [忽然, 想起, 采莲, 的, 事情, 来, 了, 。, 采莲, 是, 江南, 的, 旧俗,...       121            81      1.493827
14                                                 []         0             0      0.000000
15  [于是, 妖童媛, 女, ⑾, ，, 荡舟, 心许, ；, 鷁, 首, ⑿, 徐回, ，, ...        79            53      1.490566
16                                                 []         0             0      0.000000
17  [可见, 当时, 嬉游, 的, 光景, 了, 。, 这, 真是, 有趣, 的, 事, ，, ...        34            22      1.545455
18                                                 []         0             0      0.000000
19           [于是, 又, 记起, ，, 《, 西洲, 曲, 》, 里, 的, 句子, ：]        16            12      1.333333
20                                                 []         0             0      0.000000
21  [采莲, 南塘, 秋, ，, 莲花, 过, 人头, ；, 低头, 弄, 莲子, ，, 莲子,...        24            15      1.600000
22                                                 []         0             0      0.000000
23  [今晚, 若有, 采莲人, ，, 这儿, 的, 莲花, 也, 算, 得, “, 过, 人头,...        96            64      1.500000
24                                                 []         0             0      0.000000
25                         [一九二七年, 七月, ，, 北京, 清华园, 。]        14             6      2.333333
26                                                 []         0             0      0.000000
         line_len  word_len_sum  word_len_avg
count   27.000000     27.000000     27.000000
mean    51.333333     34.333333      0.896115
std     72.852855     49.106634      1.007903
min      0.000000      0.000000      0.000000
25%      0.000000      0.000000      0.000000
50%      4.000000      1.000000      1.333333
75%    105.000000     70.000000      1.503247
max    227.000000    150.000000      4.000000
Split Lines into Jieba Words costs 0.5901449259999936s
Statics for Words costs 0.6573179998667911ms
==      Lexical Based   ==
，的。是；了也在着这里叶子荷塘我有树像地月光一个人又采莲今晚路杨柳却只爱热闹上什么都过而但—不和一些没有很一片可以花流水忽然想起满月另门一条这是白天四面一旁些知道路上有些好虽然淡淡的自己到独处一定事现 月色荷塘月色高仿佛这时候与去便不能见如一般像是最将烟雾江南采莲人季节《》：于是莲花人头莲子几天心里颇宁静院子坐乘凉日日走过光里总该一番样子吧月亮渐渐升高墙外马路上孩子们欢笑已经听不见妻在屋里拍闰儿⑴迷迷糊糊哼眠歌悄悄地披大衫带上出去沿着曲折小煤屑幽僻少人走夜晚更加寂寞长着许多蓊蓊郁郁⑵名字晚上阴森森怕人还是背着手踱⑶天地好像超出平常世界冷静群居苍茫月下想不想便觉个自由要做要说的话可不理妙处我且受用无边荷香曲曲折折上面弥望⑷田田⑸出水亭亭舞女裙层层中间零星点缀着白花袅娜⑹地开羞涩打着朵儿正如一粒粒明珠如碧天星星如刚出浴美人微风过处送来缕缕清香远处楼上渺茫歌声似的一丝颤动闪电般霎时传那边本是肩并肩密密挨着宛然一道凝碧波痕底下脉脉⑺遮住颜色更风致⑻静静地泻薄薄的青雾浮起牛乳中洗一样笼轻纱梦天上一层云所以朗照以为这恰好处酣眠固不可少小睡别有风味隔照过来高处丛生灌木落下参差斑驳黑影峭楞楞如鬼弯弯的稀疏倩影画荷叶塘中并均匀光与影有着和谐旋律梵婀玲⑼上奏名曲远远近近高高低低多这些重重围住小路漏着几段空隙特为留下树色一例阴阴的乍看一团丰姿⑽辨得出树梢隐隐约约一带远山大意罢了缝里漏一两点灯光没精打采渴睡眼要数树上蝉声水里蛙声它们事情来旧俗似乎早就六朝时为盛从诗歌约略少年女子她们荡小船唱艳歌不用说很多还有看那风流梁元帝采莲赋说得好妖童媛女⑾荡舟心许鷁首⑿徐回兼传羽杯⒀棹⒁移而藻挂船欲动而萍开尔其纤腰束素⒂迁延顾步⒃夏始春余叶嫩花初恐沾裳浅笑畏倾船而敛裾⒄可见当时嬉游光景真是有趣可惜我们早已无福消受记起西洲曲句子南塘秋低头弄清如水若有这儿算得“”不见影子不行这令到底惦着这样想着猛一抬头不觉已门前轻轻地推进去声息妻已睡熟好久一九二七年七月北京清华园
==      Autosplit       ==
Generate a Mess Using 451 words, 9 seps costs 1.910174999920855ms
白天鷁峭北京弯弯的好超出几段？月！徐回得在 静静地阴阴的很低头清香棹眠可惜的鷁踱。：些出浴特为浅笑妻在夜晚它们我们星星了朗照。⑽。荷香袅娜本是苍茫蓊蓊郁郁一层；平常妖童媛又曲浮起中洗句子这是好可见一粒自由那边月色看苍茫我吧：《不理叶嫩有着超出

抬头旧俗！她们顾步天上采莲赋那边罢了现要说 那边平常缕缕挂；更长着很多树色几段荷塘牛乳些另想着带上渐渐路上纤腰但一旁远山我叶嫩、”但不能…地开斑驳莲花倩影到一道…迷迷糊糊真是莲花曲遮住…高处留下它们：这恰蓊蓊郁郁进去走过丰姿荡⒀与、一个过处句子漏一粒
已都，乘凉想一团“倾船影子惦着…兼几天七月艳歌无福消受棹有月色；很多漏着稀疏蓊蓊郁郁爱莲子坐斑驳有着斑驳爱；小，许多。闰儿嬉游这令淡淡的脉脉荷塘月色的话荷塘月色便觉梵婀玲顾步~们日日热闹虽然夜晚。仿佛！夏始渴睡有着隔！多斑驳⑿阴阴的。吧夏始清如水做四面漏畏闰儿、睡熟是另稀疏微风别有风味颜色一道忽然自由沿着舞女她们约略？上面迷迷糊糊顾步

不见我们
几天风致长着⑸密密今晚月光马路上阴森森有着：美人忽然却蓊蓊郁郁⒂过传羽杯低头缕缕却便北京什么牛乳树当时歌上听不见嬉游一团；从可见而萍蛙声夏始要说另！荷香兼不可独处走参差样子。而敛我们出水这是？踱一个独处！清如水平常牛乳和谐不可，《苍茫她们轻轻地可惜；女子盛高高低低淡淡的荷塘背着手一般这时候走又”而萍受用一层风流~烟雾出去；若有好处顾步一例光与影满月，自由徐回什么好：几段幽僻…高听不见一粒是一些兼小路样子几天一番缕缕听不见出浴阴阴的薄薄的走过~—她们裾“着的话和谐！天上：背着手渺茫

得出打着知道月，影子很多艳歌蓊蓊郁郁：宁静零星院子有着可以推杨柳四面南塘清如水上面句子出浴；笼一番歌去心里是轻纱中间从…乘凉总该嬉游荷塘~艳歌如有趣梁元帝黑影超出而轻纱其踱好处女、妻在固远处的抬头所以特为迷迷糊糊裾抬头打着采莲多出去出去大意披，欢笑美人均匀坐留下已而敛一条荡⑴树上不行脉脉一团墙外许多漏着牛乳；烟雾阴森森了她们顾步不七月小一般颜色斑驳推多小船中洗稀疏远处⑻出浴，要小路！少移而藻也！灯光~从走没精打采可并一番事情漏？青雾

Read WordType Dict costs 0.4244276440003887s
==      Word Kinds      ==
l / j / c / ug / i / nr / s / uz / mq / q / uv / tg / ng / b / vq / m / u / nz / nt / df / y / n / ul / g / mg / vi / rz / f / nrfg / rg / rr / ad / ud / dg / a / t / h / an / r / zg / o / vg / uj / vd / p / x / ns / ag / z / nrt / d / v / k / e / vn
Generate Dict by WordKinds costs 0.22908099981577834ms
a*20 | ad*1 | ag*0 | an*0 | b*1 | c*11 | d*31 | df*0 | dg*0 | e*0 | f*7 | g*1 | h*0 | i*3 | j*2 | k*1 | l*6 | m*22 | mg*0 | mq*1 | n*79 | ng*0 | nr*13 | nrfg*0 | nrt*0 | ns*9 | nt*0 | nz*1 | o*0 | p*4 | q*5 | r*17 | rg*0 | rr*0 | rz*0 | s*10 | t*11 | tg*1 | u*2 | ud*1 | ug*1 | uj*1 | ul*1 | uv*1 | uz*1 | v*86 | vd*0 | vg*2 | vi*0 | vn*0 | vq*0 | x*0 | y*3 | z*16 | zg*3 | ~*1 | …*1 | 、*1 | 。*1 | ！*1 | ，*1 | ：*1 | ；*1 | ？*1
Got 349054 / 349047 in 55 classes
==      Smart   ==
{'p': ['h', 'tg', 't', '*ns'], 'tg': ['p', 'h'], 't': ['p', 'h'], 'an': ['nr', 'uj', 'v', 'v', 'vn', 'vd', 'v', 'vg', 'd', '，', '。'], 'ns': ['nr', 'uj', 'v', 'v', '：', '；'], 'nt': ['nr', 'uj', 'v', 'v'], 'nr': ['nr', 'uj', 'v', 'v', 'r', 'r', 'q', 'v', 'v', 'vn', 'vd', 'v', 'vg', 'uj', 'vn', 'vd', 'v', 'vg', 'k', '：', '；', 'u', 'uz'], 'nx': ['nr', 'uj', 'v', 'v'], 'nz': ['nr', 'uj', 'v', 'v'], 'n': ['nr', 'uj', 'v', 'v', 'zg', 'ag', 'an', 'a', 'ad', 'k'], 'ng': ['nr', 'uj', 'v', 'v'], 'vn': ['nr', 'uj', 'v', 'v', 'an', 'ns', 'nt', 'nr', 'nx', 'nz', 'n', 'ng', 'vn', 'nr', 'r', 'rg', 'uj', '：', '；', 'n', 'n', 'n'], 'zg': ['nt', 'e', '！', '…', '。', '。'], 'z': ['an', 'ns', 'nt', 'nr', 'nx', 'nz', 'n', 'ng', 'vn', '！', '…'], 'ad': ['ag', 'an', 'a', 'ad', 'v', 'v', 'vn', 'vd', 'v', 'vg', 'v', 'ad', 'dg', 'vd', 'd'], 'ag': ['vn', 'vd', 'v', 'vg', 'd', 'q'], 'a': ['vn', 'vd', 'v', 'vg'], 'vd': ['an', 'ns', 'nt', 'nr', 'nx', 'nz', 'n', 'ng', 'vn', 'nr', 'r', 'rg', 'uj', '：', '；', 'v'], 'v': ['an', 'ns', 'nt', 'nr', 'nx', 'nz', 'n', 'ng', 'vn', 'nr', 'r', 'rg', 'uj', '：', '；', 'ud', 'ud', 'ud'], 'vg': ['an', 'ns', 'nt', 'nr', 'nx', 'nz', 'n', 'ng', 'vn', 'nr', 'r', 'rg', 'uj', '：', '；'], 'k': ['d', 'e', '。', '…', '！', '~', '？'], 'h': ['nr', 'r', 'rg', 'i', 'l', 'j', 'u', 'uz'], 'r': ['vn', 'vd', 'v', 'vg', 'k', '：', '；', 'u', 'uz'], 'rg': ['vn', 'vd', 'v', 'vg', 'k', '：', '；', 'u', 'uz'], 'u': ['：', '；', 'k'], 'uz': ['：', '；', 'k'], 'ul': ['：', '；', '。', '…', '！', '~', '？'], 'b': ['vn', 'vd', 'v', 'vg'], 'dg': ['v'], 'd': ['v', 'v', '：', '；', '：', '；', '。', '…', '！', '~', '？'], 'f': ['vn', 'vd', 'v', 'vg'], 'df': ['e', 'e'], 'ug': ['uj'], 'uj': ['n', '…'], 'mq': ['ns']} {'c': ['：', '；'], 'mq': ['r']}
nr/zg/vn/a/v/n/o/m/uz/y/df/mq/an/vq/rz/e/nrt/t/ud/ns/b/s/ul/z/p/nrfg/j/nz/mg/dg/uv/rg/tg/k/q/rr/r/c/ug/d/ng/x/l/ad/ag/h/uj/g/vi/vd/i/nt/f/vg/u/>

们。特为：不用说密密若有没有得清华园阴森森屋里固有些着们树自己畏纤腰密密密密独处：地星星弄群居裾！女一片峭走过莲子密密披它们：得黑影女子们？宁静这儿更！苍茫“很。平常⑷们最；于是上畏那正如光与影浅笑畏：这恰密密唱上畏光景升高：着

我着；过的…波痕想着得点缀着⑿密密也…朵儿着：颇。现从而了；很…清如水很…密密特为；开晚上从现与现沿着现在今晚歌声遮住浅笑不能大意：而弥望小睡出去牛乳我们：现淡淡的星星隔荷塘；别有风味 乍看上面眠小开北京的…可以粒煤屑美人鷁水里，女子

着们。过处可得当时沿着当时来弥望底下叶嫩不能的旧俗密密坐；的天地要最：棹约略平常⒄还有灌木平常拍星星欢笑星星辨的背着手人头们！以为畏只；。缕缕…朵儿所以浅笑畏留下孩子杨柳的话：长着密密春余小睡不行牛乳光与影遮住得拍得好久路上灯光密密不用说超出；重重围住什么的话：现上眠坐那似的；。季节踱另们？棹的缝里们~看它们
眠一两点
见有些到底！些现事情的小眠阴森森的话；很泻星星超出今晚它们着；江南的…个坐得四面荷塘月色；地从霎时沿着群居有得四面西洲辨这令少推得浅笑的…女畏：兼辨得过的…泻；踱西洲：密密畏好久罢了似的；星星浅笑另们~而像是轻纱裾⑴冷静无边。想着乍看中间渴睡人头们！坐得畏宛然的季节高底下北京辨轻纱荡舟多的荷香自由她们而重重围住棹蝉声见西洲有着女子密密不理：来这样似的：高处落下丛生宛然有趣平常艳歌密密眠烟雾稀疏约略不行：曲梵婀玲名字的煤屑热闹眠杨柳；罢了⒄的裙事情小船

眠树色丛生受用一般⑻密密中间推星星丛生着：了！现沿着现在现莲子漏特为荡舟；北京丛生要说照过来；事密密照过来；了：丛生清香树几段羞涩不见空隙听不见一样南塘超出得裾。缕缕！一样：天上们~送来江南；地月光我们踱杨柳我们小可北京看得现到：⑻的笼落下另似乎~这样远远近近自由畏阴森森畏阴森森可惜江南丛生畏与少年妻在高薄薄的田田丰姿挂不见浅笑浅笑们！四面荷塘；地地已经…远远近近束素爱》们？得似的们~四面荷塘的光景的峭去一九二七年

Generated 9 lines costs 6.84676099990611ms
>(EOF)>你好世界
你好(l)世界(n)
```

## Default Data

### Meta(shorthand) dictionary <sub>-metadict</sub>

```python
metawordclz_code = '''
*r r rg nr
*n n nr ns nt nx nz vn an ng
*v v vg vd vn
*a a ag ad an
*d d dg ad vd
*c c
*fuz b bg
*emo e o y
*pha i l j
*z z
*p p
*pre h
*u u uz
*suf k
*e e
*plac f ns s
*m m mg
*qual q
*time t tg
*misc w x
*符 ， 、 。 ！ ？ ~ ： ； …
*中符 ， 、
*介符 ： ；
*后符 。 ！ ？ ~ …
'''
```

### Normal wordclass route <sub>-route-a</sub>

```python
semt_succeeder_code = '''
*p *pre *time
*time *p *pre
*p *ns
*n nr uj v v
n zg *a k
nr r r q
zg nt *e
z *n
ad *a v v
*a *v
*v *n *r uj *介符
v ud ud ud
k d
nr v v *v uj
an d ， 。
*pre *r *pha *u
*r *v *suf *介符 *u
*u *介符 *suf
ul *介符 *后符
*suf *e *后符
vn n n n
b *v
*d v
ad *d
f *v
df *e *e
ug uj
ns *介符
d v *介符 *介符 *后符
ag d q
uj n …
zg ！ … 。 。
z ！ …
mq ns
'''
```

### Branch wordclass route <sub>-route-b</sub>

```python
semt_branch_code = '''
*c *介符
mq r
'''
```

### Text (see [sao.txt](sao.txt))

## Usage

Usage document based on Python argparse form Python3 standard library

```python
# -*- coding: utf-8 -*-

app = ArgumentParser(prog='pr', description=…, epilog=…)
```

```bash
~/Projects/pr.py% ./pr.py help   
usage: pr [-h] [--version] [--no-word-class] [--line-max LINE_MAX]
          [--file FILE] [--debug] [--quiet] [-llen LLEN] [-lsep LSEP]
          [-lnl LNL] [-rlen RLEN] [-rsep RSEP] [-rnl RNL] [-rsepen]
          [-rlsep RLSEP] [-rbondsep RBONDSEP] [-rbk RBK] [-rbad RBAD]
          [-rbegcls RBEGCLS] [-metadict METADICT] [-route-a ROUTE_A]
          [-route-b ROUTE_B]
          action [action ...]

Simple utility generating random Chinese text

positional arguments:
  action                Actions
                        (char/lexical/autosplit(split)/wkinds/smart/loop)

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         Print version
  --no-word-class, -nwc
                        Dont show word classes provided by Jieba dict (WC=0)?
                        by default
  --line-max LINE_MAX, -lines LINE_MAX
                        Generate with max lines (LEN=-1)
  --file FILE, -f FILE  Use input file path (default sao.txt)
  --debug, -dbg         Show intrinsics
  --quiet, -q           Be quiet (QUIET=1)

lexical generator:
  -llen LLEN            Length ratio
  -lsep LSEP            Seprator ratio
  -lnl LNL              Newline ratio

smart generator:
  -rlen RLEN            Length ratio
  -rsep RSEP            Random seprator ratio
  -rnl RNL              Newline ratio
  -rsepen               Enable random seprator
  -rlsep RLSEP          Limit ratio seprator
  -rbondsep RBONDSEP    Bound of seprator to line end (3,4) (disable creating)
  -rbk RBK              Statement position ratio
  -rbad RBAD            Bad(random) words ratio
  -rbegcls RBEGCLS      WKind to start generation

smart generator routes:
  -metadict METADICT    Path for meta dictionary
  -route-a ROUTE_A      Normal succeeder in statement
  -route-b ROUTE_B      Branch succeeder in statement

Text outputted by this program simply generated by random/statistic algorithm
```

