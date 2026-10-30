"""Cut one mp3 per talking head from vo.wav (0.3 s pad each side) and write th_upload.json for the HeyGen batch."""
import json, pathlib, subprocess, hashlib

HERE = pathlib.Path(__file__).parent
FF = HERE / '..' / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffmpeg.exe'
PAD = 0.3
plan = json.loads((HERE / 'th_plan.json').read_text())
files = []
for t in plan:
    a = max(0.0, t['s'] - PAD); b = t['e'] + PAD
    t['as'] = round(a, 3)  # audio start on the VO timeline (needed to line the clip up later)
    out = HERE / 'media' / 'th' / f"V18_{t['id']}.mp3"
    subprocess.run([str(FF), '-hide_banner', '-loglevel', 'error', '-y', '-ss', f'{a:.3f}', '-to', f'{b:.3f}',
                    '-i', str(HERE / 'vo.wav'), '-ac', '1', '-ar', '44100', '-b:a', '192k', str(out)], check=True)
    files.append({'filename': out.name, 'content_type': 'audio/mpeg', 'size_bytes': out.stat().st_size,
                  'checksum_sha256': hashlib.sha256(out.read_bytes()).hexdigest(), 'path': str(out)})
img = HERE / 'media' / 'th' / 'V18_TH_base_a.png'
files.append({'filename': 'V18_TH_base.png', 'content_type': 'image/png', 'size_bytes': img.stat().st_size,
              'checksum_sha256': hashlib.sha256(img.read_bytes()).hexdigest(), 'path': str(img)})
(HERE / 'th_plan.json').write_text(json.dumps(plan, indent=1))
(HERE / 'th_upload.json').write_text(json.dumps(files, indent=1))
print(len(files), 'files'); print(round(sum(t['e'] - t['s'] for t in plan), 1), 's talking head')
