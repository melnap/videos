"""Add V17 to library/catalog.json: used_in for reused library clips and the new V17 clips."""
import json, re, shutil, subprocess, pathlib, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import assets_v17 as A
LIB = HERE / '..' / '..' / 'library'
FP = str(HERE / '..' / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffprobe.exe')
C = json.loads((LIB / 'catalog.json').read_text(encoding='utf-8'))
by = {c['id']: c for c in C}

def mark(cid, v):
    c = by.get(cid)
    if c is None: print('not in catalog:', cid); return
    if v not in c['used_in']: c['used_in'].append(v)

def norm(x):  # 'V5B01' -> 'V5_B01', 'V6ST34' -> 'V6_ST34'
    m = re.match(r'(V\d)_?([A-Z]+\d+.*)', x); return f'{m.group(1)}_{m.group(2)}' if m else x

shots = json.loads((HERE / 'shots.json').read_text())
reused = sorted({re.sub(r'\^$', '', s['id'])[2:] for s in shots if s['id'].startswith('L:')})
for i in reused: mark(i, 'V17')

SETS = {A.ISL: 'kitchen_island', A.STV: 'kitchen_stove', A.SNK: 'kitchen_sink', A.PAN: 'pantry', A.UTL: 'utility', A.GDN: 'garden'}
used_new = {re.sub(r'\^$', '', s['id']) for s in shots if s['kind'] in ('BRV', 'BRS') and not s['id'].startswith('L:')} | {'X42'}
added = 0
for k, kind, ref, prompt, *m in A.A:
    if k not in used_new: continue
    vid = HERE / 'media' / 'vid' / f'{k}.mp4'
    src = vid if vid.exists() else HERE / 'stills' / (k + '.png')
    cid = f'V17_{k}'; dst = LIB / 'clips' / f'{cid}{src.suffix}'
    shutil.copy(src, dst)
    d = round(float(subprocess.check_output([FP, '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(dst)]).decode()), 2) if src.suffix == '.mp4' else None
    desc = re.sub(r'^Realistic [^.]*?\. ', '', prompt).split(' Natural window light')[0].split(' Same room')[0]
    desc = desc.replace(A.ELEM, '').strip()
    entry = dict(id=cid, file=f'clips/{cid}{src.suffix}', desc=desc + (' ' + m[0] if m else ''), catherine=(k == 'X42'),
                 set=SETS.get(ref, 'other'), dur=d, used_in=['V17'], type='video' if src.suffix == '.mp4' else 'still',
                 source='Higgsfield', note='hair in a low bun, sage-green cardigan (V17)' if k == 'X42' else '')
    if cid in by: by[cid].update(entry)
    else: C.append(entry); by[cid] = entry
    added += 1
# Pixabay stock clips (S:) used in this video
META = json.loads((HERE / 'stock12_meta.json').read_text()) if (HERE / 'stock12_meta.json').exists() else {}
used_s = sorted({re.sub(r'\^$', '', s['id'])[2:] for s in shots if s['id'].startswith('S:')})
for k in used_s:
    m = META[k]; cid = f'PX_{k}'; dst = LIB / 'clips' / f'{cid}.mp4'
    shutil.copy(HERE / 'stock' / f'{k}.mp4', dst)
    entry = dict(id=cid, file=f'clips/{cid}.mp4', desc=f"Pixabay stock: {m.get('query','')}", catherine=False, set='stock',
                 dur=m.get('dur'), used_in=['V17'], type='video', source='Pixabay',
                 note=f"{m['url']} by {m['author']}, {m['license']}")
    if cid in by: by[cid].update(entry); by[cid]['used_in'] = sorted(set(by[cid]['used_in']) | {'V17'})
    else: C.append(entry); by[cid] = entry
    added += 1
(LIB / 'catalog.json').write_text(json.dumps(C, ensure_ascii=False, indent=1), encoding='utf-8')
print('reused', len(reused), 'new', added, 'total', len(C))
