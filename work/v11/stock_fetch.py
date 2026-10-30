"""V11: Pixabay search per motif -> stock/candidates.json + thumbnail download list (scratchpad)."""
import json,os,time,urllib.request,urllib.parse,sys
K=os.environ['PIXABAY_API_KEY']
SP=os.environ.get('SP','/tmp/claude-0')
Q=[('E01','butter block'),('E02','butter dish'),('E03','butter knife'),('E04','butter toast'),('E05','sliced butter'),
('E06','grated butter'),('E07','biscuits baking'),('E08','rolling dough pie'),('E09','pie crust'),('E10','scones'),
('E11','christmas cookies baking'),('E12','cookie dough'),('E13','thanksgiving dinner'),('E14','dinner rolls'),('E15','stuffing'),
('E16','pumpkin pie'),('E17','mashed potatoes'),('E18','gravy'),('E19','roux'),('E20','grilled cheese'),
('E21','tomato soup'),('E22','cornbread'),('E23','chili con carne'),('E24','pancakes syrup'),('E25','rice bowl'),
('E26','steamed vegetables butter'),('E27','butter pan'),('E28','ice cube tray'),('E29','honey cinnamon'),('E30','garlic herbs'),
('E31','herb butter'),('E32','toast'),('E33','cows pasture'),('E34','milk pouring'),('E35','autumn leaves'),
('E36','calendar'),('E37','snow window'),('E38','snowy road'),('E39','kitchen scale'),('E40','measuring cups'),
('E41','coins'),('E42','dollar bills'),('E43','onion'),('E44','frost'),('E45','melting butter'),
('E46','corn on the cob butter'),('E47','flour bowl')]
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
with open(f'{SP}/th11.txt','w') as f:
    for m,c in C.items():
        for x in c['v']+c['p']:
            fn=f"{SP}/thumbs/{m}_{x['kind']}{x['id']}.jpg"
            if not os.path.exists(fn): f.write(f"{x['thumb']} {fn}\n")
print({m:(len(c['v']),len(c['p'])) for m,c in C.items()})
