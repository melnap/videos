# Video 9 – Übergabe an die Schnitt-Session

**Titel:** 12 Dollar Tree Foods Worth Stocking Before Winter (And 5 I Never Buy)
**Veröffentlichung:** Anfang November 2026 (nach Video 8)
**Dojo-Item:** 3pe41YGvzjCJcRN0d1Pm · **Trello:** https://trello.com/c/WKn1l2nr

## Dateien
- `script.txt` – finaler Sprechtext (2.064 Wörter, ca. 13 Min.), Sauce-Ergänzungen drin, Zahlen als Wörter.
- `thumbnail_canva_screenshot.png` – nur zur Orientierung (Thumbnail lädt Melanie selbst hoch, nicht Teil des Schnitts).

## 1. Voiceover (macht diese Session selbst)
- ElevenLabs-Konnektor: `creative_create_flow` → `creative_generate_speech` im SELBEN Flow.
- Stimme: Mariana "Intimacy with Authority", voice_id `OB0Jj6v9DGLLgz8dD57i`, Modell `eleven_multilingual_v2`.
- Max. 5.000 Zeichen pro Anfrage → an Absatzgrenzen in 3 Teile, mit ffmpeg zusammenfügen (ca. 0,6 s Pause an den Nähten), -16 LUFS (Endmaster -14 LUFS).
- Keine Generierung wiederholen (kostet jedes Mal Credits).
- Transkription mit Scribe im SELBEN Flow (kostenlos). Keine fertige Datei hochladen.

## 2. Schnitt (Regeln siehe Skill stocked-and-ready-youtube)
- Kein Intro, ab 0:00 der erste Satz. Erstes Bild: Hand nimmt ein kleines Lebensmittel aus einem Regal, Preisschild ohne Marke/Logo, oder Nahaufnahme Einkaufskorb mit Pantry-Lebensmitteln.
- KEINE echten Dollar-Tree-Ladenaufnahmen, kein Dollar-Tree-Logo, keine erkennbaren Marken auf Packungen (auch nicht Kraft, Jiffy, Pillsbury, Nature Valley, Top Ramen – die werden nur gesprochen). Keine Supermarkt-Szenen. Alles in Catherines Küche/Speisekammer.
- Talking Heads 18–22 % der Laufzeit per HeyGen-Konnektor, Catherine hinter der Kücheninsel (SET03), frontal, Hände nicht im Bild, Frisur einmal festlegen.
- Keine Hintergrundmusik, ruhige B-Roll, Karaoke-Untertitel (Inter Bold, aktuelles Wort Gold).

## Gute Stellen für Talking Heads
- „That isn't your fault. A small number on a shelf tag is designed to feel like a deal …“
- Versprechen: „So here are twelve Dollar Tree foods worth stocking before winter …“ (inkl. Teaser)
- Regel: „First, the rule that makes the whole trip work. Read the size, not just the price …“
- Nr. 7 Öl: „And here's why the small bottle is actually the smart size …“
- „Now the five things I never buy at Dollar Tree.“
- Schluss: „Before you go, one habit makes all of this work …“

## Grafiken (alle Zahlen belegt, bitte genau so)
- Preis-Chip „$1.25 → $1.50“ (viele Artikel, MoneyLion März 2026)
- „Unit price = price per ounce“-Callout; Beispiel „$1.50 / 8 oz vs. $1.50 / 24 oz“
- Je Lebensmittel: Preis-Callout + Haltbarkeit (NDSU):
  1 Pfeffer $1.25 · Gewürze gemahlen 2–3 Jahre
  2 Nudeln $1.50 · 2 Jahre ungeöffnet, 1 Jahr offen; Gefrier-Trick 0 °F, 4 Tage (UMN)
  3 Spaghetti-Kit $1.50, 8 oz, 4 Portionen
  4 Nudel-/Reisbeilagen $1.50 · Reis-Mischungen ca. 6 Monate
  5 Maisbrot-Mischung 75¢ · 9 Monate
  6 Kuchenmischung $1.50 · 12–18 Monate; Brownie 9 Monate
  7 Öl 16 oz $1.50 (vs. $3.49) · 6 Monate ungeöffnet, 3–5 offen
  8 Gurken ~$1.50 · offen 1–3 Monate im Kühlschrank
  9 Oliven $1.50 (vs. $2.49) · offen 1–3 Monate
  10 Ketchup ~24 oz $1.50 (vs. 14 oz $3.79) · 12 Monate; Senf 12 oz $1.50 · 1–2 Jahre
  11 Müsli $1.50 · 6–12 Monate ungeöffnet, 2–3 offen
  12 Ramen 5er-Pack $1.50 = 30¢ pro Packung (vs. 6er $2.99)
- Nie kaufen: Liste mit 5 roten X (Honig-Mischung, Dosengemüse ~$1 vs. ~60¢, Schmelzkäse-Ersatz, gefrorenes Steak, kleine Chips-Tüten ~2 oz $1.25)
- „Snowy weekend“-Karten: Sa Mittag Ramen + Ei · Sa Abend Spaghetti-Kit + Oliven · So Chili/Suppe + Maisbrot + Gurken · Kuchenmischung in Reserve
- Listen-Labels „1/12 … 12/12“ und „Never buy: 1/5 … 5/5“

## B-Roll-Ideen je Punkt (ohne Markenaufdruck)
1 Pfeffer in Gewürzregal, nicht über dem Herd · 2 Nudeln in Glas umfüllen, Packung ins Gefrierfach · 3 Spaghetti in Topf, Tomatensoße · 4 Reisbeilage in Topf rühren · 5 Maisbrot aus dem Ofen, neben Chili · 6 Kuchenmischung + Kürbis verrühren, Muffinblech · 7 kleine Ölflasche neben großem Kanister · 8 Gurkenglas, Gurkenwasser ins Dressing · 9 Olivenschale auf Nudeln/Ofenkartoffeln · 10 Ketchup/Senf im Kühlschranktür · 11 Müslibeutel zusammenfalten, Clip · 12 Ramen mit Ei, Gemüse, Löffel Erdnussbutter, Dampf
Nie kaufen: Honigglas-Etikett lesen (Nahaufnahme, ohne Marke), große Chipstüte vs. kleine.
Schluss: handgeschriebene Einkaufsliste, neue Packungen nach hinten ins Regal.
