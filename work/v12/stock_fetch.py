"""V12: Pixabay search per motif -> stock/candidates.json + thumbnail download list (scratchpad)."""
import json,os,time,urllib.request,urllib.parse,sys
K=os.environ['PIXABAY_API_KEY']
SP=os.environ.get('SP','/tmp/claude-0')
Q=[('E01','ice storm'),('E02','freezing rain'),('E03','ice branches'),('E04','power lines ice'),('E05','snowstorm night'),
('E06','blizzard house'),('E07','snowy road'),('E08','house snow night'),('E09','candle dark'),('E10','lantern dark'),
('E11','flashlight dark'),('E12','power outage'),('E13','candlelight hands'),('E14','refrigerator'),('E15','fridge open'),
('E16','cooler ice'),('E17','thermometer'),('E18','cheddar cheese'),('E19','pickles'),('E20','jelly jar'),
('E21','peanut butter'),('E22','apple peanut butter'),('E23','crackers'),('E24','milk pouring'),('E25','tuna'),
('E26','cereal milk'),('E27','dried fruit'),('E28','raisins'),('E29','dried apricots'),('E30','dried cranberries'),
('E31','prunes'),('E32','nuts jar'),('E33','trail mix'),('E34','applesauce'),('E35','fruit cup'),
('E36','granola bar'),('E37','cookies'),('E38','chocolate pieces'),('E39','hard candy'),('E40','water bottles'),
('E41','water jug'),('E42','can opener'),('E43','batteries'),('E44','blanket candle'),('E45','dog eating'),
('E46','cat eating'),('E47','snowy neighborhood'),('E48','porch snow'),('E49','snow night street'),('E50','candles')]
if len(sys.argv)>1: Q=[q for q in Q if q[0] in sys.argv[1:]] + [tuple(a.split('=',1)) for a in sys.argv[1:] if '=' in a]
os.makedirs('stock/cache',exist_ok=True)
def get(u,fn):
    if os.path.exists(fn): return json.load(open(fn))
    for t in range(4):
        try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'curl/8'}),timeout=40)); break
        except Exception as e: print('retry',fn,e); time.sleep(3)
    json.dump(d,open(fn,'w')); time.sleep(0.7); return d
C=json.load(open('stock/candidates.json')) if os.path.exists('stock/candidates.json') else {}
for m,q in Q:
    qq=urllib.parse.quote_plus(q)
    v=get(f'https://pixabay.com/api/videos/?key={K}&q={qq}&per_page=40&safesearch=true',f'stock/cache/{m}_v.json')
    p=get(f'https://pixabay.com/api/?key={K}&q={qq}&image_type=photo&orientation=horizontal&min_width=1920&per_page=30&safesearch=true',f'stock/cache/{m}_p.json')
    vs=[]
    for h in v['hits']:
        R=[r for r in (h['videos'][s] for s in ('small','medium','large')) if r.get('url') and r['width']==1920 and r['width']>r['height']]
        if h.get('type')=='animation' or h['duration']<4 or not R: continue
        r=R[0]
        vs.append(dict(kind='pv',id=h['id'],page=h['pageURL'],user=h['user'],dur=h['duration'],w=r['width'],h=r['height'],size=r['size'],thumb=h['videos']['medium']['thumbnail'] or h['videos']['small']['thumbnail'],url=r['url'],tags=h['tags']))
    ps=[dict(kind='pp',id=h['id'],page=h['pageURL'],user=h['user'],thumb=h['webformatURL'],url=h['largeImageURL'],tags=h['tags']) for h in p['hits']]
    C[m]=dict(q=q,v=vs[:10],p=ps[:8])
json.dump(C,open('stock/candidates.json','w'))
with open(f'{SP}/th12.txt','w') as f:
    for m,c in C.items():
        for x in c['v']+c['p']:
            fn=f"{SP}/thumbs/{m}_{x['kind']}{x['id']}.jpg"
            if not os.path.exists(fn): f.write(f"{x['thumb']} {fn}\n")
print({m:(len(c['v']),len(c['p'])) for m,c in C.items()})
