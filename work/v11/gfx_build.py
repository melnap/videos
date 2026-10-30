"""Build one standalone HyperFrames project per graphic (cream/olive/gold) and render it.
python3 gfx_build.py html | render"""
import json,os,re,sys,subprocess,shutil,html as H
from gfx import GFX
E=H.escape
S=json.load(open('sent.json')); W=json.load(open('words_cap.json')); SH=json.load(open('shots.json'))
norm=lambda x:re.sub(r'[^a-z0-9]','',x.lower())
def at(s,a):
    if a is None: return S[s]['s']
    for j in range(S[s]['w0'],S[s]['w1']+1):
        if norm(W[j]['w'])==a: return W[j]['s']
    raise SystemExit(f'anchor {s} {a}')
CSS='''
@font-face{font-family:"Inter";src:url("fonts/inter-latin-400-normal.woff2");font-weight:400}
@font-face{font-family:"Inter";src:url("fonts/inter-latin-600-normal.woff2");font-weight:600}
@font-face{font-family:"Inter";src:url("fonts/inter-latin-700-normal.woff2");font-weight:700}
@font-face{font-family:"Playfair Display";src:url("fonts/playfair-display-latin-600-normal.woff2");font-weight:600}
@font-face{font-family:"Playfair Display";src:url("fonts/playfair-display-latin-700-normal.woff2");font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden;background:#f6efe2}
#root{position:relative;width:1920px;height:1080px;overflow:hidden;font-family:"Inter",sans-serif}
.bg{position:absolute;inset:-60px;background-size:cover;background-position:center;filter:blur(18px) saturate(0.9)}
.wash{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,rgba(246,239,226,0.90) 0%,rgba(246,239,226,0.80) 55%,rgba(233,220,196,0.72) 100%)}
.wrap{position:absolute;left:0;right:0;top:110px;bottom:230px;display:flex;align-items:center;justify-content:center}
.gfx{width:1400px;color:#2a2418;display:flex;flex-direction:column;align-items:flex-start}
.kick{font:600 34px "Inter";letter-spacing:7px;text-transform:uppercase;color:#9a5226;margin-bottom:14px}
.title{font:700 92px/1.1 "Playfair Display";color:#4f6147}
.rule{width:240px;height:6px;background:#b8612e;margin:26px 0 44px;transform-origin:left center}
.rows{width:100%;display:flex;flex-direction:column;gap:26px}
.step{display:flex;align-items:center;gap:36px;font:600 64px/1.15 "Inter";color:#2a2418}
.compact .rows{flex-direction:row;gap:28px}
.compact .step{font-size:62px;padding:22px 38px;background:rgba(79,97,71,0.08);border-radius:10px}
.n{flex:none;width:92px;height:92px;border-radius:50%;background:#4f6147;color:#f6efe2;font:700 48px "Inter";display:flex;align-items:center;justify-content:center}
.n.ok{background:#6f8a3c;color:#fff}
.n.bad{background:#a8322a;color:#fff}
.tight .rows{gap:14px}
.tight .step{font-size:52px}
.tight .n{width:72px;height:72px;font-size:40px}
.n.q{background:transparent;border:4px solid #b8612e;color:#9a5226}
.card{display:flex;align-items:baseline;gap:30px;padding:26px 44px;background:rgba(79,97,71,0.08);border-left:8px solid #b8612e;border-radius:8px;width:100%}
.ck{font:600 52px "Inter";color:#6d6250;width:430px;flex:none}
.ca{font:700 52px "Inter";color:#b8612e}
.cv{font:700 60px "Inter";color:#2a2418}
.note{font:500 42px "Inter";color:#7a5e2a;margin-top:30px}
.cols{width:100%;display:flex;gap:44px}
.col{flex:1;padding:50px 56px;background:rgba(79,97,71,0.07);border-top:8px solid #6d6250;border-radius:10px}
.col.acc{border-top-color:#b8612e;background:rgba(184,97,46,0.12)}
.colh{font:600 40px "Inter";color:#6d6250;letter-spacing:3px;text-transform:uppercase}
.colbig{font:700 104px/1.1 "Playfair Display";color:#4f6147;margin-top:16px}
.quote .title{font-size:84px}
'''
def build(gid,st,du):
    g=GFX[gid]; ty=g['type']; rev=[]
    def rt(a):
        t=at(*a)-0.12-st
        return round(max(0.45,min(t,du-0.7)),3)
    body=''
    if ty in('steps','quote','check'):
        for i,r in enumerate(g['rows']):
            mark={'steps':f'<span class="n">{i+1}</span>','quote':'<span class="n q">›</span>','check':'<span class="n ok">✓</span>' if (ty!='check' or r[1]) else '<span class="n bad">✕</span>'}[ty]
            if ty=='steps' and g.get('compact'): mark=''
            txt,a=(r[0],r[2]) if ty=='check' else (r[0],r[1])
            body+=f'<div class="step" id="r{i}">{mark}<span>{E(txt)}</span></div>'; rev.append((f'#r{i}',rt(a)))
        body=f'<div class="rows">{body}</div>'
    elif ty=='card':
        for i,(k,v,a) in enumerate(g['rows']):
            body+=f'<div class="card" id="r{i}"><div class="ck">{E(k)}</div><div class="ca">→</div><div class="cv">{E(v)}</div></div>'; rev.append((f'#r{i}',rt(a)))
        body=f'<div class="rows">{body}</div>'
    elif ty=='compare':
        for i,c in enumerate(g['cols']):
            body+=f'<div class="col{" acc" if c.get("accent") else ""}" id="r{i}"><div class="colh">{E(c["head"])}</div><div class="colbig">{E(c["big"])}</div></div>'; rev.append((f'#r{i}',rt(c['a'])))
        body=f'<div class="cols">{body}</div>'
    if g.get('note'):
        body+=f'<div class="note" id="nt">{E(g["note"][0])}</div>'; rev.append(('#nt',rt(g['note'][1])))
    cls='gfx'+(' compact' if g.get('compact') else '')+(' tight' if g.get('compact_rows') else '')+(' quote' if ty=='quote' else '')
    js=[f'tl.fromTo(".bg",{{scale:1.0}},{{scale:1.06,duration:{du},ease:"none"}},0);',
        'tl.fromTo(".gfx",{opacity:0,y:30},{opacity:1,y:0,duration:0.5,ease:"power3.out"},0);',
        'tl.fromTo(".rule",{scaleX:0},{scaleX:1,duration:0.55,ease:"power2.out"},0.2);']
    for sel,t in rev: js.append(f'tl.fromTo("{sel}",{{opacity:0,x:-34}},{{opacity:1,x:0,duration:0.45,ease:"back.out(1.6)"}},{t});')
    js.append(f'tl.to(".gfx",{{opacity:0,duration:0.25}},{round(du-0.25,3)});')
    doc=f'''<!doctype html><html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{du}" data-width="1920" data-height="1080" data-fps="30">
<div class="clip" data-start="0" data-duration="{du}" data-track-index="0" style="position:absolute;inset:0"><div class="bg" style="background-image:url('{g["bg"]}')"></div><div class="wash"></div>
<div class="wrap"><div class="{cls}"><div class="kick">{E(g["kicker"])}</div><div class="title">{E(g["title"])}</div><div class="rule"></div>{body}</div></div></div>
</div><script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(js)}
window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = tl;
</script></body></html>'''
    d=f'hf/{gid}'; os.makedirs(d+'/fonts',exist_ok=True)
    open(d+'/index.html','w').write(doc)
    shutil.copy('/tmp/claude-0/hf/package/dist/gsap.min.js',d); shutil.copy(f'remotion/public/{g['bg']}',d)
    for f in os.listdir('remotion/public'):
        if f.endswith('.woff2'): shutil.copy('remotion/public/'+f,d+'/fonts/')
    for f in ('hyperframes.json','meta.json','package.json'): shutil.copy('/tmp/claude-0/hf/probe/'+f,d)
    return d
if __name__=='__main__':
    for s in SH:
        if s['kind']!='GFX': continue
        d=build(s['id'],s['t'],s['dur'])
        if 'render' in sys.argv:
            out=os.path.abspath(f'media/gfx/{s["id"]}.mp4'); os.makedirs('media/gfx',exist_ok=True)
            if not os.path.exists(out):
                r=subprocess.run(['npx','--yes','hyperframes@0.8.133','render','-o',out,'--crf','18'],cwd=d,capture_output=True,text=True)
                print(s['id'],'rc',r.returncode,r.stdout[-300:],r.stderr[-500:])
