"""Bring out/mix.m4a to -14 LUFS with true peak below -1.0 dB after AAC encoding (single-pass loudnorm overshot on V15,
AAC re-encode overshot a hard consonant on V16, so the limiter ceiling is lowered until the encoded file is safe)."""
import re, subprocess, shutil, pathlib
HERE = pathlib.Path(__file__).parent
FF = str(HERE / '..' / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffmpeg.exe')
src = HERE / 'out' / 'mix_raw.m4a'
if not src.exists(): shutil.move(HERE / 'out' / 'mix.m4a', src)
def meas(p):
    e = subprocess.run([FF, '-hide_banner', '-i', str(p), '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', e)[-1]), float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS', e)[-1])
gain = -14.0 - meas(src)[0]; limit = 0.79
for _ in range(8):
    subprocess.run([FF, '-v', 'error', '-y', '-i', str(src), '-af', f'volume={gain:.2f}dB,alimiter=limit={limit:.3f}:level=disabled:attack=1:release=50',
                    '-ar', '48000', '-c:a', 'aac', '-b:a', '256k', str(HERE / 'out' / 'mix.m4a')], check=True)
    i, p = meas(HERE / 'out' / 'mix.m4a')
    print(f'gain {gain:+.2f}, limit {limit:.2f} -> {i:.1f} LUFS, peak {p:.1f} dBFS')
    ok_i, ok_p = abs(i + 14) < 0.2, p <= -1.0
    if ok_i and ok_p: break
    if not ok_p: limit *= 0.89
    if not ok_i: gain += -14.0 - i
