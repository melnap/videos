# Video 17 – Übergabe an die Schnitt-Session

**Titel:** 15 Holiday Foods You Can Freeze Now (Most People Throw Them Away)
**Dojo-Item:** 9OzbZ9okGssybLodskex · **Trello:** Karte „Vid17“ im Board Stocked & Ready
**Reihenfolge:** erscheint VOR Video 18 (Video 18 verweist darauf). Spätestens Mitte November online (Thanksgiving 26.11.).

## Dateien
- `script.txt` – finaler Sprechtext (ca. 1.890 Wörter, ca. 12–13 Min), überarbeitete Sauce-Fassung, Zahlen als Wörter.
- Thumbnail lädt Melanie selbst hoch (nicht Teil des Schnitts).

## 1. Voiceover (macht diese Session selbst)
- ElevenLabs-Konnektor: `creative_create_flow` → `creative_generate_speech` im SELBEN Flow.
- Stimme: Mariana "Intimacy with Authority", voice_id `OB0Jj6v9DGLLgz8dD57i`, Modell `eleven_multilingual_v2`, **speed 1.08**.
- Max. 5.000 Zeichen pro Anfrage → an Absatzgrenzen in 3 Teile, ffmpeg zusammenfügen (ca. 0,6 s Pause), -16 LUFS (Endmaster -14 LUFS).
- Keine Generierung wiederholen. Transkription mit Scribe im SELBEN Flow.

## 2. Schnitt (Regeln siehe Skill stocked-and-ready-youtube)
- Kein Intro. Ab 0:00 Talking Head TH00 mit dem Hook („Your holiday leftovers don't belong in the trash. Most of them belong in your freezer. But that's not where most of them end up.“).
- Talking Heads 18–22 % der Laufzeit per HeyGen-Konnektor, Catherine hinter der Kücheninsel (SET03), frontal, Hände nicht im Bild. Zoom-Wechsel weit/nah.
- Keine Hintergrundmusik, ruhige B-Roll, Karaoke-Untertitel (Inter Bold, aktuelles Wort Gold).
- Keine Supermarkt-Szenen, keine Markenlogos (keine Ziploc-, Ocean-Spray-, Philadelphia-Marken). Gefriertruhe = SET06. Dezente Feiertagsstimmung (Tannenzweig, Kerze) erlaubt.
- Winken erst nach dem letzten gesprochenen Satz.

## Erstes Bild
Nahaufnahme Mülleimer/Abfallschale mit halbem Sahnekarton, Tasse mit Eiweiß, Beutel Cranberries, Schale Bratensoße – passt zu „Your holiday leftovers don't belong in the trash“. Danach TH00.

## Gute Stellen für Talking Heads
- Hook (TH00)
- „That isn't carelessness. Most of us learned that the freezer is for meat, ice cream and frozen peas.“
- Versprechen + Teaser: „So today I'm sharing fifteen holiday foods you can freeze now …“
- „I'm Catherine, and I learned these the slow way …“
- Kommentarfrage: „What's one food you've thrown away after the holidays …“
- Nr. 1: „This is the one almost nobody freezes, and it can rescue your Christmas baking.“
- Schluss: „Here's the habit that ties it together …“

## Grafiken (alle belegt, bitte genau so)
- Regel-Karte: „0 °F = safe indefinitely · times = quality only“ (FoodSafety.gov)
- Listen-Labels „15 … 1“
- Zeiten: Cranberries up to 12 months, straight from the bag (Penn State) · Heavy cream only ≥40 % fat (NDSU) · Hard cheese ≤½ lb pieces, ~6 months (NDSU/WSU) · Bread & rolls ~3 months · Cookie dough ~3 months · Unbaked pie crust 6–8 weeks · Unbaked fruit pies ~8 months · Pumpkin pie 4–5 weeks · Gravy 3–4 months · Stuffing ~1 month (Univ. of Missouri) · Cooked poultry 2–6 months (FoodSafety.gov) · Raw whites & yolks ~12 months (FoodSafety.gov)
- 2-Stunden-Regel (USDA): turkey off the bones, sliced, shallow containers within 2 hours
- Eier: 3 Tbsp = 1 egg · 2 Tbsp = 1 white · yolks + pinch of salt or sugar (NCHFP) · Never in the shell
- Schlusskarte: „Could this go in the freezer instead?“

## B-Roll-Ideen je Punkt (ohne Markenaufdruck)
Salbei/Thymian in Gefrierfolie · Beutel Cranberries direkt in die Gefriertruhe · Schlagsahne-Tupfen auf Blech (Schockfrosten) → auf Kakao · Frischkäse-Blöcke im Gefrierbeutel · Käse in ½-Pfund-Stücken · Milchkanister, oben etwas abgießen · Buttermilch in 1-Cup-Portionen · Brötchen in Folie im Ofen · Plätzchenteig als Rolle und Kugeln auf Blech · Pie-Böden flach gestapelt · ungebackener Obst-Pie, Lüftungsschlitze nach dem Einfrieren · Soße in kleinen Dosen · Füllung aufwärmen · Truthahn vom Knochen, flache Dosen · Eier verquirlen in Eiswürfelform · Beschriften mit Marker, Luft rausdrücken.
