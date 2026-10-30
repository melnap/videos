"""Contact sheets for a visual audit: 3 frames (start/mid/end) of every shot, 2 shots per row, 12 shots per sheet.
python audit_sheets.py 16 -> ../_audit/v16/sheet_NN.jpg (frames from videos/Stocked-and-Ready_Video16.mp4)"""
import json, os, sys, subprocess, pathlib
from PIL import Image, ImageDraw
HERE = pathlib.Path(__file__).parent
v = sys.argv[1]; W = HERE / f'v{v}'
FF = str(HERE / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffmpeg.exe')
src = HERE / '..' / 'videos' / f'Stocked-and-Ready_Video{v}.mp4'
out = HERE / '..' / '_audit' / f'v{v}'; os.makedirs(out / 'f', exist_ok=True)
SH = json.load(open(W / 'shots.json'))
VO_END = SH[-1]['t'] + SH[-1]['dur']
SH = SH + [dict(t=VO_END, dur=3.0, id='WAVE (end)', kind='BR'), dict(t=VO_END + 3.0, dur=2.0, id='END CARD', kind='BR')]
TW, TH_ = 300, 169
def grab(t, p):
    if not p.exists():
        subprocess.run([FF, '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', str(src), '-frames:v', '1', '-vf', f'scale={TW}:{TH_}', str(p)])
    return p
rows = []
for k, s in enumerate(SH):
    ts = [s['t'] + s['dur'] * f for f in (0.12, 0.5, 0.88)]
    rows.append((k, s, [grab(t, out / 'f' / f's{k:03d}_{j}.jpg') for j, t in enumerate(ts)]))
per = 12
for n in range(0, len(rows), per):
    part = rows[n:n + per]; lines = (len(part) + 1) // 2
    im = Image.new('RGB', (2 * (3 * TW + 20), lines * (TH_ + 26)), 'white'); d = ImageDraw.Draw(im)
    for i, (k, s, fs) in enumerate(part):
        x0 = (i % 2) * (3 * TW + 20); y0 = (i // 2) * (TH_ + 26)
        m, sec = divmod(s['t'], 60)
        d.text((x0 + 4, y0 + 6), f"#{k}  {int(m)}:{sec:04.1f}  {s['id']}  ({s['dur']:.1f}s)", fill='black')
        for j, f in enumerate(fs):
            try: im.paste(Image.open(f).convert('RGB').resize((TW, TH_)), (x0 + j * TW, y0 + 24))
            except Exception: pass
    im.save(out / f'sheet_{n // per:02d}.jpg', quality=82)
print(v, len(rows), 'shots', (len(rows) + per - 1) // per, 'sheets')
