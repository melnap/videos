"""V10 overlays on top of the karaoke subs: channel lower third, item labels (n/15, Wait on n/5), storage callouts. Hidden while a full-screen graphic runs."""
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
ITEMS=[(21,'1/20','Check the temperature'),(31,'2/20','Fill the empty space'),(39,'3/20','Air is the enemy'),(51,'4/20','Freeze in the size you cook'),(58,'5/20','A list on the door'),
 (69,'6/20','Cranberries'),(80,'7/20','A second turkey'),(86,'8/20','Leftover turkey, in broth'),(93,'9/20','Holiday ham, in small pieces'),(99,'10/20','Soup in 2-cup portions'),
 (106,'11/20','Baked cookies, made early'),(113,'12/20','Which meat to eat first'),(121,'13/20','The short-timers'),
 (131,'14/20','Eggs in the shell & mayo'),(137,'15/20','Salad greens'),(145,'16/20','Unopened cans'),
 (152,'17/20','Thaw it in the fridge'),(161,'18/20','The refreezing rule'),(168,'19/20','The coin in a cup'),(177,'20/20','Power out: keep it shut')]
STOP={58:67,113:121,121:129,145:150,177:186}
CALL=[(28,'Appliance thermometer: a few dollars'),(37,'Leave 1 inch at the top'),(54,'5 × 1-lb bags'),(82,'Whole turkey: about 1 year'),
 (95,'Cooked ham: 1–2 months'),(101,'Soups & stews: 2–3 months'),(103,'Leave about 1 inch'),(109,'Baked cookies: 8–12 months'),(112,'Thaws in about 15 min'),
 (136,'Mayo salads: fridge, 3–5 days'),(164,'Thawed in the fridge: may refreeze'),(166,'Cold water or microwave: cook first'),(182,'Ice crystals or ≤ 40 °F: may refreeze')]
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
    a=S[s]['s']; nxt=STOP.get(s, ITEMS[k+1][0] if k+1<len(ITEMS) else 186)
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
