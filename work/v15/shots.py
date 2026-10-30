"""Turn beats.py into shots.json (one entry per cut) and check the edit rules.
Rules checked: talking heads 18-22 %, TH clip covers its span, max 2 uses per asset, max 2 stills in a row,
graphics <= 8.5 s, no B-roll shorter than 1.2 s, alternating TH sizes."""
import json, pathlib, re, subprocess
HERE = pathlib.Path(__file__).parent
exec((HERE / 'beats.py').read_text(encoding='utf-8'))
S = json.loads((HERE / 'sent.json').read_text(encoding='utf-8'))
TH = {t['id']: t for t in json.loads((HERE / 'th_plan.json').read_text())}
FFPROBE = HERE / '..' / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffprobe.exe'
VO_END = S[-1]['e'] + 0.35
VIDS = {'P05', 'P07', 'P16', 'P18', 'P20', 'P21', 'P42'}
LIB = HERE / '..' / '..' / 'library' / 'clips'

def dur(p):
    return float(subprocess.run([str(FFPROBE), '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True).stdout)

def base(i): return re.sub(r'\^$', '', i.split('#')[0])

def kind(i):
    if i.startswith('TH'): return 'TH'
    if i.startswith('G:'): return 'GFX'
    b = base(i)
    if b.startswith('L:'):
        return 'BRV' if (LIB / (b[2:] + '.mp4')).exists() else 'BRS'
    return 'BRV' if b in VIDS else 'BRS'

def start(b):
    t = b[0]
    return float(t) if isinstance(t, float) else round(S[t]['s'] - 0.05, 3)

shots = []
for k, b in enumerate(BEATS):
    a = start(b); e = start(BEATS[k + 1]) if k + 1 < len(BEATS) else VO_END
    n = len(b[1])
    for j, it in enumerate(b[1]):
        mv = it.split('#')[1] if '#' in it else None; it = it.split('#')[0]
        shots.append(dict(t=round(a + (e - a) * j / n, 3), id=it, kind=kind(it), force=mv))
for n, o in enumerate(shots):
    o['dur'] = round((shots[n + 1]['t'] if n + 1 < len(shots) else VO_END) - o['t'], 3)
# a talking head never runs past the end of its rendered clip: cut to the next shot earlier instead of freezing
for n, o in enumerate(shots):
    if o['id'].startswith('TH') and n + 1 < len(shots):
        p = TH[o['id']]; cd = dur(HERE / 'media' / 'heygen' / (o['id'] + '.mp4'))
        end = p['as'] + cd - 0.04
        if o['t'] + o['dur'] > end:
            shots[n + 1]['t'] = round(end, 3); o['dur'] = round(end - o['t'], 3)
            nx = shots[n + 1]; nx['dur'] = round((shots[n + 2]['t'] if n + 2 < len(shots) else VO_END) - nx['t'], 3)
last = shots[-1]
if last['id'].startswith('TH'):   # the final talking head also ends where its clip ends
    p = TH[last['id']]; end = p['as'] + dur(HERE / 'media' / 'heygen' / (last['id'] + '.mp4')) - 0.04
    last['dur'] = round(min(last['dur'], end - last['t']), 3)

# camera moves: B-roll alternates gentle zoom/pan; TH alternates wide / close (~130 %) / slow push
MOVES = ['zin', 'panR', 'zout', 'panL']; TM = ['none', 'thclose', 'thpush', 'thclose']; mv = tm = 0
for o in shots:
    if o['kind'] in ('BRV', 'BRS'): o['move'] = MOVES[mv % 4]; mv += 1
    elif o['kind'] == 'TH':
        o['move'] = o['force'] or TM[tm % 4]; tm += 1
        p = TH[o['id']]; o['ms'] = round(o['t'] - p['as'], 3)
    else: o['move'] = 'none'
(HERE / 'shots.json').write_text(json.dumps(shots, indent=0))

# ---- checks
err = []
th = sum(o['dur'] for o in shots if o['kind'] == 'TH')
print(f'{len(shots)} shots, VO end {VO_END:.2f}s, talking heads {th:.1f}s = {100 * th / VO_END:.1f} %')
if not 18 <= 100 * th / VO_END <= 22: err.append('TH share out of range')
for o in shots:
    if o['kind'] == 'TH':
        cd = dur(HERE / 'media' / 'heygen' / (o['id'] + '.mp4'))
        if o['ms'] < -0.01 or o['ms'] + o['dur'] > cd + 0.05: err.append(f"{o['id']} span {o['ms']:.2f}+{o['dur']:.2f} outside clip {cd:.2f}")
    if o['kind'] == 'GFX' and o['dur'] > 9.1: err.append(f"graphic {o['id']} {o['dur']:.1f}s too long")
    if o['kind'] != 'TH' and o['dur'] < 1.2: err.append(f"short shot {o['id']} {o['dur']:.2f}s at {o['t']:.1f}")
uses = {}
for o in shots:
    if o['kind'] in ('BRV', 'BRS'): uses[base(o['id'])] = uses.get(base(o['id']), 0) + 1
err += [f'{k} used {v}x' for k, v in uses.items() if v > 2]
run = 0
for o in shots:
    run = run + 1 if o['kind'] == 'BRS' else 0
    if run > 2: err.append(f"3 stills in a row ending {o['id']} at {o['t']:.1f}")
prev = None
for o in shots:
    if o['kind'] == 'TH':
        if prev and prev['move'] == o['move'] and o['move'] == 'none': err.append(f"same TH size twice {prev['id']}/{o['id']}")
        prev = o
print('\n'.join(err) if err else 'ALL CHECKS PASSED')
