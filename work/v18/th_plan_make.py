"""Write th_plan.json for V18 from sentence ranges and print the talking-head share."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
S = json.loads((HERE / 'sent.json').read_text(encoding='utf-8'))
R = [(0,2),(11,13),(16,20),(32,33),(40,40),(44,45),(55,56),(64,65),(73,75),(78,81),(87,88),(98,99),(107,108),(116,117),(119,120),(123,124),(133,134),(137,137),(161,162),(170,172),(176,177),(27,27),(49,49)]
plan, tot = [], 0.0
for k, (a, b) in enumerate(R):
    s = 0.0 if a == 0 else S[a]['s']; e = S[b]['e']
    nxt = S[b + 1]['s'] if b + 1 < len(S) else e + 1.5
    tot += nxt - s
    plan.append({'id': f'TH{k:02d}', 'sent': [a, b], 's': round(s, 3), 'e': round(e, 3)})
(HERE / 'th_plan.json').write_text(json.dumps(plan, indent=1))
print(len(plan), 'THs', round(tot, 1), 's =', round(100 * tot / (S[-1]['e'] + 1.5), 1), '%')
