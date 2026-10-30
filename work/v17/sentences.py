"""Group words.json into sentences -> sent.json [{i, s, e, text}] and print a numbered list."""
import json, pathlib, re

HERE = pathlib.Path(__file__).parent
W = json.loads((HERE / 'words.json').read_text(encoding='utf-8'))
sent, cur = [], []
for w in W:
    cur.append(w)
    if re.search(r'[.?!]["”]?$', w['w']):
        sent.append(cur); cur = []
if cur:
    sent.append(cur)
out = [{'i': i, 's': s[0]['s'], 'e': s[-1]['e'], 'text': ' '.join(x['w'] for x in s)} for i, s in enumerate(sent)]
(HERE / 'sent.json').write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding='utf-8')
for o in out:
    print(f"{o['i']:3d} {o['s']:7.2f}-{o['e']:7.2f} {o['text']}")
