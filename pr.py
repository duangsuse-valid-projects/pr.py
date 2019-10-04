#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Random utility for Chinese random text generation (token viewing)

author: duangsuse
'''

import typing
typing.TYPE_CHECKING = True
from typing import Any, AnyStr, Callable, Union, TypeVar, cast
from typing import Iterable, Tuple, List, Dict, Set
T = TypeVar('T')
E = TypeVar('E')
K = TypeVar('K')
V = TypeVar('V')

from os import environ
from sys import stdout, argv
from argparse import ArgumentParser

from time import perf_counter
from random import sample, randint

from pandas import DataFrame
from jieba import lcut, get_dict_file
from jieba import setLogLevel as jiebaLogLevel

#### identity(1) is 1
identity = lambda x: x
#useful
#### envOr('PATH', '/bin:/usr/bin', lambda s: s.split(':')) is not None
def envOr(v: str, deft: T, caster: Callable[[str], T]
          = lambda s: cast(T,s)) -> T:
  return caster(environ[v]) if v in environ else deft
#### entries(dict([('A', 0x41)])) == [('A', 0x41)]
def entries(dic: Dict[K, V]) -> List[Tuple[K, V]]: return [(k, dic[k]) for k in dic.keys()]
#### dic={}; countTo(dic, [1,2,3,3], 0, lambda x, i: x*10+i) == {1: 0, 2: 1, 3: 23}
def countTo(dic: Dict[K, V], seq: Iterable[K], init: V = 0,
            update: Callable[[V, int], V] = lambda x, i: cast(V, x+1)):
  for idx, item in enumerate(seq):
    if item not in dic: dic[item] = 0
    dic[item] = update(dic[item], idx)
#### ds=[]; appendAll(ds, [[1,1], [2,2], [3,3]]) == [1, 1, 2, 2, 3, 3]
def appendAll(dst: List[E], src: Iterable[Iterable[E]]):
  for xs in src:
    for x in xs:
      dst.append(x)
def pick(xs): return sample(xs, 1)[0]
def ratioly(r, f):
  if randint(0,100) < r: return f()
#### color('red', 31) == '\x1b[31mred\x1b[0m'
def color(t: AnyStr, ac: int) -> str: return "\x1b[{}m{}\x1b[0m".format(ac, t)

def descPandaTbl(tbl: DataFrame, headn: int = 10):
  if QUIET: return
  print(tbl.head(headn))
  print(tbl.describe())
def joinPrint(xs: Iterable[str], sep: str = ''): print(sep.join(xs))
#### it0([0, 1]) == 0
it0 = lambda t: t[0]
#### it1([0, 1]) == 1
it1 = lambda t: t[1]
#### average([1,2,3]) == 2.0 and average(['..', '.', '...'], len) == 2.0
def average(xs: List[E], scalarf: Callable[[E], int] = int) -> float:
  return sum(scalarf(x) for x in xs) / max(1, len(xs))
#### delazy(1) == 1 and delazy(lambda: 1) == 1
def delazy(fo: Union[Callable[[], T], T]) -> T: return fo() if callable(fo) else fo

def printed(f: Callable): #decorator
  def __call__(*fps, **kwps):
    res = f(*fps, **kwps)
    print(res); return
  return __call__
def timed(opname: Union[str, Callable[[], str]]): #decorator
  def timedop(op: Callable):
    def op_timer(*fps, **kwps):
      t0 = perf_counter(); res = op(*fps, **kwps)
      dt = perf_counter() - t0
      unitfmt = f'{dt*1000}ms' if (dt <= 0.1**2) else f'{dt}s'
      tdfmt = "" if QUIET else ' costs {}'
      print(('{}'+tdfmt).format(color(delazy(opname), 33), color(unitfmt, 32)))
      return res
    return op_timer
  return timedop

@printed
def banner(t: AnyStr, c: int = 31): return '==\t{}\t=='.format(color(t,c))

#useful
showCtrl = dict([(9, '\u21E5'), (11, '\u2B73'), (10, '↵\n'), (13, '⏎\r'), (32, '.')])

def dict_code(c, dr='\n', dc=' '):
  return dict([e.split(dc) for e in c.split(dr) if len(e.split(dc)) == 2])
#useful
def brl_code(c, dr='\n', dc=' ', coll=list, addf=list.append,
             keyedf=lambda dic, ps: [ps[0]], itemf=lambda dic, ps: ps[1:len(ps)]):
  dic = {}
  for r in c.strip().split(dr):
    ps = r.strip().split(dc)
    if len(ps) < 2: continue
    for k in keyedf(dic, ps):
      if k not in dic: dic[k] = coll()
      for s in itemf(dic, ps): addf(dic[k], s)
  return dic

#####
#### Line length cut for text generation
LEN = envOr('LEN', (-1), int)
QUIET = envOr('QUIET', False, lambda v: v == '1')
#### Print colorized word class?
ShowWordClass = envOr('WC', True, lambda v: v != '0')

filename = 'sao.txt'
@timed(lambda: f'Read File {filename}')
def read_file():
  with open(filename, 'r') as f:
    txt = f.read()
    lns = txt.split('\n')
  return (txt, lns)

#### input text and (lines)
global txt, lns
@timed(lambda: f'Count Char Freq of length {len(txt)}({len(lns)} lines)')
def count_chars(txt):
  chrd = {} # 字符典
  countTo(chrd, txt)
  wrds = entries(chrd) # 字符典.entries(c, n)
  chrsdsc = sorted(wrds, key=it1, reverse=True)

  dd0 = DataFrame()
  dd0['chr'] = list(map(it0, chrsdsc))
  dd0['n'] = list(map(it1, chrsdsc))
  descPandaTbl(dd0)
  return chrsdsc

##
@timed('Split Lines into Jieba Words')
def cut_lines(lns):
  dd = DataFrame()
  lnwords = dd['words'] = list(map(lcut, lns)) #tokenize
  dd['line_len'] = list(map(len, lns))
  dd['word_len_sum'] = list(map(len, lnwords))
  dd['word_len_avg'] = [average(tokz, scalarf=len) for tokz in lnwords]
  descPandaTbl(dd, 30)
  allwords = []
  appendAll(allwords, lnwords)
  return allwords, dd

@timed('Statics for Words')
def stat_words(sws):
  wordc = {}
  for (i, w) in enumerate(sws):
    if not w in wordc: wordc[w] = ([i], 0)
    orig = wordc[w] # old indices storage
    orig[0].append(i)
    wordc[w] = (orig[0], orig[1]+1) # (poss, count)
  allposed = map(lambda kv: (kv[0], kv[1][1]), entries(wordc))
  return sorted(allposed, key=it1, reverse=True)

##
global worda
wordsp = set('， 、 。 ！ ？ ~ ： ； …'.split(' '))
@timed(lambda: f'Generate a Mess Using {len(worda)} words, {len(wordsp)} seps')
def auto_split_gen(dd, worda, lenratio=2, sepratio=10, nlratio=80):
  txt_gen = []
  for lnl in dd['line_len'][0:LEN]:
    while lnl > 0:
      word = pick(worda)
      txt_gen.append(word)
      lnl -= len(word) / lenratio
      ratioly(sepratio, lambda: txt_gen.append(pick(wordsp)))
    ratioly(nlratio, lambda: txt_gen.append('\n'))
  return (''.join(txt_gen))

##
#useful
@timed('Read WordType Dict')
def jieba_wordtys():
  wordty_dict = {}
  dictf = get_dict_file()
  estxt = dictf.read().decode()
  entries = [etxt.split(' ') for etxt in estxt.split('\n')]
  allwords = len(entries)
  entries = filter(lambda ent: len(ent) == 3, entries)
  for w, _k, t in entries:
    wordty_dict[w] = t
  return (wordty_dict, allwords)

wordsp_mid = ('， 、 ： ；'.split(' '))
wordsp_end = ('。 ！ ？ ~ …'.split(' '))

global wtyo, wtyc, wtys, wtyid # 0.. id-repr of wtyo
# 帮(v) 大陆(n) 麻烦(an) 工作(vn) 凶(zg) 穿(zg) 组(zg)
# 一分钟(m) 暖和(a) 呢(y) 明年(t) 源泉(nz)
# 薄的(z)  不要(df) 怎么回事(l) 等(u) 尼玛(nrt) 帅(nr)
# 不知不觉(i)
wtyo = ('nr/zg/vn/a/v/n/o/m/uz/y/df/mq/an'+
     '/vq/rz/e/nrt/t/ud/ns/b/s/ul/z/p/nrfg'+
     '/j/nz/mg/dg/uv/rg/tg/k/q/rr/r/c/ug/d'+
     '/ng/x/l/ad/ag/h/uj/g/vi/vd/i/nt/f/vg/u').split('/')
wtyid = {}
for i, wty in enumerate(wtyo):
  wtyid[wty] = i
# for k in `awk 'BEGIN {$i=0;while($i!=110){print $i; $i++}}'|xargs`; printf '\e['$k'mA\e[0m' done
#useful
def wtyc(cls):
  if cls in wordsp: return 2
  i = wtyid[cls]
  if i in range(6, 6+4) or (6+4+6) <= i:
    if i not in range(6, 6+4): i -= 6
    return (84+i) % (84+(6+4+6)+17) # 第二段高亮彩色
  else:
    return 31+i # 第一段彩色
#useful
def wtyct(wc):
  ca = wtyc(wc)
  return color(wc, ca)
#useful
def wtycp():
  for wt in wtyid:
    stdout.write(wtyct(wt))
    stdout.write('/')
  stdout.write('\x7f') # DEL

#useful
@timed('Generate Dict by WordKinds')
def generate_wclassdict(words, wtydict, wtyset):
  wordclasses = {}
  for wclass in wtyset:
    wordclasses[wclass] = set()
  for wd in words:
    if wd not in wtydict: continue
    wordclasses[wtydict[wd]].add(wd)
  for sep in wordsp:
    wordclasses[sep] = [sep] # ！=[！]；？=[？]
    wtydict[sep] = sep
  return wordclasses

# 元词类简写：此类键名引用一个键的集合，添加时视为集合批量关于 succs 添加

# 代词 （语素） （名词性）
# 名词 人名 地名 团体名 外文名 其他专有名词 （动词性） （形容词性） （语素）
# 动词 （语素） （副词性） （名词性）
# 形容词 （语素） （副词性） （名词性）
# 副词 （语素） （形容词性） （动词性）
# 连接词
# 区别性 （语素）
# 辅助表达性词条 感叹词 拟声词
# （短语） 成语 常用语 简略语
# 状语
# 介词
# （前接部分）
# 助词
# （后接部分）
# 感叹 （语素）
# （位置） 方位 地名 处所词
# （数） 数词 数语素
# 量词
# 时间 时间语素
# 杂项 标点 非语素
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

metawordclz = brl_code(metawordclz_code, coll=set, addf=set.add)
def meta_keyed(dic, ps):
  keynam = ps[0]
  if keynam not in metawordclz:
    if keynam in wtyo or keynam in wordsp: return [keynam]
    else: raise KeyError('Word class not found', dic, keynam)
  return metawordclz[keynam]
def meta_value(dic, ps):
  resb = []
  for p in ps[1:len(ps)]:
    if p in metawordclz:
      for x in metawordclz[p]: resb.append(x)
    else: resb.append(p)
  return resb

# TODO 添加词类序列识别的功能
# 1. 固定序列插入新词时可以考虑
# 2. 如果两行对接词类吻合，取消上一次换行
# TODO 提供 succ 列表减去的办法，比如 u 和 uj 一起出现是无意义的，或者支持序列识别删除

# ， 、 。 ！ ？ ~ ： ； …
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
'''
'''
semt_branch_code = '''
*c *介符
mq r
'''
'''
'''

semt_succeeder = brl_code(semt_succeeder_code, keyedf=meta_keyed, itemf=meta_value)
semt_branch = brl_code(semt_branch_code, keyedf=meta_keyed, itemf=meta_value)

# 依照句子中的位置和上一词的词性选择单词
# bs: 单词位置系数，正影响分支选择的可能性
# bk: 默认开始分支的位置，bs 一定时 bk 越大越容易分支、bs*stmtpos >= bk 时发生变化
# 如果 bs 为 100，句尾一定有变化
# bad: 随机跳词性的可能性
def sample_by_semantic(lastcl, stmtpos, bs=10, bk=lambda: 82, bad=lambda: 4, deft_succ=lambda c: pick(wtyo)):
  will_branch_succ = randint(max(99,int(stmtpos*bs)),100) <= delazy(bk) # 随着句中位置的后移，变化可能性增大
  new_wcls = (semt_branch if will_branch_succ else semt_succeeder)
  new_wcl = pick(new_wcls.get(lastcl) or [deft_succ(lastcl)]) # 如果找不到后继，默认继续原词性
  return ratioly(delazy(bad), lambda: pick(worda)) or pick(worddict.get(new_wcl) or worda) # 有一定概率突破词性限制

LastLines = 0
no_newlineclz = 'j/uj/ul/：/；/，/、/？'.split('/')
@timed(lambda: f'Generated {LastLines} lines')
@printed
def gen_smart(ksep=0.66,lsep=4,borsep=(3,4),rnl=97,rlen=2,bk=82,bad=4,deft_cls=lambda: 'n',beg_cls=lambda: 'v',disableRandSep=True):
  #print(ksep,lsep,borsep,rnl,rlen,bk,bad,deft_cls,beg_cls,disableRandSep)
  global dd, worddict, wtys, LastLines; txt_gen = []
  for lnl in dd['line_len'][0:LEN]:
    ln_length = lnl
    last_charclass = delazy(beg_cls)
    while lnl >= 0 and lnl != 0: #joke
      count_used_sep = 0 # 不能输出太多标点
      ratio = 1- (abs(lnl)+1.0 / ln_length) # 语句位置
      #txt_gen.append(f'{ratio}') # 调试语句位置比率
      word = sample_by_semantic(last_charclass, ratio, bk=bk, bad=bad)
      lnl -= len(word) / rlen # 生成的字符长度只需等于原语句
      last_charclass = wtys.get(word) or delazy(deft_cls) # 选词词性
      txt_gen.append(color(word, wtyc(last_charclass)))
      if (len(txt_gen)>1 and last_charclass in no_newlineclz and txt_gen[-2] == '\n'): txt_gen.pop(-2) # 撤销不合适的换行
      if(ShowWordClass): txt_gen.append(color(f'({last_charclass})', 3))
      if not disableRandSep and (randint(0,1) == 0 and randint(0,lsep)>=count_used_sep):
        sep = pick(wordsp_mid if ratio <= (ksep) else wordsp_end)
        txt_gen.append(sep); last_charclass = sep
    oknewline = all([c not in wordsp for c in txt_gen[-1:-randint(*borsep)] ]) # 不能在标点符号后直接换行、不能在介词后换行
    if (oknewline and last_charclass not in no_newlineclz and randint(1,100) < rnl): txt_gen.append('\n')
  LastLines = txt_gen.count('\n')
  return (''.join(txt_gen))
#useful
def lexp(s, dc='n'):
  txt_gen = []
  words = lcut(s)
  for word in words:
    if word in set('\t\v\n\r '):
      txt_gen.append(word.translate(showCtrl))
      continue
    txt_gen.append(color(word, wtyc(wtys.get(word) or dc)))
    if(ShowWordClass): txt_gen.append(color(f'({wtys.get(word) or "?"})', 3))
  return ''.join(txt_gen)

VERSION = '1.0' # 迫真版本号
app = ArgumentParser(prog='pr', description='Simple utility generating random Chinese text',
         epilog='Text outputted by this program simply generated by random/statistic algorithm')
app.add_argument('--version', '-v', help='Print version', action='version', version=VERSION)
app.add_argument('--no-word-class', '-nwc', help='Dont show word classes provided by Jieba dict (WC=0)? by default', action='store_false', default=True)
app.add_argument('--line-max', '-lines', type=int, help=f'Generate with max lines (LEN={LEN})')
app.add_argument('--file', '-f', type=str, help=f'Use input file path (default {filename})')
app.add_argument('--debug', '-dbg', help='Show intrinsics', action='store_true')
app.add_argument('--quiet', '-q', help='Be quiet (QUIET=1)', action='store_true')
app.add_argument('action', type=str, nargs='+', help='Actions (char/lexical/autosplit(split)/wkinds/smart/loop)')

grp_l = app.add_argument_group('lexical generator')
grp_l.add_argument('-llen', type=int, help='Length ratio', default=2)
grp_l.add_argument('-lsep', type=int, help='Seprator ratio', default=10)
grp_l.add_argument('-lnl', type=int, help='Newline ratio', default=80)
grp_s = app.add_argument_group('smart generator')
# ksep=0.66,lsep=4,borsep=(3,4),rnl=97,rlen=2,bk=82,bad=4
# beg_cls, disableRandSep
grp_s.add_argument('-rlen', type=int, help='Length ratio', default=2)
grp_s.add_argument('-rsep', type=int, help='Random seprator ratio', default=0.66)
grp_s.add_argument('-rnl', type=int, help='Newline ratio', default=97)
grp_s.add_argument('-rsepen', action='store_false', help='Enable random seprator', default=True)
grp_s.add_argument('-rlsep', type=int, help='Limit ratio seprator', default=4)
grp_s.add_argument('-rbondsep', type=str, help='Bound of seprator to line end (3,4) (disable creating)', default='3,4')
grp_s.add_argument('-rbk', type=int, help='Statement position ratio', default=82)
grp_s.add_argument('-rbad', type=int, help='Bad(random) words ratio', default=4)
grp_s.add_argument('-rbegcls', type=str, help='WKind to start generation', default='r')

grp_rule = app.add_argument_group('smart generator routes')
grp_rule.add_argument('-metadict', type=str, help='Path for meta dictionary')
grp_rule.add_argument('-route-a', type=str, help='Normal succeeder in statement')
grp_rule.add_argument('-route-b', type=str, help='Branch succeeder in statement')

def zip_with_next(iter):
  gotc = 0
  try:
    while True:
      me = iter.__next__(); gotc += 1
      nxt = iter.__next__(); gotc += 1
      yield (me, nxt)
  except StopIteration:
    if gotc % 2 != 0: yield me

def zip_with_next_sticky(iter):
  try:
    left = iter.__next__()
    while True:
      right = iter.__next__()
      restup = (left, right)
      left = right
      yield restup
  except StopIteration: pass

def read_dicts(args): #well done, dear Python *3*
  global metawordclz, semt_succeeder, semt_branch
  md, da, db = (args.metadict, args.route_a, args.route_b)
  if md:
    with open(md, 'r') as f:
      code = f.read()
      metawordclz = brl_code(code, coll=set, addf=set.add)
  if da:
    with open(da, 'r') as f:
      code = f.read()
      semt_succeeder = brl_code(code, keyedf=meta_keyed, itemf=meta_value)
  if db:
    with open(db, 'r') as f:
      code = f.read()
      semt_branch = brl_code(code, keyedf=meta_keyed, itemf=meta_value)


deps = '''
loop<smart<wkinds<split<autosplit<lexical<char
'''
def loop(**ts):
  line = ''
  try:
    while True:
      line = input('>') if line=='' else input()
      print(lexp(line))
      if len(line) == 0: gen_smart(**ts)
  except EOFError:
    global ShowWordClass
    ShowWordClass = not ShowWordClass
    loop(**ts)
  except KeyboardInterrupt:
    print('bye')
def main(argv):
  global ShowWordClass, LEN, QUIET, filename
  args = app.parse_args(argv)
  ShowWordClass = args.no_word_class; LEN = args.line_max; QUIET = args.quiet
  if args.file: filename = args.file
  if filename == '-': filename = '/dev/stdin'
  if QUIET: jiebaLogLevel(0)
  llen, lsep, lnl = (args.llen, args.lsep, args.lnl)
  rlen, rsep, rnl = (args.rlen, args.rsep, args.rnl)
  rsepen, rlsep, rbondsep = (args.rsepen, args.rlsep, list(map(int, args.rbondsep.split(','))))
  rbk, rbad, rbegcls = (args.rbk, args.rbad, args.rbegcls)
  read_dicts(args)
  acts = args.action
  if args.debug: print(acts)
  for me, dep in zip_with_next_sticky(iter(deps.strip().split('<'))):
    if args.debug: print(f'Testing if {me} < {dep} is satisfied')
    if me in acts and dep not in acts:
      if args.debug: print(f'{dep} is required to run {me}')
      acts.append(dep)
  acts.reverse()
  if args.debug: print(deps, acts)
  if 'help' in acts:
    print(app.format_help()); return
  if len(acts) != 0:
    global txt, lns, worda, dd, worddict, wtys
    txt, lns = read_file() # Read text
    swd = count_chars(txt) # Count character rate for char based generation
  if 'char' in acts:
    banner('Char Based', 35)
    print(''.join([x[0] for x in swd ]))
  if 'lexical' in acts:
    sws, dd = cut_lines(lns)
    counted = stat_words(sws)
    banner('Lexical Based', 35)
    worda = list(map(it0, counted))
    print(''.join(worda))
  if 'autosplit' in acts:
    banner('Autosplit', 34)
    print(auto_split_gen(dd, worda, llen, lsep, lnl))
  if 'wkinds' in acts:
    wtys, jieba_allwords = jieba_wordtys()
    banner('Word Kinds', 36)
    wkinds = set(map(wtys.get, wtys))
    print(' / '.join(wkinds))
    worddict = generate_wclassdict(worda, wtys, wtyo)
    print(' | '.join([f'{k}*{len(worddict[k])}' for k in sorted(worddict)]))
    print(color(f'Got {len(wtys)} / {jieba_allwords} in {len(wtyo)} classes', 35))
  if 'smart' in acts:
    banner('Smart')
    if not QUIET: print(semt_succeeder, semt_branch)
    wtycp()
  if 'loop' in acts: loop(ksep=rsep,lsep=rlsep,borsep=rbondsep,rnl=rnl,rlen=rlen,bk=rbk,bad=rbad,beg_cls=rbegcls,disableRandSep=rsepen)

if __name__ == '__main__':
  main(argv);
