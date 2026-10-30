"""Stocked & Ready V14 edit with ffmpeg (graphics rendered by HyperFrames).
python build13.py precut   -> seg/sNNN.mp4, each shot 1920x1080p30 with its exact length and a calm camera move
python build13.py concat   -> out/video_raw.mp4
python build13.py mix      -> out/mix.m4a (VO + quiet varied SFX, -14 LUFS, no music)
python build13.py final    -> out/Stocked-and-Ready_Video14.mp4 (grade, burned karaoke captions)"""
import json, os, re, subprocess, sys, pathlib
from concurrent.futures import ThreadPoolExecutor
HERE = pathlib.Path(__file__).parent; os.chdir(HERE)
FF = str((HERE / '..' / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffmpeg.exe').resolve())
FP = FF.replace('ffmpeg.exe', 'ffprobe.exe')
LIB = (HERE / '..' / '..' / 'library' / 'clips').resolve()
SH = json.load(open('shots.json'))
S = json.load(open('sent.json', encoding='utf-8'))
VO_END = SH[-1]['t'] + SH[-1]['dur']; WAVE = 3.0; CARD = 2.0; FPS = 30
TOTAL = VO_END + WAVE + CARD
TIGHT = {}   # crop away background details
WAVE_START = 1.0     # the part of N42 with the wave
os.makedirs('seg', exist_ok=True); os.makedirs('out', exist_ok=True)

def dur(f): return float(subprocess.check_output([FP, '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(f)]).decode())
def base(i): return re.sub(r'\^$', '', i)

def src_for(s):
    k, i = s['kind'], base(s['id'])
    if k == 'TH': return f'media/heygen/{i}.mp4'
    if k == 'GFX': return f'media/gfx/{i[2:]}.mp4'
    if i.startswith('L:'):
        for ext in ('.mp4', '.png'):
            if (LIB / (i[2:] + ext)).exists(): return str(LIB / (i[2:] + ext))
    if os.path.exists(f'media/vid/{i}.mp4'): return f'media/vid/{i}.mp4'
    if i == 'N40': return 'stills/M20.png'
    return f'stills/{i}.png'

def zp(move, N, still):
    a = 0.08 if still else 0.05; p = f'(on/{max(N - 1, 1)})'
    m = {'zin': (f'1+{a}*{p}', 'iw/2-iw/zoom/2', 'ih/2-ih/zoom/2'),
         'zout': (f'1+{a}-{a}*{p}', 'iw/2-iw/zoom/2', 'ih/2-ih/zoom/2'),
         'panR': ('1.12', f'(iw-iw/zoom)*(0.15+0.7*{p})', 'ih/2-ih/zoom/2'),
         'panL': ('1.12', f'(iw-iw/zoom)*(0.85-0.7*{p})', 'ih/2-ih/zoom/2'),
         'tightL': (f'1.30+0.05*{p}', '(iw-iw/zoom)*0.30', '(ih-ih/zoom)*0.42'),
         'tightR': (f'1.30+0.05*{p}', '(iw-iw/zoom)*0.70', '(ih-ih/zoom)*0.42'),
         'thclose': ('1.30', 'iw/2-iw/zoom/2', '(ih-ih/zoom)*0.15'),
         'thpush': (f'1+0.14*{p}', 'iw/2-iw/zoom/2', '(ih-ih/zoom)*0.15')}.get(move)
    if not m: return None
    return f"zoompan=z='{m[0]}':x='{m[1]}':y='{m[2]}':d=1:s=1920x1080:fps={FPS}"

COVER = 'scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080,setsar=1'
BIG = 'scale=3840:2160:force_original_aspect_ratio=increase:flags=lanczos,crop=3840:2160,setsar=1'

def offsets():
    """Where each shot starts inside its source: second uses ('^') continue the clip, others skip 0.3 s."""
    res, used = [], {}
    for s in SH:
        if s['kind'] == 'TH': res.append(s['ms']); continue
        if s['kind'] == 'GFX': res.append(0.0); continue
        b = base(s['id']); o = used.get(b, 0.3) if s['id'].endswith('^') else 0.3
        res.append(o); used[b] = o + s['dur']
    return res

def job(k, s, ms):
    out = f'seg/s{k:03d}.mp4'
    if os.path.exists(out): return
    src = src_for(s); du = s['dur']; N = round(du * FPS); still = src.endswith('.png')
    if not os.path.exists(src): print('waiting for', src); return
    mv = zp(TIGHT.get(s['id'], s.get('move', 'none')), N, still)
    if still:
        vf = f'{BIG},{mv}' if mv else COVER
        cmd = [FF, '-v', 'error', '-y', '-loop', '1', '-framerate', str(FPS), '-i', src, '-frames:v', str(N), '-vf', vf]
    else:
        D = dur(src)
        if ms > D - 1.0 and s['kind'] != 'TH': ms = 0.3
        pre = ''
        if s['kind'] not in ('TH', 'GFX'):
            avail = D - ms
            if avail < du - 0.05: pre = f'setpts=PTS/{max(0.55, avail / du):.4f},'   # gently slow a short B-roll clip, never a talking head
        base_vf = f'{pre}fps={FPS},' + (f'{BIG},{mv}' if mv else COVER)
        cmd = [FF, '-v', 'error', '-y', '-ss', f'{ms:.3f}', '-i', src, '-an', '-vf', base_vf + ',tpad=stop_mode=clone:stop_duration=10', '-frames:v', str(N)]
    cmd += ['-c:v', 'libx264', '-preset', 'fast', '-crf', '17', '-pix_fmt', 'yuv420p', '-r', str(FPS), out + '.tmp.mp4']
    subprocess.run(cmd, check=True); os.replace(out + '.tmp.mp4', out)

def endcard():
    """Calm end card: blurred pantry still with the channel name, no call to action."""
    out = f'seg/s{len(SH) + 1:03d}.mp4'
    if os.path.exists(out): return
    vf = (f"{COVER},boxblur=18:2,eq=brightness=0.04,"
          "drawtext=fontfile=fonts/PlayfairDisplay-Bold.ttf:text='Stocked & Ready':fontsize=110:fontcolor=white:x=(w-tw)/2:y=(h-th)/2-30:shadowcolor=black@0.4:shadowx=2:shadowy=2,"
          "drawtext=fontfile=fonts/Inter-Bold.otf:text='WITH CATHERINE REESE':fontsize=36:fontcolor=0xE6B743:x=(w-tw)/2:y=(h/2)+70,"
          f"fade=in:st=0:d=0.4")
    subprocess.run([FF, '-v', 'error', '-y', '-loop', '1', '-framerate', str(FPS), '-i', 'stills/M20.png', '-frames:v', str(round(CARD * FPS)), '-vf', vf,
                    '-c:v', 'libx264', '-preset', 'fast', '-crf', '17', '-pix_fmt', 'yuv420p', out], check=True)

if __name__ == '__main__':
    if 'precut' in sys.argv:
        offs = offsets()
        jobs = [(k, s, offs[k]) for k, s in enumerate(SH)]
        jobs.append((len(SH), dict(kind='BR', id='M42', dur=WAVE, move='none'), WAVE_START))   # wave only after the VO has ended
        with ThreadPoolExecutor(4) as ex:
            for f in [ex.submit(job, *j) for j in jobs]: f.result()
        endcard(); print('precut done', len(jobs) + 1)
    if 'concat' in sys.argv:
        n = len(SH) + 2
        open('seg/list.txt', 'w').write(''.join(f"file 's{k:03d}.mp4'\n" for k in range(n)))
        subprocess.run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', 'seg/list.txt', '-c', 'copy', 'out/video_raw.mp4'], check=True)
        print('raw', dur('out/video_raw.mp4'), 'expected', round(TOTAL, 3))
    if 'mix' in sys.argv:
        sfx = []; gi = 0
        for s in SH:
            if s['kind'] == 'GFX':
                sfx.append((f'sfx{gi % 7 + 1}', max(0, s['t'] - 0.08), 0.16)); gi += 1
        ins = ['-i', 'vo.wav']; flt = [f'[0:a]aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur={TOTAL}[vo]']; labs = ['[vo]']
        for k, (n, t, v) in enumerate(sfx):
            ins += ['-i', f'audio/{n}.wav']; ms = int(t * 1000)
            flt.append(f'[{k + 1}:a]aresample=48000,aformat=channel_layouts=stereo,volume={v},adelay={ms}|{ms}[s{k}]'); labs.append(f'[s{k}]')
        flt.append(''.join(labs) + f'amix=inputs={len(labs)}:normalize=0:dropout_transition=0,atrim=0:{TOTAL},loudnorm=I=-14:TP=-1.5:LRA=11[out]')
        subprocess.run([FF, '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(flt), '-map', '[out]', '-ar', '48000', '-c:a', 'aac', '-b:a', '192k', 'out/mix.m4a'], check=True)
        print('mix ok', len(sfx), 'sfx')
    if 'final' in sys.argv:
        vf = ("colorbalance=rs=-0.02:bs=0.03:rh=0.035:gh=0.01:bh=-0.035,eq=contrast=1.04:saturation=0.97,vignette=angle=PI/5,noise=alls=3:allf=t,"
              "ass=subs.ass:fontsdir=fonts")
        subprocess.run([FF, '-v', 'error', '-y', '-i', 'out/video_raw.mp4', '-i', 'out/mix.m4a', '-vf', vf, '-map', '0:v', '-map', '1:a',
                        '-c:v', 'libx264', '-preset', 'faster', '-crf', '20', '-maxrate', '10M', '-bufsize', '20M', '-pix_fmt', 'yuv420p',
                        '-c:a', 'copy', '-movflags', '+faststart', '-shortest', 'out/Stocked-and-Ready_Video14.mp4'], check=True)
        print('FINAL DONE')
