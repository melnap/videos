"""V10: Pixabay search per motif -> stock/candidates.json + thumbnail download list (scratchpad)."""
import json,os,time,urllib.request,urllib.parse,sys
K=os.environ['PIXABAY_API_KEY']
SP=os.environ.get('SP','/tmp/claude-0')
Q=[('E01','ice crystals'),('E02','frozen berries'),('E03','frozen vegetables'),('E04','frozen meat'),('E05','ground beef'),
('E06','raw chicken'),('E07','cranberries'),('E08','cranberry harvest'),('E09','cranberry sauce'),('E10','roast turkey'),
('E11','raw turkey'),('E12','sliced turkey'),('E13','turkey sandwich'),('E14','pot pie'),('E15','ham'),
('E16','bean soup'),('E17','stew pot'),('E18','soup bowl'),('E19','cookies baking'),('E20','cookie tin'),
('E21','raw steak'),('E22','bacon'),('E23','sausages'),('E24','hot dog'),('E25','cracking egg'),
('E26','eggs carton'),('E27','potato salad'),('E28','egg salad'),('E29','lettuce'),('E30','cucumber'),
('E31','celery'),('E32','tomatoes'),('E33','green beans'),('E34','broccoli'),('E35','boiling water'),
('E36','coin'),('E37','ice cubes'),('E38','melting ice'),('E39','ice storm'),('E40','power lines winter'),
('E41','snowstorm night'),('E42','candle dark'),('E43','window snow night'),('E44','house snow night'),('E45','thermometer'),
('E46','writing list'),('E47','handwriting pen'),('E48','dry ice'),('E49','raw meat plate'),('E50','empty plate')]
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
        R=[r for r in (h['videos'][s] for s in ('small','medium','large')) if r.get('url') and r['width']>=1920 and r['width']>r['height']]
        if h.get('type')=='animation' or h['duration']<4 or not R: continue
        r=R[0]
        vs.append(dict(kind='pv',id=h['id'],page=h['pageURL'],user=h['user'],dur=h['duration'],w=r['width'],h=r['height'],size=r['size'],thumb=h['videos']['medium']['thumbnail'] or h['videos']['small']['thumbnail'],url=r['url'],tags=h['tags']))
    ps=[dict(kind='pp',id=h['id'],page=h['pageURL'],user=h['user'],thumb=h['webformatURL'],url=h['largeImageURL'],tags=h['tags']) for h in p['hits']]
    C[m]=dict(q=q,v=vs[:12],p=ps[:8])
json.dump(C,open('stock/candidates.json','w'))
with open(f'{SP}/th10.txt','w') as f:
    for m,c in C.items():
        for x in c['v']+c['p']:
            fn=f"{SP}/thumbs/{m}_{x['kind']}{x['id']}.jpg"
            if not os.path.exists(fn): f.write(f"{x['thumb']} {fn}\n")
print({m:(len(c['v']),len(c['p'])) for m,c in C.items()})
