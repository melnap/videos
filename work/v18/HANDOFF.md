# Video 18 – Übergabe an die Schnitt-Session

**Titel:** 10 Foods Your Freezer Ruins (And What to Do Instead)
**Dojo-Item:** H3VGiWIabPPpyx8DZUvM · **Trello:** Karte „Vid18“ im Board Stocked & Ready
**Reihenfolge:** erscheint NACH Video 17 (das Skript verweist auf Video 17).

## Dateien
- `script.txt` – finaler Sprechtext (ca. 1.890 Wörter, ca. 12–13 Min), Sauce-Fassung, Zahlen als Wörter.
- Thumbnail lädt Melanie selbst hoch (nicht Teil des Schnitts).

## 1. Voiceover (macht diese Session selbst)
- ElevenLabs-Konnektor: `creative_create_flow` → `creative_generate_speech` im SELBEN Flow.
- Stimme: Mariana "Intimacy with Authority", voice_id `OB0Jj6v9DGLLgz8dD57i`, Modell `eleven_multilingual_v2`, **speed 1.08**.
- Max. 5.000 Zeichen pro Anfrage → an Absatzgrenzen in 3 Teile, ffmpeg zusammenfügen (ca. 0,6 s Pause), -16 LUFS (Endmaster -14 LUFS).
- Keine Generierung wiederholen. Transkription mit Scribe im SELBEN Flow.

## 2. Schnitt (Regeln siehe Skill stocked-and-ready-youtube)
- Kein Intro. Ab 0:00 Talking Head TH00 mit dem Hook („Some of the food you put in your freezer to save money is coming back out ruined. The freezer didn't fail you. It was the wrong food.“).
- Talking Heads 18–22 % der Laufzeit per HeyGen-Konnektor, Catherine hinter der Kücheninsel (SET03), frontal, Hände nicht im Bild. Zoom-Wechsel weit/nah.
- Keine Hintergrundmusik, ruhige B-Roll, Karaoke-Untertitel (Inter Bold, aktuelles Wort Gold).
- Keine Supermarkt-Szenen, keine Markenlogos (keine Ziploc-, FoodSaver-, Mayo-Marken). Gefriertruhe = SET06.
- Winken erst nach dem letzten gesprochenen Satz.

## Erstes Bild
Nahaufnahme: aufgetaute Kartoffelsuppe im durchsichtigen Behälter, wässrig, Kartoffelstücke zerfallen („wet sand“). Danach TH00.

## Gute Stellen für Talking Heads
- Hook (TH00)
- „That's not your fault. Nobody hands you the other list …“
- Versprechen + Teaser: „So today I'm going through ten foods …“
- Kommentarfrage: „What's the worst thing you've ever pulled out of your freezer?“
- Nr. 1: „This is the one that isn't about taste. It's about safety.“
- Schluss: „If you take one thing from this video …“

## Grafiken (alle belegt, bitte genau so)
- Erklär-Grafik: Wasser → Eiskristalle → Zellwände platzen · „Emulsions such as mayonnaise or cream will separate“ (USDA)
- Listen-Labels „10 … 1“, jeweils mit Karte „DO THIS INSTEAD“
- Nr. 4: Unbaked pie crust 6–8 weeks (Univ. of Missouri)
- Extras: Bacon & sausage 1–2 months (USDA) · Only heavy cream ≥40 % fat freezes (NDSU)
- Wiedereinfrieren: Thawed in fridge → OK to refreeze · Thawed on counter → never (USDA)
- Sicher auftauen: Fridge · Cold water · Microwave (USDA)
- Schlusskarte: „Mostly water? Creamy? → Freeze the parts, not the dish.“

## B-Roll-Ideen je Punkt (ohne Markenaufdruck)
Welker dunkler Salat im Beutel vs. Beutel TK-Spinat · Hähnchensalat getrennt/ölig → Hähnchenwürfel und Nudeln separat einfrieren · Ei mit gesprungener Schale aus dem Gefrierfach → verquirlte Eier in Eiswürfelform · hartgekochtes Ei · körnige saure Sahne → Kaffeekuchen · Alfredo-Soße geronnen → Sahne erst beim Aufwärmen einrühren · Cremetorte mit matschigem Boden → gefrorener Pie-Boden · zerfallene Kartoffeln in Suppe → frisch gekochte Kartoffeln dazu · matschige Nudeln in Soße → Soße einzeln einfrieren · Dose mit aufgeplatzter Naht (nur Standbild) → Reste in Gefrierdose umfüllen · Dosen aus kalter Garage ins Haus tragen · Gefrierbrand-Stellen wegschneiden.
