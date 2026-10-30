"""V10: picked Pixabay candidates (motif + index from contact sheets) -> stock/media/<motif><v|p><id>, metadata -> stock/pixabay.json.
Usage: python3 stock_picks.py            -> writes $SP/dl10.txt (url path) and stock/pixabay.json
DROP lists keys rejected after full-size check."""
import json,os
SP=os.environ.get('SP','/tmp/claude-0')
PICKS='''E01 v0 v8 v11 p0 p1 p3
E02 p6 p1 p2
E03 p3 p5
E04 v4 v3
E05 v5 v7 p0 p1 p4
E06 p0 p3 p6 p1 p2
E07 v1 p0 p3
E08 p3 p6 p1 p7
E09 p1
E10 p0 p2 p5 p6 p7
E11 p2 p6
E12 p5 p1 p0
E13 p2 p1 p6
E14 p0 p1 p2 v1
E15 v0 v6
E16 p2 p6 p4 p7
E17 v1 v3 p3 p4 p6
E18 v6 v8 p7 p5
E19 v0 v2 p3 p0 p1
E20 p4 p7 v3
E21 v5 v7 p5 p7 p4
E22 v0 v8 v10 v11 v5
E23 v1 v0 p3
E24 v0 p1 p3 p5
E25 v1 v2 p2 p7
E26 p0 p3 p5 p7
E27 p1 p2 p7 v11 v4
E28 p2 p6
E29 v6 v9 p0
E30 v0 v10 p0 p7
E31 p0 p1 p6
E32 v7 v11 p0 p4
E33 p0 p4 p7
E34 v3 v10 v1 p2
E35 v1 p4
E36 v0 v3 p6
E37 v0 v8 p0 p1 p2
E38 v2 p6 p7
E39 p1 p3 v4
E40 p0 p3 p4 p5
E41 p2
E42 v4 v7 v6 p5
E43 v3 p7
E44 v2 p0 p6
E45 p1 p5 p4
E46 v9 p0 p7 p4
E47 v8 v3 p1 p5
E48 v2 p2
E49 p3 p6 p4
E50 p0 p5
E52 v8 p0 p1
E53 p3 p5 p1 v2
E54 v3 v2 v10 p7 p1
E55 v2 v3
E56 p2
E57 v1 v2 v6 p4 p6
E58 p5 p7
E61 p1
E62 p0 v7
E64 p0 p5
E65 p7 p3
E67 p0 p1
E68 v6 p7
E69 p4 p6
E70 v1 v10'''
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
open(f'{SP}/dl10.txt','w').write('\n'.join(jobs)+'\n')
json.dump(meta,open('stock/pixabay.json','w'),indent=1)
vs=[k for k in meta if meta[k]['kind']=='video']
print(len(meta),'items',len(vs),'videos',len(jobs),'to download; dups skipped:',dups)
print('est video MB', round(sum(x['size'] for m in C for x in C[m]['v'] if f"{m}v{x['id']}" in meta)/1e6))
