"""V11: picked Unsplash candidates -> stock/media/<Uxx_i>.jpg (2400 px), metadata -> stock/unsplash.json.
download_location is stored but NOT triggered (unsplash_track.py does that for photos actually used)."""
import json,os
SP=os.environ.get('SP','/tmp/claude-0')
PICKS='''U01 0 1 2
U02 1 8
U03 6 11 10
U04 7 8
U05 2 6 9 0
U06 0 2
U08 2 8 6 3
U09 0 3
U10 3 6 9 10
U11 0 2 7
U12 1
U13 0 5 9
U14 5 9
U15 0 1 2 11
U16 0 3 8'''
DROP=set(open('stock/udrop.txt').read().split()) if os.path.exists('stock/udrop.txt') else set()
C=json.load(open('stock/unsplash_candidates.json')); meta={}; jobs=[]
for line in PICKS.splitlines():
    m,*ix=line.split()
    for i in ix:
        x=C[m]['items'][int(i)]; key=f'{m}_{i}'
        if key in DROP: continue
        fn=f'stock/media/{key}.jpg'
        meta[key]=dict(file=fn,src='unsplash',kind='photo',unsplash_id=x['id'],url=x['url'],author=x['author'],license='Unsplash License',query=C[m]['q'],download_location=x['dl'])
        if not os.path.exists(fn): jobs.append(f"{x['full']} {fn}")
open(f'{SP}/udl11.txt','w').write('\n'.join(jobs)+'\n')
json.dump(meta,open('stock/unsplash.json','w'),indent=1)
print(len(meta),'items',len(jobs),'to download')
