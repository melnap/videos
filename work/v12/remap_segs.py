"""Reuse already rendered segments after the shot list changed: segments are named by index, so move every
segment whose shot (id, t, dur, move, ms) is unchanged to its new index; everything else gets re-rendered."""
import json, os, subprocess, sys
os.chdir(sys.argv[1])
old = json.loads(subprocess.check_output(['git', 'show', f'HEAD:work/{os.path.basename(os.getcwd())}/shots.json']))
new = json.load(open('shots.json'))
key = lambda o: (o['id'], round(o['t'], 3), round(o['dur'], 3), o.get('move'), o.get('ms'))
pos = {key(o): j for j, o in enumerate(old)}
os.makedirs('seg_old', exist_ok=True)
for f in os.listdir('seg'):
    if f.startswith('s') and f.endswith('.mp4'): os.rename(f'seg/{f}', f'seg_old/{f}')
kept = 0
for k, o in enumerate(new):
    j = pos.get(key(o))
    if j is not None and os.path.exists(f'seg_old/s{j:03d}.mp4'):
        os.rename(f'seg_old/s{j:03d}.mp4', f'seg/s{k:03d}.mp4'); kept += 1
# wave + endcard segments sit right after the last shot
for d in (0, 1):
    if os.path.exists(f'seg_old/s{len(old)+d:03d}.mp4'): os.rename(f'seg_old/s{len(old)+d:03d}.mp4', f'seg/s{len(new)+d:03d}.mp4'); kept += 1
print('kept', kept, 'of', len(new) + 2)
