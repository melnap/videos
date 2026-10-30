"""Quick check of a rebuilt video before sending it.
python qc_quick.py 16 -> loudness per minute of videos/..._v2.mp4 + one sheet with 4 frames of every changed shot (../_audit/vNN_changed.jpg)"""
import json, re, sys, subprocess, pathlib
from PIL import Image, ImageDraw
HERE = pathlib.Path(__file__).parent; v = sys.argv[1]
FF = str(HERE / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffmpeg.exe')
F = HERE / '..' / 'videos' / f'Stocked-and-Ready_Video{v}_v2.mp4'
e = subprocess.run([FF, '-hide_banner', '-nostats', '-i', str(F), '-af', 'ebur128=peak=true', '-vn', '-f', 'null', '-'], capture_output=True, text=True).stderr
I = re.findall(r'I:\s+(-?[\d.]+) LUFS', e)[-1]; pk = re.findall(r'Peak:\s+(-?[\d.]+) dBFS', e)[-1]
# short-term loudness every 0.1 s -> average per minute over voiced parts
M = [(float(t), float(s)) for t, s in re.findall(r't:\s*([\d.]+).*?S:\s*(-?[\d.]+)', e)]
mins = {}
for t, s in M:
    if s > -40: mins.setdefault(int(t // 60), []).append(s)
per = [sum(x) / len(x) for k, x in sorted(mins.items())]
print(f'V{v}_v2: {I} LUFS, peak {pk} dBFS; per minute: ' + ' '.join(f'{x:.1f}' for x in per) + f'  (spread {max(per) - min(per):.1f} LU)')
W = HERE / f'v{v}'
old = W / 'shots_before_audit.json'; new = json.load(open(W / 'shots.json'))
oldS = json.load(open(old)) if old.exists() else new
ch = [k for k, (a, b) in enumerate(zip(oldS, new)) if a['id'] != b['id']]
extra = {'13': [104], '14': [18, 111], '16': [2, 80, 127, 129], '17': [8, 29], '18': [41, 42]}.get(v, [])
ch = sorted(set(ch + [k for k in extra if k < len(new)])) + ['wave']
VO_END = new[-1]['t'] + new[-1]['dur']
tiles = []
for k in ch:
    t0, du, name = (VO_END, 3.0, 'wave') if k == 'wave' else (new[k]['t'], new[k]['dur'], f"#{k} {new[k]['id']}")
    fr = []
    for j, f in enumerate((0.05, 0.35, 0.65, 0.95)):
        o = HERE / '..' / '_audit' / f'q{v}_{k}_{j}.jpg'
        subprocess.run([FF, '-v', 'error', '-y', '-ss', f'{t0 + du * f:.2f}', '-i', str(F), '-frames:v', '1', '-vf', 'scale=320:180', str(o)])
        fr.append(o)
    tiles.append((name, fr))
im = Image.new('RGB', (4 * 320, len(tiles) * 200), 'white'); d = ImageDraw.Draw(im)
for r, (name, fr) in enumerate(tiles):
    d.text((4, r * 200 + 3), name, fill='black')
    for j, f in enumerate(fr):
        try: im.paste(Image.open(f), (j * 320, r * 200 + 18))
        except Exception: pass
im.save(HERE / '..' / '_audit' / f'v{v}_changed.jpg', quality=82)
print('changed shots checked:', len(tiles))
