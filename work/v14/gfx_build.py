"""Build one HyperFrames project per graphic (same look as V12) and snapshot or render it.
python gfx_build.py html      -> hf/<id>/index.html
python gfx_build.py snap      -> media/gfx_stills/<id>.png (fully revealed frame, for Melanie's review)
python gfx_build.py render    -> media/gfx/<id>.mp4"""
import json, os, re, sys, shutil, subprocess, pathlib, html as H
HERE = pathlib.Path(__file__).parent; os.chdir(HERE)
from gfx_v14 import GFX
E = H.escape
NODE = r'C:\Users\49c9\AppData\Local\Microsoft\WinGet\Packages\OpenJS.NodeJS.LTS_Microsoft.Winget.Source_8wekyb3d8bbwe\node-v24.20.0-win-x64'
FFDIR = str((HERE / '..' / '..' / '..' / 'tools' / 'ffmpeg' / 'bin').resolve())
ENV = dict(os.environ, PATH=NODE + os.pathsep + FFDIR + os.pathsep + os.environ['PATH'], HYPERFRAMES_TELEMETRY='0')
V12 = HERE / '..' / 'v12' / 'hf' / 'cereal'
S = json.load(open('sent.json', encoding='utf-8')); W = json.load(open('words.json', encoding='utf-8'))
SH = [s for s in json.load(open('shots.json')) if s['kind'] == 'GFX']
norm = lambda x: re.sub(r'[^a-z0-9]', '', x.lower())

def at(s, a):
    for w in W:
        if S[s]['s'] - 0.01 <= w['s'] <= S[s]['e'] + 0.01 and norm(w['w']) == a: return w['s']
    raise SystemExit(f'anchor not found: sentence {s} word {a}')

CSS = (V12 / 'index.html').read_text(encoding='utf-8').split('<style>')[1].split('</style>')[0] + '''
.colh{font:600 34px "Inter";letter-spacing:2px;text-transform:none}
.label .title{font-size:120px}
.label.small .title{font-size:76px;line-height:1.2}
'''

def build(gid, st, du):
    g = GFX[gid]; ty = g['type']; rev = []; body = ''
    def rt(a): return round(max(0.45, min(at(*a) - 0.12 - st, du - 1.2)), 3)
    if ty == 'card':
        for i, (k, v, a) in enumerate(g['rows']):
            body += f'<div class="card" id="r{i}"><div class="ck">{E(k)}</div><div class="ca">→</div><div class="cv">{E(v)}</div></div>'
            rev.append((f'#r{i}', rt(a)))
        body = f'<div class="rows">{body}</div>'
    elif ty == 'compare':
        for i, c in enumerate(g['cols']):
            body += f'<div class="col{" acc" if c.get("accent") else ""}" id="r{i}"><div class="colh">{E(c["head"])}</div><div class="colbig">{E(c["big"])}</div></div>'
            rev.append((f'#r{i}', rt(c['a'])))
        body = f'<div class="cols">{body}</div>'
    cls = 'gfx' + (' label' if ty == 'label' else '') + (' small' if g.get('small') else '')
    js = [f'tl.fromTo(".bg",{{scale:1.0}},{{scale:1.06,duration:{du},ease:"none"}},0);',
          'tl.fromTo(".gfx",{opacity:0,y:30},{opacity:1,y:0,duration:0.5,ease:"power3.out"},0);',
          'tl.fromTo(".rule",{scaleX:0},{scaleX:1,duration:0.55,ease:"power2.out"},0.2);']
    for sel, t in rev: js.append(f'tl.fromTo("{sel}",{{opacity:0,x:-34}},{{opacity:1,x:0,duration:0.45,ease:"back.out(1.6)"}},{t});')
    # full-screen graphic stays fully on screen until the cut (no fade-out before the next shot)
    doc = f'''<!doctype html><html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1920, height=1080" />
<script src="gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{du}" data-width="1920" data-height="1080" data-fps="30">
<div class="clip" data-start="0" data-duration="{du}" data-track-index="0" style="position:absolute;inset:0"><div class="bg" style="background-image:url('{g["bg"]}')"></div><div class="wash"></div>
<div class="wrap"><div class="{cls}"><div class="kick">{E(g["kicker"])}</div><div class="title">{E(g["title"])}</div><div class="rule"></div>{body}</div></div></div>
</div><script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(js)}
window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = tl;
</script></body></html>'''
    d = HERE / 'hf' / gid; (d / 'fonts').mkdir(parents=True, exist_ok=True)
    (d / 'index.html').write_text(doc, encoding='utf-8')
    for f in ('gsap.min.js', 'hyperframes.json', 'meta.json', 'package.json'): shutil.copy(V12 / f, d)
    for f in os.listdir(V12 / 'fonts'): shutil.copy(V12 / 'fonts' / f, d / 'fonts')
    shutil.copy(HERE / 'media' / 'gfx_bg.png', d / 'bg.png')
    return d, max([t for _, t in rev] + [0.6]) + 0.6

def hf(args, cwd):
    return subprocess.run(['npx.cmd', '--offline', 'hyperframes@0.8.133'] + args, cwd=cwd, env=ENV, capture_output=True, text=True)

if __name__ == '__main__':
    os.makedirs('media/gfx_stills', exist_ok=True); os.makedirs('media/gfx', exist_ok=True)
    only = [a for a in sys.argv[2:]]
    for s in SH:
        gid = s['id'][2:]
        if only and gid not in only: continue
        d, tfull = build(gid, s['t'], s['dur'])
        if sys.argv[1] == 'snap':
            r = hf(['snapshot', '--at', f'{min(tfull, s["dur"] - 0.1):.2f}', '--no-end', '-o', str(HERE / 'media' / 'gfx_stills' / gid), '--describe', 'false'], d)
            print(gid, 'snap rc', r.returncode, (r.stdout + r.stderr)[-300:] if r.returncode else '')
        if sys.argv[1] == 'render':
            out = HERE / 'media' / 'gfx' / f'{gid}.mp4'
            if not out.exists():
                r = hf(['render', '-o', str(out), '--crf', '18'], d)
                print(gid, 'render rc', r.returncode, (r.stdout + r.stderr)[-400:] if r.returncode else '')
