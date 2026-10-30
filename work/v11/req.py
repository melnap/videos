import json,sys,assets_m as a
ks=sys.argv[1:]; R=[]
for i,(k,kind,ref,p,*m) in enumerate(a.A):
    if ks and k not in ks: continue
    med=[]
    if p.startswith(a.ELEM): med.append({'value':a.CATH,'role':'image_references'})
    if ref: med.append({'value':ref,'role':'image_references'})
    R.append({'index':i,'params':{'model':'nano_banana_2','aspect_ratio':'16:9','prompt':p,'medias':med}})
print(json.dumps(R))
