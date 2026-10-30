"""List time windows where the lower body/hand zone moves (possible gesture)."""
import subprocess, sys, pathlib, numpy as np
FF = pathlib.Path(__file__).parent / '..' / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffmpeg.exe'
W, H = 192, 108
for p in sys.argv[1:]:
    raw = subprocess.run([str(FF), '-v', 'error', '-i', p, '-vf', f'fps=10,scale={W}:{H},format=gray', '-f', 'rawvideo', '-'], capture_output=True, check=True).stdout
    f = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
    ref = np.median(f[:, 52:100, 20:172], axis=0)          # resting pose
    dev = np.abs(f[:, 52:100, 20:172] - ref).mean(axis=(1, 2))  # distance from resting pose
    hot = dev > 3.0
    wins, s = [], None
    for i, h in enumerate(hot):
        if h and s is None: s = i
        if not h and s is not None: wins.append((s / 10, i / 10)); s = None
    if s is not None: wins.append((s / 10, len(hot) / 10))
    print(f'{pathlib.Path(p).name}: max dev {dev.max():.1f}  windows {wins}')
