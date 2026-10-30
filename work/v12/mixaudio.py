"""VO + SFX -> out/mix.m4a (-14 LUFS). No background music on the avatar channels."""
import json, subprocess
SH = json.load(open('shots.json')); TOTAL = 671.2 + 5.0
sfx = []
for s in SH:
    if s['kind'] == 'CARD': sfx.append(('whoosh', max(0, s['t'] - 0.25), 0.30))
    if s['kind'] == 'GFX': sfx.append(('pop', s['t'] + 0.05, 0.22))
sfx.append(('whoosh', 671.2 + 3.0 - 0.25, 0.30))
ins = ['-i','vo.mp3']
flt = ['[0:a]aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur=%s[vo]' % TOTAL]
labs = ['[vo]']
for k, (n, t, v) in enumerate(sfx):
    ins += ['-i', f'audio/{n}.mp3']; ms = int(t * 1000)
    flt.append(f'[{k+1}:a]aresample=48000,aformat=channel_layouts=stereo,volume={v},adelay={ms}|{ms}[s{k}]'); labs.append(f'[s{k}]')
flt.append(''.join(labs) + f'amix=inputs={len(labs)}:normalize=0:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11,atrim=0:{TOTAL}[out]')
subprocess.run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(flt),'-map','[out]','-ar','48000','-c:a','aac','-b:a','192k','out/mix.m4a'], check=True)
print('mix ok', len(sfx), 'sfx')
