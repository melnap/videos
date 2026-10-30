import json,os,re
exec(open('beats.py').read())
S=json.load(open('sent.json')); TH={t['id']:t for t in json.load(open('th_plan.json'))}
VO_END=652.56
def thid(it): return it.split('@')[0]
def start(k):
    s,it=BEATS[k][:2]
    if len(BEATS[k])>2: return BEATS[k][2]  # explicit absolute start time (mid-sentence cut)
    if k==0: return 0
    if it[0].startswith('TH'):
        p=TH[thid(it[0])]
        return p['s'] if s==p['sent'][0] else S[s]['s']-0.05
    pv=BEATS[k-1][1][0]
    if pv.startswith('TH'):
        p=TH[thid(pv)]
        if p['sent'][1]+1==s: return p['e']
    return S[s]['s']-0.05
starts=[round(start(k),3) for k in range(len(BEATS))]
shots=[]
for k,(s,items,*_) in enumerate(BEATS):
    a=starts[k]; b=starts[k+1] if k+1<len(BEATS) else VO_END; span=b-a
    if items[0].startswith('TH'):
        p=TH[thid(items[0])]; shots.append(dict(t=a,kind='TH',id=thid(items[0]),ms=round(a-p['s'],3))); continue
    if items[0].startswith('G:'): shots.append(dict(t=a,kind='GFX',id=items[0][2:])); continue
    pieces=[]; rest=items; span2=span
    if items[0].startswith('C:'):
        cd=min(4.0,max(2.0,span-3.0)) if len(items)>1 else span
        pieces.append(('CARD',items[0][2:],cd)); rest=items[1:]; span2=span-cd
    if rest:
        share=span2/len(rest)
        for it in rest:
            n=1 if share<=4.6 else (2 if share<=9 else 3)
            for q in range(n): pieces.append(('BR',it+('' if q==0 else f'^{q}'),share/n))
    t=a
    for kind,i,d in pieces: shots.append(dict(t=round(t,3),kind=kind,id=i)); t+=d
for n,o in enumerate(shots):
    o['dur']=round((shots[n+1]['t'] if n+1<len(shots) else VO_END)-o['t'],3)
MOVES=['zin','panR','zout','panL','zin','zout','panR','panL']; mv=0
for o in shots:
    o['move']='none'
    if o['kind']=='BR':
        o['move']=('tightL' if mv%2 else 'tightR') if ('^' in o['id'] or '~' in o['id']) else MOVES[mv%len(MOVES)]; mv+=1
# talking heads: alternate wide / close (~130 %), now and then a slow push-in; a split TH ('@') switches size
TM=['none','thclose','thpush','thclose']; tm=0
for o in shots:
    if o['kind']=='TH':
        o['move']=TM[tm%len(TM)]; tm+=1
json.dump(shots,open('shots.json','w'),indent=0)
if __name__=='__main__':
    br=[o for o in shots if o['kind']=='BR']
    print(len(shots),'shots',len(br),'broll avg %.2f'%(sum(o['dur'] for o in br)/len(br)))
    print('short',[(o['id'],o['dur']) for o in shots if o['dur']<1.3])
    print('long',[(o['id'],o['dur']) for o in shots if o['kind']=='BR' and o['dur']>4.6])
    print('TH',round(sum(o['dur'] for o in shots if o['kind']=='TH'),1))
    print('cards/gfx',[(o['id'],o['dur']) for o in shots if o['kind'] in('CARD','GFX')])
