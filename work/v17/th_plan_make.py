"""Write th_plan.json for V15 from sentence ranges and print the talking-head share."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
S = json.loads((HERE / 'sent.json').read_text(encoding='utf-8'))
R = [(0,2),(9,11),(12,12),(15,19),(22,23),(45,45),(57,58),(67,67),(87,90),(106,106),(112,112),(118,120),(123,124),(134,134),(137,137),(146,149),(163,164),(167,169),(172,173)]
plan, tot = [], 0.0
for k, (a, b) in enumerate(R):
    s = 0.0 if a == 0 else S[a]['s']; e = S[b]['e']
    nxt = S[b + 1]['s'] if b + 1 < len(S) else e + 1.5
    tot += nxt - s
    plan.append({'id': f'TH{k:02d}', 'sent': [a, b], 's': round(s, 3), 'e': round(e, 3)})
(HERE / 'th_plan.json').write_text(json.dumps(plan, indent=1))
print(len(plan), 'THs', round(tot, 1), 's =', round(100 * tot / (S[-1]['e'] + 1.5), 1), '%')
