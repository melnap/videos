"""Synthesize 7 soft, different transition sounds with ffmpeg (no downloads, no licences needed).
Each graphic gets the next one in turn, so the same sound never repeats within 6 uses."""
import subprocess, pathlib
HERE = pathlib.Path(__file__).parent
FF = str(HERE / '..' / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffmpeg.exe')
OUT = HERE / 'audio'; OUT.mkdir(exist_ok=True)
# (name, source, filter) – filtered noise "air" whooshes and soft wooden/paper taps
V = [
 ('sfx1', 'anoisesrc=color=pink:duration=0.6:amplitude=0.5', 'highpass=f=500,lowpass=f=3500,afade=t=in:d=0.25,afade=t=out:st=0.3:d=0.3'),
 ('sfx2', 'anoisesrc=color=brown:duration=0.5:amplitude=0.6', 'highpass=f=300,lowpass=f=2200,afade=t=in:d=0.12,afade=t=out:st=0.15:d=0.35'),
 ('sfx3', 'sine=frequency=880:duration=0.35', 'volume=0.5,afade=t=out:st=0.02:d=0.33,aecho=0.6:0.4:40:0.25'),
 ('sfx4', 'anoisesrc=color=white:duration=0.45:amplitude=0.3', 'bandpass=f=2500:width_type=o:w=1.5,afade=t=in:d=0.2,afade=t=out:st=0.2:d=0.25'),
 ('sfx5', 'sine=frequency=520:duration=0.3', 'volume=0.45,afade=t=out:st=0.01:d=0.29'),
 ('sfx6', 'anoisesrc=color=pink:duration=0.8:amplitude=0.4', 'highpass=f=800,lowpass=f=5000,afade=t=in:d=0.4,afade=t=out:st=0.4:d=0.4'),
 ('sfx7', 'anoisesrc=color=brown:duration=0.25:amplitude=0.8', 'lowpass=f=1200,afade=t=out:st=0.02:d=0.23'),
]
for n, src, flt in V:
    subprocess.run([FF, '-v', 'error', '-y', '-f', 'lavfi', '-i', src, '-af', flt + ',aformat=channel_layouts=stereo', '-ar', '48000', str(OUT / f'{n}.wav')], check=True)
print('made', len(V))
