"""V9 TH clip checks: duration, size, audio sync (xcorr vs mp3), motion, hand-strip motion."""
import numpy as np, subprocess, json, sys
sys.path.insert(0,'/home/user/stockedandready/work/v9')
from motion import energy
HAND='800:160:560:820'   # strip between hips and island edge (calibrated on V8: pass ~0.4-0.5, fail >=0.87)
MOUTH='240:120:880:270'
def probe(f):
    o=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=width,height,codec_type','-of','json',f]))
    v=[s for s in o['streams'] if s['codec_type']=='video'][0]
    return float(o['format']['duration']),v['width'],v['height']
def env(f,sr=100):
    raw=subprocess.check_output(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','16000','-f','s16le','-'])
    a=np.frombuffer(raw,np.int16).astype(np.float32)
    n=len(a)//160; return np.sqrt((a[:n*160].reshape(n,160)**2).mean(1)+1e-6)
def xcorr(a,b,maxlag):
    a=(a-a.mean())/a.std(); b=(b-b.mean())/b.std(); best=(-9,0)
    for L in range(-maxlag,maxlag+1):
        if L>=0: x,y=a[L:],b[:len(b)-L] if L else b
        else: x,y=a[:L],b[-L:]
        n=min(len(x),len(y)); c=float(np.dot(x[:n],y[:n])/n)
        if c>best[0]: best=(c,L)
    return best
res={}
import os
for i in range(1,13):
    if not os.path.exists("media/heygen/TH%02d.mp4"%i): continue
    n='TH%02d'%i; v=f'media/heygen/{n}.mp4'; m=f'th/{n}.mp3'
    dv,w,h=probe(v); dm=probe(m)[0] if False else float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',m]))
    c,L=xcorr(env(v),env(m),50)
    d=energy(v); hd=energy(v,HAND); md=energy(v,MOUTH)
    # mouth motion vs audio envelope (lip-sync) at 25 fps
    e=env(m,100); e25=e[:len(e)//4*4].reshape(-1,4).mean(1)[1:]
    k=min(len(e25),len(md)); mc,mL=xcorr(md[:k],e25[:k],10)
    # per 0.5s hand windows
    hw=[float(hd[j:j+12].mean()) for j in range(0,len(hd),12)]
    res[n]=dict(dur_v=round(dv,2),dur_mp3=round(dm,2),size=f'{w}x{h}',lag_s=round(L/100,2),corr=round(c,3),
                mouth_lag_s=round(mL/25,2),mouth_corr=round(mc,2),mean=round(float(d.mean()),3),p90=round(float(np.percentile(d,90)),3),
                hand=round(float(hd.mean()),3),hand_p90=round(float(np.percentile(hd,90)),3),hand_win=[round(x,2) for x in hw])
    r=res[n]; print(n,r['dur_v'],r['dur_mp3'],r['size'],'lag',r['lag_s'],'corr',r['corr'],'mouth',r['mouth_lag_s'],r['mouth_corr'],'mot',r['mean'],r['p90'],'hand',r['hand'],r['hand_p90'],flush=True)
json.dump(res,open('th_check.json','w'),indent=1)
