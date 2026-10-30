"""Build vo.wav: part1 + 0.6 s + part2 + 0.6 s + part3, tempo x1.08, about -16 LUFS, 48 kHz mono."""
import json, re, subprocess, pathlib

HERE = pathlib.Path(__file__).parent
FF = HERE / '..' / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffmpeg.exe'
TARGET = -16.0

def run(args):
    return subprocess.run([str(FF), '-hide_banner', '-y', *args], capture_output=True, text=True)

ins = []
for i in (1, 2, 3):
    ins += ['-i', str(HERE / f'vo_part{i}.mp3')]
fc = ('anullsrc=r=48000:cl=mono:d=0.6[g1];anullsrc=r=48000:cl=mono:d=0.6[g2];'
      '[0:a]aresample=48000,aformat=channel_layouts=mono[a0];[1:a]aresample=48000,aformat=channel_layouts=mono[a1];'
      '[2:a]aresample=48000,aformat=channel_layouts=mono[a2];'
      '[a0][g1][a1][g2][a2]concat=n=5:v=0:a=1,atempo=1.08[o]')
r = run([*ins, '-filter_complex', fc, '-map', '[o]', '-c:a', 'pcm_s16le', str(HERE / 'vo_pre.wav')])
assert r.returncode == 0, r.stderr[-800:]

def lufs(p):
    r = run(['-i', str(p), '-af', 'ebur128', '-f', 'null', '-'])
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r.stderr)[-1])

gain = TARGET - lufs(HERE / 'vo_pre.wav')
for _ in range(3):  # the limiter eats some loudness, so correct up to 3 times
    r = run(['-i', str(HERE / 'vo_pre.wav'), '-af',
             f'volume={gain:.2f}dB,alimiter=limit=0.891:level=disabled', '-c:a', 'pcm_s16le', str(HERE / 'vo.wav')])
    assert r.returncode == 0, r.stderr[-800:]
    miss = TARGET - lufs(HERE / 'vo.wav')
    if abs(miss) < 0.3: break
    gain += miss
print(f'gain {gain:+.2f} dB -> vo.wav {lufs(HERE / "vo.wav"):.1f} LUFS')
