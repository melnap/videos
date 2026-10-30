"""Stocked & Ready V12 - ffmpeg edit.
python3 build.py precut [-j 4]  -> seg/sNNN.mp4 (1920x1080p30, exact duration, camera move baked in)
python3 build.py concat         -> out/video_raw.mp4"""
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
SH = json.load(open('shots.json')); TH = {t['id']: t for t in json.load(open('th_plan.json'))}
VO_END = 671.2; OUTRO = 5.0; WAVE = 3.0; FPS = 30
SKIP = {'A02': 1.4, 'A18': 1.3}
LIMIT = {'A03': 4.0}
SEG = 'seg'; os.makedirs(SEG, exist_ok=True); os.makedirs('out', exist_ok=True)

def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode())

def src_for(s):
    k, i = s['kind'], s['id']
    if k == 'TH': return f'media/heygen/{i}_fix.mp4'
    if k == 'GFX': return f'media/gfx/{i}.mp4'
    if k == 'CARD': return f'remotion/out/{i}.mp4'
    b = re.sub(r'[~^].*', '', i)
    if os.path.exists(f'media/vid/{b}.mp4'): return f'media/vid/{b}.mp4'
    if os.path.exists(f'stills/{b}.png'): return f'stills/{b}.png'
    for ext in ('.mp4', '.jpg'):
        if os.path.exists(f'stock/media/{b}{ext}'): return f'stock/media/{b}{ext}'
    raise SystemExit('missing ' + i)

def zp(move, N, still):
    a = 0.08 if still else 0.05
    p = f'(on/{max(N-1,1)})'
    if move == 'zin':  z, x, y = f'1+{a}*{p}', 'iw/2-iw/zoom/2', 'ih/2-ih/zoom/2'
    elif move == 'zout': z, x, y = f'1+{a}-{a}*{p}', 'iw/2-iw/zoom/2', 'ih/2-ih/zoom/2'
    elif move == 'panR': z, x, y = '1.12', f'(iw-iw/zoom)*(0.15+0.7*{p})', 'ih/2-ih/zoom/2'
    elif move == 'panL': z, x, y = '1.12', f'(iw-iw/zoom)*(0.85-0.7*{p})', 'ih/2-ih/zoom/2'
    elif move == 'tightL': z, x, y = f'1.30+0.05*{p}', '(iw-iw/zoom)*0.30', '(ih-ih/zoom)*0.42'
    elif move == 'tightR': z, x, y = f'1.30+0.05*{p}', '(iw-iw/zoom)*0.70', '(ih-ih/zoom)*0.42'
    elif move == 'thclose': z, x, y = '1.30', 'iw/2-iw/zoom/2', '(ih-ih/zoom)*0.15'
    elif move == 'thpush': z, x, y = f'1+0.14*{p}', 'iw/2-iw/zoom/2', '(ih-ih/zoom)*0.15'
    else: return None
    return f"zoompan=z='{z}':x='{x}':y='{y}':d=1:s=1920x1080:fps={FPS}"

COVER = 'scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080,setsar=1'
BIG = 'scale=3840:2160:force_original_aspect_ratio=increase:flags=lanczos,crop=3840:2160,setsar=1'

def job(k, s, offsets):
    out = f'{SEG}/s{k:03d}.mp4'
    if os.path.exists(out): return
    src = src_for(s); du = s['dur']
    if not os.path.exists(src): print('skip (missing)', k, src); return
    N = round(du * FPS); still = src.endswith(('.png', '.jpg'))
    mv = zp(s.get('move', 'none'), N, still)
    if still:
        vf = f'{BIG},{mv}' if mv else COVER
        cmd = ['ffmpeg','-v','error','-y','-loop','1','-framerate',str(FPS),'-i',src,'-frames:v',str(N),'-vf',vf]
    else:
        ms = offsets
        if ms > dur(src) - 1.0: ms = 0.2  # offset past the clip end (reused + split short clip): start from the top
        b = re.sub(r'[~^].*', '', s['id'])
        avail = min(dur(src), LIMIT.get(b, 99)) - ms; pre = ''
        if avail < du - 0.05 and s['kind'] not in ('TH',):
            rate = max(0.55, avail / du); pre = f'setpts=PTS/{rate:.4f},'
        base = f'{pre}fps={FPS},' + (f'{BIG},{mv}' if mv else COVER)
        cmd = ['ffmpeg','-v','error','-y','-ss',f'{ms:.3f}','-i',src,'-an','-vf',base+',tpad=stop_mode=clone:stop_duration=10','-frames:v',str(N)]
    if s['kind'] == 'CARD': cmd[cmd.index('-vf')+1] += ',fade=in:st=0:d=0.35:color=0xfff3e0'
    cmd += ['-c:v','libx264','-preset','fast','-crf','17','-pix_fmt','yuv420p','-r',str(FPS),out+'.tmp.mp4']
    subprocess.run(cmd, check=True); os.rename(out+'.tmp.mp4', out)

def offsets():
    """media start per shot: stock videos skip 0.5 s; split pieces continue where the previous piece stopped."""
    res = []; prev = {}
    for k, s in enumerate(SH):
        i = s['id']; b = re.sub(r'[~^].*', '', i)
        if s['kind'] == 'TH': res.append(s.get('ms', 0.0)); continue
        if s['kind'] != 'BR': res.append(0.0); continue
        if '^' in i: o = prev.get(b, 0.5)
        elif '~' in i: o = 1.6
        else: o = 0.5 if not (b[0] in 'MD' and b[1].isdigit()) else 0.0
        o = max(o, SKIP.get(b, 0.0))
        res.append(o); prev[b] = o + s['dur']
    return res

if __name__ == '__main__':
    if 'precut' in sys.argv:
        offs = offsets()
        jobs = [(k, s, offs[k]) for k, s in enumerate(SH)]
        # wave only after the voiceover has ended (Catherine must not wave while the VO is still talking)
        jobs.append((len(SH), dict(kind='BR', id='Q03', dur=WAVE, move='none'), 1.2))
        jobs.append((len(SH)+1, dict(kind='CARD', id='endcard', dur=OUTRO-WAVE, move='none'), 0.0))
        with ThreadPoolExecutor(int(sys.argv[sys.argv.index('-j')+1]) if '-j' in sys.argv else 4) as ex:
            for f in [ex.submit(job, *j) for j in jobs]: f.result()
        print('precut done', len(jobs))
    if 'concat' in sys.argv:
        n = len(SH) + 2
        open('seg/list.txt','w').write(''.join(f"file 's{k:03d}.mp4'\n" for k in range(n)))
        subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','seg/list.txt','-c','copy','out/video_raw.mp4'], check=True)
        print('raw', dur('out/video_raw.mp4'))
