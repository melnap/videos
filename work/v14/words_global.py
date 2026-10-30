"""Map Scribe word timestamps of the three raw VO parts onto the final vo.wav timeline.

Final timeline = (part1 + 0.6 s + part2 + 0.6 s + part3) sped up by 1.08.
Writes words.json: [{"w": text, "s": start, "e": end, "p": part}] and prints a sanity check.
"""
import json, subprocess, pathlib

HERE = pathlib.Path(__file__).parent
FFPROBE = HERE / '..' / '..' / '..' / 'tools' / 'ffmpeg' / 'bin' / 'ffprobe.exe'
GAP, TEMPO = 0.6, 1.08


def dur(p):
    out = subprocess.run([str(FFPROBE), '-v', 'error', '-show_entries', 'format=duration',
                          '-of', 'default=nw=1:nk=1', str(p)], capture_output=True, text=True)
    return float(out.stdout.strip())


def load_words(p):
    d = json.loads(p.read_text(encoding='utf-8'))
    if isinstance(d, dict):
        d = d.get('words', d)
    return [w for w in d if w.get('type', 'word') == 'word']


words, offset = [], 0.0
for i in (1, 2, 3):
    for w in load_words(HERE / f'words_part{i}.json'):
        words.append({'w': w['text'], 's': round((offset + w['start']) / TEMPO, 3),
                      'e': round((offset + w['end']) / TEMPO, 3), 'p': i})
    offset += dur(HERE / f'vo_part{i}.mp3') + GAP

(HERE / 'words.json').write_text(json.dumps(words, ensure_ascii=False, indent=0), encoding='utf-8')
total = (offset - GAP) / TEMPO
print(f'words={len(words)} last_end={words[-1]["e"]:.2f}s timeline={total:.2f}s vo.wav={dur(HERE / "vo.wav"):.2f}s')
print('first:', ' '.join(w['w'] for w in words[:12]))
print('last :', ' '.join(w['w'] for w in words[-10:]))
