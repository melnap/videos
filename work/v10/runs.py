import json,os,re
exec(open('shots.py').read().split("if __name__")[0])
P=json.load(open('stock/pixabay.json')); Uj=json.load(open('stock/unsplash.json'))
def isvid(i):
    b=re.split(r'[~^]',i)[0]
    if b.startswith('TH') or os.path.exists(f'media/vid/{b}.mp4'): return True
    m=P.get(b) or Uj.get(b)
    if m: return m.get('kind')=='video'
    return os.path.exists(f'stock/media/{b}.mp4')
run=[];tot=0;vid=0
for o in shots+[dict(kind='END',id='',t=VO_END,dur=0)]:
    if o['kind']=='BR':
        tot+=o['dur']
        if isvid(o['id']): vid+=o['dur']
        else: run.append(o); continue
    if len(run)>=3: print('RUN', [(r['id'],round(r['t'],1),round(r['dur'],1)) for r in run])
    run=[]
print('BR video share %.0f%%'%(100*vid/tot), 'BR total', round(tot))
from collections import Counter
c=Counter(re.split(r'[~^]',o['id'])[0] for o in shots if o['kind']=='BR' and '^' not in o['id']); print('reuse>2',[k for k,v in c.items() if v>2])
