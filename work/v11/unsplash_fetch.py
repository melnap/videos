"""V11: Unsplash search per thin motif -> stock/unsplash_candidates.json + thumb list (no download_location calls)."""
import json,os,urllib.request,urllib.parse,time
K=os.environ['UNSPLASH_ACCESS_KEY']; SP=os.environ.get('SP','/tmp/claude-0')
Q=[('U01','butter dish'),('U02','butter sticks'),('U03','slicing butter'),('U04','grated butter flour'),('U05','buttermilk biscuits'),
('U06','dinner rolls'),('U07','gravy pan'),('U08','grilled cheese skillet'),('U09','buttered rice'),('U10','ice cube tray'),
('U11','paper calendar'),('U12','kitchen scale baking'),('U13','freezer frost'),('U14','dollar bills'),('U15','thanksgiving table food'),('U16','measuring cups flour')]
os.makedirs('stock/ucache',exist_ok=True); C={}
for m,q in Q:
    fn=f'stock/ucache/{m}.json'
    if not os.path.exists(fn):
        u=f'https://api.unsplash.com/search/photos?query={urllib.parse.quote(q)}&per_page=12&orientation=landscape'
        r=urllib.request.urlopen(urllib.request.Request(u,headers={'Authorization':'Client-ID '+K,'User-Agent':'curl/8'}),timeout=30)
        print(m,'remaining',r.headers.get('X-Ratelimit-Remaining'))
        d=json.load(r); json.dump(d,open(fn,'w')); time.sleep(0.5)
    d=json.load(open(fn))
    C[m]=dict(q=q,items=[dict(id=r['id'],url=r['links']['html'],author=r['user']['name'],w=r['width'],plus=r.get('premium') or r.get('plus'),dl=r['links']['download_location'],full=r['urls']['raw']+'&w=2400&q=85&fm=jpg',thumb=r['urls']['small'],desc=r.get('alt_description')) for r in d['results']])
json.dump(C,open('stock/unsplash_candidates.json','w'),indent=1)
with open(f'{SP}/u11.txt','w') as f:
    for m,c in C.items():
        for i,x in enumerate(c['items']): f.write(f"{x['thumb']} {SP}/uthumbs/{m}_{i}.jpg\n")
print({m:len(c['items']) for m,c in C.items()})
