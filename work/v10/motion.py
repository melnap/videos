"""Motion energy per 0.5 s window (mean abs frame diff on grayscale 160x90)."""
import numpy as np, subprocess, sys
def energy(f, crop=None):
    vf='scale=160:90,format=gray' if not crop else f'crop={crop},scale=160:90,format=gray'
    raw=subprocess.check_output(['ffmpeg','-v','error','-i',f,'-vf',vf,'-f','rawvideo','-'])
    a=np.frombuffer(raw,np.uint8).reshape(-1,90,160).astype(np.float32)
    d=np.abs(np.diff(a,axis=0)).mean(axis=(1,2))
    return d  # per frame
if __name__=='__main__':
    for f in sys.argv[1:]:
        d=energy(f); fps=25 if 'iii' in f else 25
        print(f, 'mean %.3f  p90 %.3f'%(d.mean(), np.percentile(d,90)))
