"""Measure movement per region of a HeyGen talking-head clip.
Prints the peak frame-to-frame change in the arm/hand zone (lower half, outside the face) and in the head zone.
A clip is 'calm' when the arm zone stays low (< ~4) for the whole clip."""
import subprocess, sys, pathlib, numpy as np
FF = pathlib.Path(__file__).parent / '..' / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffmpeg.exe'
W, H = 192, 108
def frames(p):
    raw = subprocess.run([str(FF), '-v', 'error', '-i', p, '-vf', f'fps=10,scale={W}:{H},format=gray', '-f', 'rawvideo', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
for p in sys.argv[1:]:
    f = frames(p); d = np.abs(np.diff(f, axis=0))
    arms = d[:, 52:100, 20:172].mean(axis=(1, 2))
    head = d[:, 5:45, 75:117].mean(axis=(1, 2))
    i = int(arms.argmax())
    print(f'{pathlib.Path(p).name}: arms max {arms.max():.2f} at {i/10:.1f}s, arms mean {arms.mean():.2f}, head max {head.max():.2f}')
