"""Even out the voice: bring each ElevenLabs part to the same loudness and brightness, then rebuild vo.wav.

python vo_level.py v16        -> v16/vo.wav (old one kept as v16/vo_before_level.wav)
Same assembly as vo_make.py (part1 + 0.6 s + part2 + 0.6 s + part3, tempo x1.08, -16 LUFS), so all timings stay identical.
Extra: per-part gain to the same loudness, a small treble correction per part (max +-2.5 dB at 4 kHz),
and a gentle compressor (ratio 2) that evens out level changes inside a part."""
import re, sys, shutil, subprocess, pathlib
import numpy as np

W = pathlib.Path(__file__).parent / sys.argv[1]
FF = str(pathlib.Path(__file__).parent / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffmpeg.exe')
FP = FF.replace('ffmpeg.exe', 'ffprobe.exe')
TARGET = -16.0
PARTS = [W / f'vo_part{i}.mp3' for i in (1, 2, 3)]

def run(args):
    return subprocess.run([FF, '-hide_banner', '-y', *args], capture_output=True, text=True)

def lufs(p, extra=()):
    r = run([*extra, '-i', str(p), '-af', 'ebur128', '-f', 'null', '-'])
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r.stderr)[-1])

def dur(p):
    return float(subprocess.check_output([FP, '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)]).decode())

def bright(p):
    raw = subprocess.run([FF, '-v', 'error', '-i', str(p), '-ac', '1', '-ar', '44100', '-f', 'f32le', '-'], capture_output=True).stdout
    x = np.frombuffer(raw, np.float32); n = 4096; f = np.fft.rfftfreq(n, 1 / 44100)
    P = np.mean([np.abs(np.fft.rfft(x[k:k + n] * np.hanning(n))) ** 2 for k in range(0, len(x) - n, n) if np.abs(x[k:k + n]).mean() > 0.02], axis=0)
    band = lambda a, b: 10 * np.log10(P[(f >= a) & (f < b)].mean())
    return band(4000, 10000) - band(500, 2000)

old = W / 'vo.wav'
expect = (sum(dur(p) for p in PARTS) + 1.2) / 1.08
assert abs(dur(old) - expect) < 0.15, f'vo.wav {dur(old):.2f}s was not built the standard way (expected {expect:.2f}s) - stop'

L = [lufs(p) for p in PARTS]; B = [bright(p) for p in PARTS]; ref = sum(L) / 3; bref = sum(B) / 3
filt = []
for i in range(3):
    g = ref - L[i]; t = max(-2.5, min(2.5, bref - B[i]))
    filt.append(f'[{i}:a]aresample=48000,aformat=channel_layouts=mono,volume={g:.2f}dB,treble=g={t:.2f}:f=4000:t=s:w=0.7[a{i}]')
    print(f'part{i + 1}: {L[i]:.1f} LUFS -> gain {g:+.1f} dB, brightness {B[i]:.1f} dB -> treble {t:+.1f} dB')
fc = (';'.join(filt) + ';anullsrc=r=48000:cl=mono:d=0.6[g1];anullsrc=r=48000:cl=mono:d=0.6[g2];'
      '[a0][g1][a1][g2][a2]concat=n=5:v=0:a=1,atempo=1.08,acompressor=threshold=-26dB:ratio=2:attack=15:release=300:makeup=1,'
      'dynaudnorm=f=2000:g=21:m=4:p=0.9:r=0.2[o]')   # slow leveling over ~40 s: evens out minute-to-minute changes without pumping
ins = sum((['-i', str(p)] for p in PARTS), [])
pre = W / 'vo_pre_level.wav'
r = run([*ins, '-filter_complex', fc, '-map', '[o]', '-c:a', 'pcm_s16le', str(pre)]); assert r.returncode == 0, r.stderr[-800:]

if not (W / 'vo_before_level.wav').exists(): shutil.copy(old, W / 'vo_before_level.wav')
gain = TARGET - lufs(pre)
for _ in range(3):
    r = run(['-i', str(pre), '-af', f'volume={gain:.2f}dB,alimiter=limit=0.891:level=disabled', '-c:a', 'pcm_s16le', str(old)]); assert r.returncode == 0
    miss = TARGET - lufs(old)
    if abs(miss) < 0.3: break
    gain += miss
d = dur(old); third = d / 3
parts = [lufs(old, ['-ss', f'{k * third:.2f}', '-t', f'{third:.2f}']) for k in range(3)]
print(f'vo.wav {lufs(old):.1f} LUFS, {d:.2f}s (before {dur(W / "vo_before_level.wav"):.2f}s), thirds: ' + ' / '.join(f'{x:.1f}' for x in parts))
