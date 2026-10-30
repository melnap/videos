"""Write description_credits.txt (Pixabay + Unsplash authors of stock actually used in shots.json)."""
import json,re
P=json.load(open('stock/pixabay.json')); U=json.load(open('stock/unsplash.json')); SH=json.load(open('shots.json'))
used={re.split(r'[~^]',o['id'])[0] for o in SH if o['kind']=='BR'}
pu=sorted({P[k]['author'] for k in used if k in P},key=str.lower)
uu=sorted({U[k]['author'] for k in used if k in U},key=str.lower)
txt='Stock footage & photos: Pixabay ('+', '.join(pu)+')\nPhotos: '+', '.join(f'{u} / Unsplash' for u in uu)+'\n'
open('description_credits.txt','w').write(txt); print(txt)
