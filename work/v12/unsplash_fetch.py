"""V12: Unsplash search per thin motif -> stock/unsplash_candidates.json + thumb list (no download_location calls)."""
import json,os,urllib.request,urllib.parse,time
K=os.environ['UNSPLASH_ACCESS_KEY']; SP=os.environ.get('SP','/tmp/claude-0')
Q=[('U01','ice storm power lines'),('U02','flashlight beam dark'),('U03','camping lantern night'),('U04','dark kitchen night'),('U05','snowy house night'),
('U06','open refrigerator'),('U07','cooler ice'),('U08','milk carton'),('U09','tuna crackers'),('U10','nuts glass jar'),
('U11','canned peaches bowl'),('U12','water jugs'),('U13','batteries'),('U14','family candlelight'),('U15','cat eating bowl'),
('U16','power outage candle'),('U17','snowy porch')]
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
with open(f'{SP}/u12.txt','w') as f:
    for m,c in C.items():
        for i,x in enumerate(c['items']): f.write(f"{x['thumb']} {SP}/uthumbs/{m}_{i}.jpg\n")
print({m:len(c['items']) for m,c in C.items()})
