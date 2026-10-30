"""V12: picked Pixabay candidates (motif + index from contact sheets) -> stock/media/<motif><v|p><id>, metadata -> stock/pixabay.json.
Usage: python3 stock_picks.py            -> writes $SP/dl12.txt (url path) and stock/pixabay.json
DROP lists keys rejected after full-size check."""
import json,os
SP=os.environ.get('SP','/tmp/claude-0')
PICKS='''E01 p1 p5
E02 p3 p1 v5
E03 p0
E08 v3 p0
E49 v8 v7 p4 p6
E05 p3
E06 p4 p6 v0
E07 v0 v4 p1 p0
E05 p6
E47 p5
E09 v4 v6 v1
E50 v7
E44 v3 p7
E10 p4
E11 v6 v0 v7
E13 p0 p4 v0 v4
E50 v8
E15 v0
E17 p1 p5 p4
E18 p1 p5 p0
E20 p2 p3 p7 p0
E21 p6 p7 p5
E22 p0
E23 p5 p4
E24 v0 v2 v6 p1
E27 v0
E26 p5 p6 p3
E27 p2 p6
E28 p7
E29 p3 p4 p2
E30 p0 p1
E32 p2 p5 p6
E33 p1 p2 p4
E30 p3
E34 p2 p1
E36 p0 p1 p3 p7
E37 v1 v0 p0
E38 p0 p2 p4
E39 p0 p4 p6 p1
E40 p1 p6 p5 v8
E42 p0 p5
E44 p5 p2 v4 p0
E45 v0 v1 p3 p7
E46 v0 p1
E47 v0 p2 p3 p0
E48 p2 p3 p6 p0'''
DROP=set(open('stock/drop.txt').read().split()) if os.path.exists('stock/drop.txt') else set()
C=json.load(open('stock/candidates.json')); os.makedirs('stock/media',exist_ok=True)
meta={}; seen={}; jobs=[]; dups=[]
for line in PICKS.splitlines():
    m,*ix=line.split()
    for i in ix:
        x=C[m]['v' if i[0]=='v' else 'p'][int(i[1:])]
        if x['id'] in seen: dups.append(f"{m}{i}={seen[x['id']]}"); continue
        key=f"{m}{i[0]}{x['id']}"; seen[x['id']]=key
        if key in DROP: continue
        fn=f"stock/media/{key}.{'mp4' if i[0]=='v' else 'jpg'}"
        d=dict(file=fn,src='pixabay',kind='video' if i[0]=='v' else 'photo',pixabay_id=x['id'],url=x['page'],author=x['user'],license='Pixabay Content License',query=C[m]['q'],dur=x.get('dur'))
        if i[0]=='v': d['res']=f"{x['w']}x{x['h']}"
        meta[key]=d
        if not os.path.exists(fn): jobs.append(f"{x['url']} {fn}")
open(f'{SP}/dl12.txt','w').write('\n'.join(jobs)+'\n')
json.dump(meta,open('stock/pixabay.json','w'),indent=1)
vs=[k for k in meta if meta[k]['kind']=='video']
print(len(meta),'items',len(vs),'videos',len(jobs),'to download; dups skipped:',dups)
print('est video MB', round(sum(x['size'] for m in C for x in C[m]['v'] if f"{m}v{x['id']}" in meta)/1e6))
