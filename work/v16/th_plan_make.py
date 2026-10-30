"""Write th_plan.json for V15 from sentence ranges and print the talking-head share."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
S = json.loads((HERE / 'sent.json').read_text(encoding='utf-8'))
R = [(0,0),(8,10),(11,11),(14,15),(16,19),(36,36),(60,61),(74,77),(88,89),(105,106),(112,112),(122,123),(127,127),(133,134),(138,139),(145,147),(151,151),(160,162),(164,166)]
plan, tot = [], 0.0
for k, (a, b) in enumerate(R):
    s = 0.0 if a == 0 else S[a]['s']; e = S[b]['e']
    nxt = S[b + 1]['s'] if b + 1 < len(S) else e + 1.5
    tot += nxt - s
    plan.append({'id': f'TH{k:02d}', 'sent': [a, b], 's': round(s, 3), 'e': round(e, 3)})
(HERE / 'th_plan.json').write_text(json.dumps(plan, indent=1))
print(len(plan), 'THs', round(tot, 1), 's =', round(100 * tot / (S[-1]['e'] + 1.5), 1), '%')
