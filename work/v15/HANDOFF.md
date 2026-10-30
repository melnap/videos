# Video 15 – Übergabe an die Schnitt-Session

**Titel:** 12 Baking Staples to Stock Up On Before the Holidays (And How to Store Them)
**Dojo-Item:** 3TC3pCWbvYdAbvFa7Yau · **Trello:** Karte „Vid15“ im Board Stocked & Ready
**Deadline:** spätestens Mitte November online (Backsaison/Thanksgiving 26.11.)

## Dateien
- `script.txt` – finaler Sprechtext (ca. 2.060 Wörter, ca. 13 Min), Sauce-Fassung, Zahlen als Wörter.
- Thumbnail lädt Melanie selbst hoch (nicht Teil des Schnitts).

## 1. Voiceover (macht diese Session selbst)
- ElevenLabs-Konnektor: `creative_create_flow` → `creative_generate_speech` im SELBEN Flow.
- Stimme: Mariana "Intimacy with Authority", voice_id `OB0Jj6v9DGLLgz8dD57i`, Modell `eleven_multilingual_v2`, **speed 1.08**. Erst einen kurzen Probesatz erzeugen.
- Max. 5.000 Zeichen pro Anfrage → an Absatzgrenzen in 3 Teile, mit ffmpeg zusammenfügen (ca. 0,6 s Pause an den Nähten), -16 LUFS (Endmaster -14 LUFS).
- Keine Generierung wiederholen (kostet jedes Mal Credits).
- Transkription mit Scribe im SELBEN Flow (kostenlos).

## 2. Schnitt (Regeln siehe Skill stocked-and-ready-youtube)
- Kein Intro. Ab 0:00 Talking Head TH00 mit dem Hook („The baking staples in your cupboard right now could ruin your holiday baking. Not because you bought the wrong brand …“).
- Talking Heads 18–22 % der Laufzeit per HeyGen-Konnektor, Catherine hinter der Kücheninsel (SET03), frontal, Hände nicht im Bild. Zoom-Wechsel weit/nah im Schnitt.
- Keine Hintergrundmusik, ruhige B-Roll, Karaoke-Untertitel (Inter Bold, aktuelles Wort Gold).
- Keine Supermarkt-Szenen, keine Markenlogos (kein Arm & Hammer, Crisco, King Arthur usw.). Packungen ohne lesbare Schrift. Alles in Catherines Küche/Speisekammer, Gefriertruhe im Hauswirtschaftsraum (SET06).
- Winken erst nach dem letzten gesprochenen Satz.

## Erstes Bild
Nahaufnahme: ein Backblech mit flach zerlaufenen, blassen Plätzchen auf der Kücheninsel – passt zu „could ruin your holiday baking“. Danach TH00.

## Gute Stellen für Talking Heads
- Hook (TH00, s. o.)
- Versprechen + Teaser: „So today I'm going through the twelve baking staples …“
- „I'm Catherine, and I learned most of this the hard way, with a tray of flat cookies on a Christmas Eve.“
- Kommentarfrage: „What's the one holiday recipe your family asks for every single year?“
- Nr. 1: „This is the one that's probably in your cupboard right now, and it may already be dead.“
- Routine: „Here's my routine before the holidays …“
- Schluss: „It takes about twenty minutes …“

## Grafiken (alle Zahlen belegt, bitte genau so)
- Preislage: Sugar & sweets ~+6–7 % · Wheat (farm) ~+17 % (USDA ERS 2026) · Chocolate ~+11–12 % (analyst, Oct 2026) while wholesale cocoa fell
- Haltbarkeiten (NDSU FN579), jeweils „unopened / opened“:
  - 12 Vanilla 2 yr / 12 mo
  - 11 Ground spices 2–3 yr · whole 3–4 yr · blends 6 mo
  - 10 Cornstarch 18–24 mo / 18 mo
  - 9 Sweetened condensed milk 12 mo / 4–5 days (fridge)
  - 8 Molasses 1–2 yr / 6 mo
  - 7 Brown sugar 18–24 mo (airtight)
  - 6 Shortening 1–2 yr / ~1 yr (Iowa State)
  - 5 Baking chocolate 1–2 yr / 1 yr · cocoa: indefinitely
  - 4 Whole wheat flour 3–6 mo / 6–8 mo fridge (white flour 6–12 mo, freezer indefinite)
  - 3 Dry yeast 2 yr / 4 mo fridge · 6 mo freezer
  - 2 Baking soda 2–3 yr / 3–6 mo
  - 1 Baking powder 6–18 mo / 3–6 mo
- Test-Karten (Iowa State Extension):
  - Baking soda: 1 tsp + 3 Tbsp vinegar → bubbles = good
  - Baking powder: 1 tsp + 1/3 cup hot water → bubbles = good
  - Yeast: 1 tsp sugar + 1/2 cup warm water + 1 envelope, 10 min → foams to 1/2 cup mark
- Schädlinge (K-State MF2270): 0 °F for 3 days · large packages 7 days · glass jars with screw-on lids best
- Listen-Labels „12 … 1“
- Schlusskarte (Routine): „Smell · Test · Freeze new flour · Seal brown sugar · Date every lid“

## B-Roll-Ideen je Punkt (ohne Markenaufdruck)
Vanilleflasche zuschrauben, dunkler Schrank · an Zimtglas riechen, Gewürzschublade · Stärke in Bratensoße einrühren · Kondensmilchrest in kleines Glas schaben · Melasseglas im warmen Wasserbad, Rand abwischen · steinharter brauner Zucker → Brotscheibe drauf, Dose zu → am Morgen lockerer Zucker · Backfett-Dose, Teig für Pie-Kruste · Schokolade mit grauem Bloom vs. geschmolzene Schokolade, Kakaodose · Vollkornmehl-Beutel in die Gefriertruhe, später ins Schraubglas · Hefeprobe im Messbecher schäumt bis zur ½-Cup-Marke · Natron in Essig sprudelt · Backpulver in heißem Wasser sprudelt vs. flaches Glas · flache vs. aufgegangene Plätzchen · Marker beschriftet Deckel mit Datum.
