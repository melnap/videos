"""V11 overlays on top of the karaoke subs: channel lower third, item labels (n/15, Wait on n/5), storage callouts. Hidden while a full-screen graphic runs."""
import json
S=json.load(open('sent.json')); SH=json.load(open('shots.json'))
GF=[(o['t'],o['t']+o['dur']) for o in SH if o['kind']=='GFX']
def ts(t): h=int(t//3600); m=int(t%3600//60); s=t%60; return f"{h}:{m:02d}:{s:05.2f}"
def clip(a,b):
    out=[(a,b)]
    for g0,g1 in GF:
        nxt=[]
        for x,y in out:
            if y<=g0 or x>=g1: nxt.append((x,y))
            else:
                if x<g0-0.3: nxt.append((x,g0))
                if y>g1+0.3: nxt.append((g1,y))
        out=nxt
    return [(x,y) for x,y in out if y-x>=1.2]
ITEMS=[(20,'Part 1/6','Why November'),(44,'Part 2/6','How much to buy'),(63,'Part 3/6','Which butter, how to wrap it'),(93,'Part 4/6','Using it from the freezer'),(119,'Part 5/6','A winter of butter'),(135,'Part 6/6','Mistakes to skip')]
STOP={135:154}
CALL=[(24,'Loss leader: priced low to bring you in'),(42,'Bought mid-Nov: best until May–July'),(55,'Write your number down'),(61,'Check the per-customer limit'),(70,'Compare the price per pound'),
 (89,'Back of the freezer, not the door'),(94,'Thaw: fridge, overnight'),(97,'Soften: about 1 hour on the counter'),(103,'Large holes of a box grater'),(132,'≈ $1 per stick'),(152,'Freezer burn: cut it off')]
L=['Style: LblN,Inter,30,&H002E61B8,&H002E61B8,&H00000000,&HB4F2EFE6,1,0,0,0,100,100,2,0,3,14,0,7,0,0,0,1',
   'Style: LblT,Inter,40,&H00475F4F,&H00475F4F,&H00000000,&HB4F2EFE6,1,0,0,0,100,100,0,0,3,14,0,7,0,0,0,1',
   'Style: Call,Inter,36,&H00FFFFFF,&H00FFFFFF,&H00000000,&H9C2E4A3A,1,0,0,0,100,100,0,0,3,16,0,9,0,0,0,1',
   'Style: LT1,Playfair Display,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,0,3,7,0,0,0,1',
   'Style: LT2,Inter,30,&H002E61B8,&H002E61B8,&H00000000,&H00000000,1,0,0,0,100,100,3,0,1,0,2,7,0,0,0,1',
   'Style: LTB,Inter,20,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1']
D=[]
a,b=ts(0.4),ts(4.6)
D+=[f'Dialogue: 0,{a},{b},LTB,,0,0,0,,{{\\pos(0,0)\\fad(400,400)\\1c&H2E4A3A&\\1a&H50&\\p1}}m 90 800 l 700 800 l 700 915 l 90 915{{\\p0}}',
    f'Dialogue: 0,{a},{b},LTB,,0,0,0,,{{\\pos(0,0)\\fad(400,400)\\1c&H2E61B8&\\p1}}m 90 800 l 98 800 l 98 915 l 90 915{{\\p0}}',
    f'Dialogue: 1,{a},{b},LT1,,0,0,0,,{{\\pos(122,804)\\fad(400,400)}}Stocked & Ready',
    f'Dialogue: 1,{a},{b},LT2,,0,0,0,,{{\\pos(126,872)\\fad(400,400)}}WITH CATHERINE REESE']
for k,(s,n,t) in enumerate(ITEMS):
    a=S[s]['s']; nxt=STOP.get(s, ITEMS[k+1][0] if k+1<len(ITEMS) else 154)
    b=S[nxt]['s']-0.2
    for x,y in clip(a,b):
        D.append(f'Dialogue: 2,{ts(x)},{ts(y)},LblN,,0,0,0,,{{\\pos(70,60)\\fad(250,250)}}{n.upper()}')
        D.append(f'Dialogue: 2,{ts(x)},{ts(y)},LblT,,0,0,0,,{{\\pos(70,112)\\fad(250,250)}}{t}')
for s,t in CALL:
    a=S[s]['s']+0.3; b=min(a+4.2,S[s]['e']+1.0)
    for x,y in clip(a,b): D.append(f'Dialogue: 3,{ts(x)},{ts(y)},Call,,0,0,0,,{{\\pos(1850,60)\\fad(300,300)}}{t}')
s=open('subs.ass').read().split('\n')
i=[k for k,l in enumerate(s) if l.startswith('Style: Cap')][0]
s[i+1:i+1]=L
open('subs.ass','w').write('\n'.join(s+D+['']))
print(len(D),'overlay lines')
