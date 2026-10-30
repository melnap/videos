"""V12: picked Unsplash candidates -> stock/media/<Uxx_i>.jpg (2400 px), metadata -> stock/unsplash.json.
download_location is stored but NOT triggered (unsplash_track.py does that for photos actually used)."""
import json,os
SP=os.environ.get('SP','/tmp/claude-0')
PICKS='''U01 3 7 8
U02 7 0 10
U03 4 11
U04 0 9 10
U05 6 7 2 4
U06 0 9 7
U07 8
U09 1 5
U10 3 4
U11 5 8
U12 6 10
U13 3 4
U14 8
U15 5 7 2
U16 6 1
U17 2 3'''
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
open(f'{SP}/udl12.txt','w').write('\n'.join(jobs)+'\n')
json.dump(meta,open('stock/unsplash.json','w'),indent=1)
print(len(meta),'items',len(jobs),'to download')
