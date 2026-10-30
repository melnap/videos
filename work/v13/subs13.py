"""Karaoke captions (Inter Bold, current word gold) + channel lower third + list labels -> subs.ass.
Captions quote the voiceover word for word (from Scribe), spelled like the script."""
import json, re, pathlib
HERE = pathlib.Path(__file__).parent
W = json.loads((HERE / 'words.json').read_text(encoding='utf-8'))
S = json.loads((HERE / 'sent.json').read_text(encoding='utf-8'))
SH = json.loads((HERE / 'shots.json').read_text())
GOLD, WHITE = '&H0043B7E6&', '&H00FFFFFF&'   # gold #E6B743 (ASS is BGR)
GF = [(o['t'], o['t'] + o['dur']) for o in SH if o['kind'] == 'GFX']

def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'

# karaoke groups: max 4 words / 22 characters, break after punctuation or a pause > 0.45 s
groups, cur = [], []
for i, w in enumerate(W):
    cur.append(w); nxt = W[i + 1] if i + 1 < len(W) else None
    txt = ' '.join(x['w'] for x in cur)
    if nxt is None or len(cur) >= 4 or len(txt) >= 22 or re.search(r'[.,;:!?]$', w['w']) or nxt['s'] - w['e'] > 0.45:
        groups.append(cur); cur = []
D = []
for gi, g in enumerate(groups):
    nxt_start = groups[gi + 1][0]['s'] if gi + 1 < len(groups) else g[-1]['e'] + 1
    g_end = min(g[-1]['e'] + 0.37, nxt_start)
    for k, w in enumerate(g):
        st = w['s']; en = g[k + 1]['s'] if k + 1 < len(g) else g_end
        if en <= st: continue
        parts = [(f'{{\\c{GOLD}}}{x["w"]}{{\\c{WHITE}}}' if j == k else x['w']) for j, x in enumerate(g)]
        D.append(f'Dialogue: 0,{ts(st)},{ts(en)},Cap,,0,0,0,,{" ".join(parts)}')

def clip(a, b):
    """Overlay time ranges minus full-screen graphics (labels never sit on a graphic)."""
    out = [(a, b)]
    for g0, g1 in GF:
        nx = []
        for x, y in out:
            if y <= g0 or x >= g1: nx.append((x, y))
            else:
                if x < g0 - 0.3: nx.append((x, g0))
                if y > g1 + 0.3: nx.append((g1, y))
        out = nx
    return [(x, y) for x, y in out if y - x >= 1.2]

# channel lower third, first seconds only
a, b = ts(0.4), ts(4.3)
D += [f'Dialogue: 1,{a},{b},LTB,,0,0,0,,{{\\pos(0,0)\\fad(400,400)\\1c&H2E4A3A&\\1a&H50&\\p1}}m 90 790 l 700 790 l 700 905 l 90 905{{\\p0}}',
      f'Dialogue: 1,{a},{b},LTB,,0,0,0,,{{\\pos(0,0)\\fad(400,400)\\1c&H43B7E6&\\p1}}m 90 790 l 98 790 l 98 905 l 90 905{{\\p0}}',
      f'Dialogue: 2,{a},{b},LT1,,0,0,0,,{{\\pos(122,794)\\fad(400,400)}}Stocked & Ready',
      f'Dialogue: 2,{a},{b},LT2,,0,0,0,,{{\\pos(126,862)\\fad(400,400)}}WITH CATHERINE REESE']
# list labels top-left while each item runs
ITEMS = [(31, 39, '10/10', 'Sugar'), (39, 50, '9/10', 'Rice'), (50, 60, '8/10', 'Flour'), (60, 71, '7/10', 'Canned chicken'),
         (71, 84, '6/10', 'Frozen vegetables'), (84, 96, '5/10', 'Frozen berries'), (100, 113, '4/10', 'Nuts'), (113, 124, '3/10', 'Chicken breasts'),
         (124, 136, '2/10', 'Coffee'), (136, 150, '1/10', 'Butter'), (151, 157, 'NEVER 1/5', 'Giant olive oil'), (157, 162, 'NEVER 2/5', 'Big spice tubs'),
         (162, 166, 'NEVER 3/5', 'Giant fresh produce'), (166, 173, 'NEVER 4/5', 'Ground beef 5-pack'), (173, 180, 'NEVER 5/5', 'Five-dozen eggs')]
for s0, s1, n, t in ITEMS:
    for x, y in clip(S[s0]['s'], S[s1]['s'] - 0.2):
        D.append(f'Dialogue: 3,{ts(x)},{ts(y)},LblN,,0,0,0,,{{\\pos(70,60)\\fad(250,250)}}{n}')
        D.append(f'Dialogue: 3,{ts(x)},{ts(y)},LblT,,0,0,0,,{{\\pos(70,112)\\fad(250,250)}}{t}')

HEAD = ['[Script Info]', 'ScriptType: v4.00+', 'PlayResX: 1920', 'PlayResY: 1080', 'WrapStyle: 2', '', '[V4+ Styles]',
 'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',
 'Style: Cap,Inter,66,&H00FFFFFF,&H00FFFFFF,&H00141008,&H96000000,1,0,0,0,100,100,0,0,1,4.5,2,2,120,120,96,1',
 'Style: LblN,Inter,30,&H0043B7E6,&H0043B7E6,&H00000000,&HB4F2EFE6,1,0,0,0,100,100,2,0,3,14,0,7,0,0,0,1',
 'Style: LblT,Inter,40,&H00475F4F,&H00475F4F,&H00000000,&HB4F2EFE6,1,0,0,0,100,100,0,0,3,14,0,7,0,0,0,1',
 'Style: LT1,Playfair Display,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,0,3,7,0,0,0,1',
 'Style: LT2,Inter,30,&H0043B7E6,&H0043B7E6,&H00000000,&H00000000,1,0,0,0,100,100,3,0,1,0,2,7,0,0,0,1',
 'Style: LTB,Inter,20,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1',
 '', '[Events]', 'Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text']
(HERE / 'subs.ass').write_text('\n'.join(HEAD + D) + '\n', encoding='utf-8')
print(len(groups), 'caption groups,', len(D), 'events')
