"""Trigger Unsplash download_location for every Unsplash photo used in the edit (API guideline)."""
import json,os,re,urllib.request
U=json.load(open('stock/unsplash.json')); SH=json.load(open('shots.json'))
used=sorted({re.split(r'[~^]',o['id'])[0] for o in SH if o['kind']=='BR'} & set(U))
ok=0
for k in used:
    r=urllib.request.Request(U[k]['download_location'],headers={'Authorization':'Client-ID '+os.environ['UNSPLASH_ACCESS_KEY'],'User-Agent':'curl/8'})
    try: urllib.request.urlopen(r,timeout=20).read(); ok+=1
    except Exception as e: print(k,e)
print('tracked',ok,'of',len(used))
