# Video 8 – Übergabe an die Schnitt-Session

**Titel:** Always Keep These 12 Canned Foods for When Money Gets Tight
**Veröffentlichung:** Ende Oktober 2026 (nach Video 7)
**Dojo-Item:** jxdIP6U33vWveY104cqW · **Trello:** https://trello.com/c/sr4bm7Ub

## Dateien
- `script.txt` – finaler Sprechtext (2.237 Wörter, ca. 13–14 Min.), Sauce-Ergänzungen sind drin. Zahlen sind bereits als Wörter ausgeschrieben.
- `thumb_v8_a3.png` – Thumbnail (lädt Melanie selbst hoch, nicht Teil des Schnitts).

## 1. Voiceover (macht diese Session selbst)
- ElevenLabs-Konnektor: `creative_create_flow` → `creative_generate_speech` im SELBEN Flow.
- Stimme: Mariana "Intimacy with Authority", voice_id `OB0Jj6v9DGLLgz8dD57i`, Modell `eleven_multilingual_v2`.
- Max. 5.000 Zeichen pro Anfrage → Text an Absatzgrenzen in 3 Teile schneiden, danach mit ffmpeg zusammenfügen (kurze Pause ca. 0,6 s an den Nahtstellen), auf -16 LUFS normalisieren (Endmaster -14 LUFS).
- Generierung nicht wiederholen, um es „nochmal zu versuchen“: jeder Aufruf kostet Credits.
- Transkription (Wort-Zeitstempel für Karaoke-Untertitel und satzgenauen Schnitt) mit Scribe im SELBEN Flow, dann kostenlos. KEIN Upload einer fertigen Datei zum Transkribieren.

## 2. Schnitt (Regeln siehe Skill stocked-and-ready-youtube)
- Kein Intro: ab 0:00 direkt der erste Satz. Erstes Bild: starkes Motiv zu „the cans on your shelf decide dinner“ (z. B. Nahaufnahme Regal mit Dosen, Hand greift eine Dose).
- Talking Heads 18–22 % der Laufzeit per HeyGen-Konnektor, Catherine hinter der Kücheninsel (SET03), frontal, Hände nicht im Bild, Frisur einmal festlegen. Auf der Anrichte je Szene die passende Dose.
- Keine Hintergrundmusik, keine Supermarkt-Szenen, ruhige B-Roll, Karaoke-Untertitel (Inter Bold, aktuelles Wort Gold).

## Gute Stellen für Talking Heads
- „That isn't a lack of discipline. Nobody ever showed you how to set up the shelf …“
- Versprechen: „So here are twelve canned foods worth keeping …“ (inkl. der drei Teaser)
- Die drei Regeln (store brand / on sale / only what your family eats)
- Nr. 10 Sardinen: „Not every family will love them, so buy one can and try it …“
- Nr. 12: „This is the one I promised you …“
- „These were never twelve separate cans.“
- Schluss: „The idea behind all of this is simple …“

## Grafiken (alle Zahlen belegt, bitte genau so)
- Essen außer Haus +3,4 % vs. Lebensmittel zuhause +2,2 % (BLS, August 2026)
- Obst & Gemüse aus der Dose +4,0 % (BLS, August 2026); frisches Gemüse 2026 Prognose +5,7 % (USDA ERS, Sept. 2026)
- Haltbarkeit: Low-Acid-Dosen 2–5 Jahre, High-Acid (Obst, Tomatenmark) 12–18 Monate; geöffnet 3–4 bzw. 5–7 Tage im Kühlschrank (USDA)
- Süßkartoffel: 1 Cup ≈ fast ganzer Tagesbedarf Vitamin A, ca. 6 g Ballaststoffe
- Sardinen (3,75 oz): ca. 350 mg Kalzium vs. Glas Milch ca. 300 mg; über 20 g Protein
- Bohnen: Abtropfen −36 % Natrium, Abtropfen + Spülen −41 % (University of Tennessee)
- Listen-Labels „1/12 … 12/12“
- Abschnitt „A week from this shelf“: kleine Rezept-Kärtchen (Chili, Casserole, Hash, Sheet-Pan-Bowl, Sardinen-Toast, Chili auf Ofenkartoffel)
- Verbeulte Dosen: Checkliste (bulging, leaking, spurting, deep dent on seam, rust)

## B-Roll-Ideen je Punkt
1 Mais in Topf/Pfanne · 2 Mischgemüse in Bratreis rühren · 3 Pfirsiche in Schale · 4 Dosenkartoffeln in der Pfanne anbraten · 5 Tomatenmark in Esslöffel-Portionen auf Teller, Gefrierbeutel · 6 Auflauf mit Cremesuppe aus dem Ofen · 7 Süßkartoffel-Püree mit Zimt · 8 Kichererbsen abspülen, im Ofen rösten · 9 Chili über Ofenkartoffel · 10 Sardinen auf Toast · 11 Hähnchen aus der Dose, Brühe in Tasse gießen · 12 Bohnen im Sieb unter dem Wasserhahn, großer Topf Chili
Lagerung: Dosenregal in der Speisekammer, neue Dosen nach hinten, alte nach vorn; verbeulte Dose in Nahaufnahme.
Alle Etiketten ohne Text und ohne Markenlogos.
