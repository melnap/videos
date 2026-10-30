"""V10: picked Unsplash candidates -> stock/media/<Uxx_i>.jpg (2400 px), metadata -> stock/unsplash.json.
download_location is stored but NOT triggered (unsplash_track.py does that for photos actually used)."""
import json,os
SP=os.environ.get('SP','/tmp/claude-0')
PICKS='''U01 2 5 8
U02 0 2 3 4 9
U03 0 1 3 7
U04 0 1 2 9 11
U05 1 2 3 4
U06 1 2 10
U07 2 3 4 6
U08 2 6 11
U09 0 1 6 9
U10 0 6
U11 0 1 9
U12 0 2 6 8
U13 2 4 5 8
U14 0 2 4 6 7
U15 0 1
U16 2 5 6 9'''
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
open(f'{SP}/udl10.txt','w').write('\n'.join(jobs)+'\n')
json.dump(meta,open('stock/unsplash.json','w'),indent=1)
print(len(meta),'items',len(jobs),'to download')
