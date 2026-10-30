# Stand Video 11 / 12 (für die nächste Session)

## Festgelegte Einstellungen (gelten für V10–V12)
- Voiceover: ElevenLabs **Eleven v4** (wie Melanie in Studio), Stimme Mariana "Intimacy with Authority" `OB0Jj6v9DGLLgz8dD57i`, je Teil 1 Take (generations_count=1).
- Tempo danach **+8 %** per ffmpeg `atempo=1.08` je Teil, dann 0,6 s Pausen an den Nähten, loudnorm -16 LUFS → `vo.mp3`. Rohdateien bleiben als `vo/raw_pN.mp3`.
- Scribe läuft auf den Rohteilen (im selben Flow, kostenlos); Wort-Zeiten danach durch 1,08 teilen → `asr/wN.json`, dann `python3 align.py`.
- Talking Heads: Arme locker auf dem Counter (von Melanie freigegeben; leichte Bewegung ok, wilde Gesten im Schnitt mit B-Roll/Nah-Ausschnitt verdecken, nichts neu rendern). Grundbild V10: Higgsfield 82f4078b-9cd0-4cd3-963c-256f23c02f4f (HeyGen-Asset e10b85bd65d549b5bd96d052851e9a84). TH00 = Hook-Satz, Winken erst nach dem VO.
- Credits sparsam: bei Zweifeln Melanie die Szene zeigen statt neu rendern.
- Vorlage für alles: `work/v10` (Pipeline-Skripte, beats.py, th_plan.json, gfx.py, subs_extra.py, shots.py mit TH-Zoom thclose/thpush, build.py, remap_segs.py).

## Video 11 (Butter) – Stand
- ElevenLabs-Flow "Stocked & Ready V11 Voiceover", flow_id `teV2e4m0nfK9pdZ8MkpF`.
  - Teil 1: node `COnUf4XJMYM4u9ok7wSj`, generation `mLnUGVsPDw2hEqlt9z7V` → `vo/raw_p1.mp3` ✔
  - Teil 2: node `olB5iQMTd5yJz2iuaGX2`, generation `w4cU4bhsNSihOLabF0mn` → `vo/raw_p2.mp3` ✔
  - Teil 3: node `XranNj7UVefxALm70YiY`, generation `hOlcToiZPHmTGKfMFYNY` – **fertig generiert, noch nicht heruntergeladen** (creative_get_flow_run_status mit session `1AuerXrD5crfgH0aTwpy` liefert eine neue URL; NICHT neu generieren).
- Danach: Scribe auf die drei Nodes (creative_transcribe_audio, connect_from = Node-ID), Tempo/Alignment wie oben.
- Länge mit +8 %: ca. 10:55 (Melanie: 8 % bleibt, keine künstlichen Pausen).
- Fertig: assets_m.py, Higgsfield-B-Roll (27 Stills, 14 Clips; B04 und B08 nur als Standbild), Stock (134 Dateien, stock/picks_notes.md), gfx.py (Anker noch eintragen, sobald sent.json da ist).
- Offen: TH-Plan + HeyGen (Stellen laut HANDOFF.md), beats.py, subs_extra (Labels/Callouts), Render, QC, Auslieferung `videos/Stocked-and-Ready_Video11.mp4`.

## Video 12 (Stromausfall) – noch nicht begonnen
- Komplett wie Video 10/11. Laut Auftrag: KEINE Szene mit Grill, Campingkocher oder Generator im Haus.
