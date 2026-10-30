"""V11: picked Pixabay candidates (motif + index from contact sheets) -> stock/media/<motif><v|p><id>, metadata -> stock/pixabay.json.
Usage: python3 stock_picks.py            -> writes $SP/dl11.txt (url path) and stock/pixabay.json
DROP lists keys rejected after full-size check."""
import json,os
SP=os.environ.get('SP','/tmp/claude-0')
PICKS='''E01 v3 v1 p0 p3
E48 v5 p0
E02 v9 p3 p6
E03 p5 p7
E04 p7 p6
E05 p5 p6 p7
E06 p2 p3
E45 p4
E47 p6
E07 v0 p2
E08 v3 p0 p4
E09 v8 p3
E51 p7
E10 p4 p5 p2
E11 v1 p3
E12 v8
E50 v0
E67 v9
E13 p3 p7
E14 p7
E15 p4
E16 p2 p4
E17 p6 p7 p1
E18 p5 p7
E20 p7 p5 p0
E21 p3 p4 p1
E22 p0 p1 p2
E23 p0 p5
E24 v7 p5 p0
E25 p3 v2
E26 p0 p4
E46 p1 v9
E27 v1 v7 p0
E48 v2
E28 p2 p3
E29 v8 p2
E58 v1 p0
E30 v1 p3
E31 p1 p5
E56 v2 p0
E32 v8 p0
E61 v0 p0
E33 v0 v4 p5
E34 v1 v2
E35 v2 v8 p0 p3
E37 v2 p6
E38 v0 v5
E53 v5
E54 v7
E39 p1 p5
E40 p0
E41 v8 v2 p4 p6
E43 v3 p0 p3
E44 p0 p2'''
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
open(f'{SP}/dl11.txt','w').write('\n'.join(jobs)+'\n')
json.dump(meta,open('stock/pixabay.json','w'),indent=1)
vs=[k for k in meta if meta[k]['kind']=='video']
print(len(meta),'items',len(vs),'videos',len(jobs),'to download; dups skipped:',dups)
print('est video MB', round(sum(x['size'] for m in C for x in C[m]['v'] if f"{m}v{x['id']}" in meta)/1e6))
