"""Make karaoke-style ASS (burn-in) + SRT (YouTube) from word timings.
Usage: python3 subs.py words.json offset_seconds out_basename"""
import json, sys, re

words = json.load(open(sys.argv[1])); OFF = float(sys.argv[2]); OUT = sys.argv[3]
GOLD = '&H006AB2D9&'; WHITE = '&H00FFFFFF&'

def ts_ass(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'
def ts_srt(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = int(t % 60); ms = int(round((t - int(t)) * 1000))
    if ms == 1000: s += 1; ms = 0
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'

W = [dict(w=x['w'].strip(), s=x['s'] + OFF, e=x['e'] + OFF) for x in words if x['w'].strip()]
# group: max 4 words / 22 chars, break after punctuation or pause > 0.45s
groups, cur = [], []
for i, w in enumerate(W):
    cur.append(w)
    nxt = W[i + 1] if i + 1 < len(W) else None
    txt = ' '.join(x['w'] for x in cur)
    brk = (nxt is None or len(cur) >= 4 or len(txt) >= 22 or re.search(r'[.,;:!?]$', w['w'])
           or (nxt and nxt['s'] - w['e'] > 0.45))
    if brk: groups.append(cur); cur = []

ass = ['[Script Info]', 'ScriptType: v4.00+', 'PlayResX: 1920', 'PlayResY: 1080', 'WrapStyle: 2', '',
       '[V4+ Styles]',
       'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',
       'Style: Cap,Inter,66,&H00FFFFFF,&H00FFFFFF,&H00141008,&H96000000,1,0,0,0,100,100,0,0,1,4.5,2,2,120,120,96,1', '',
       '[Events]', 'Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
srt = []
for gi, g in enumerate(groups):
    g_end = g[-1]['e'] + 0.12
    nxt_start = groups[gi + 1][0]['s'] if gi + 1 < len(groups) else g_end + 1
    g_end = min(g_end + 0.25, nxt_start)  # hold briefly, never overlap next group
    for k, w in enumerate(g):
        st = w['s'] if k else g[0]['s']
        en = g[k + 1]['s'] if k + 1 < len(g) else g_end
        if en <= st: continue
        parts = [(f'{{\\c{GOLD}}}{x["w"]}{{\\c{WHITE}}}' if j == k else x['w']) for j, x in enumerate(g)]
        ass.append(f'Dialogue: 0,{ts_ass(st)},{ts_ass(en)},Cap,,0,0,0,,{" ".join(parts)}')
    srt.append(f'{gi + 1}\n{ts_srt(g[0]["s"])} --> {ts_srt(g_end)}\n{" ".join(x["w"] for x in g)}\n')
open(OUT + '.ass', 'w').write('\n'.join(ass) + '\n')
open(OUT + '.srt', 'w').write('\n'.join(srt))
print(len(groups), 'groups')
