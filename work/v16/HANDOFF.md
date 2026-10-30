# Video 16 – Übergabe an die Schnitt-Session

**Titel:** 15 Foods FEMA Says Every Family Should Store for Winter (Food Storage)
**Dojo-Item:** tpMoksxO1EJmrao5Rrmy · **Trello:** Karte „Vid16“ im Board Stocked & Ready

## Dateien
- `script.txt` – finaler Sprechtext (ca. 1.880 Wörter, ca. 12 Min), Sauce-Fassung, Zahlen als Wörter.
- Thumbnail lädt Melanie selbst hoch (nicht Teil des Schnitts).

## 1. Voiceover (macht diese Session selbst)
- ElevenLabs-Konnektor: `creative_create_flow` → `creative_generate_speech` im SELBEN Flow.
- Stimme: Mariana "Intimacy with Authority", voice_id `OB0Jj6v9DGLLgz8dD57i`, Modell `eleven_multilingual_v2`, **speed 1.08**.
- Max. 5.000 Zeichen pro Anfrage → an Absatzgrenzen in 3 Teile, mit ffmpeg zusammenfügen (ca. 0,6 s Pause an den Nähten), -16 LUFS (Endmaster -14 LUFS).
- Keine Generierung wiederholen. Transkription mit Scribe im SELBEN Flow.
- Aussprache prüfen: „FEMA“ (FEE-muh), „Ready.gov“ (Ready dot gov), „USDA“ (U-S-D-A).

## 2. Schnitt (Regeln siehe Skill stocked-and-ready-youtube)
- Kein Intro. Ab 0:00 Talking Head TH00 mit dem Hook („Your pantry probably wouldn't pass FEMA's Ready.gov emergency food list … It looks full. That's the problem.“).
- Talking Heads 18–22 % der Laufzeit per HeyGen-Konnektor, Catherine hinter der Kücheninsel (SET03), frontal, Hände nicht im Bild. Zoom-Wechsel weit/nah.
- Keine Hintergrundmusik, ruhige B-Roll, Karaoke-Untertitel (Inter Bold, aktuelles Wort Gold).
- Keine Supermarkt-Szenen, keine Markenlogos, kein FEMA-/Ready.gov-Logo, keine Kirchen-Symbole. Stromausfall-Stimmung: Abendlicht, Kerze/Laterne, Fenster mit Schnee (Pixabay für Außenaufnahmen Schnee/Eis).
- Winken erst nach dem letzten gesprochenen Satz.

## Erstes Bild
Volle Speisekammer (SET04) im Halbdunkel, Licht aus, nur eine Laterne – passt zu „It looks full. That's the problem.“ Danach TH00.

## Gute Stellen für Talking Heads
- Hook (TH00)
- „That isn't your fault. Nobody teaches us to stock a pantry for the day things stop working.“
- Versprechen + Teaser: „So today I'm going through the fifteen foods …“
- „I'm Catherine. I didn't grow up with a stocked pantry …“
- Kommentarfrage: „If the power went out tonight for three days …“
- Nr. 1: „This is the one that needs no stove, no refrigerator and no can opener.“
- „So that's FEMA's list. Now, how much is enough?“
- Schluss: „If you take one thing from this video …“

## Grafiken (alle Zahlen belegt, bitte genau so)
- Quellen-Karte: Ready.gov (FEMA) · „Food and Water in an Emergency“ (FEMA, American Red Cross, USDA)
- Listen-Labels „15 … 1“
- Haltbarkeits-Karten (FEMA-Broschüre):
  - Use within 6 months: crackers, dried fruit, boxed powdered milk
  - Use within 1 year: canned soups, canned fruits & vegetables, canned juice, cereals, peanut butter, canned nuts
  - Indefinitely (proper containers): salt, white rice, dry pasta, instant coffee/tea/cocoa, bouillon, nitrogen-packed powdered milk
- „How much is enough?“: Ready.gov several days → FEMA guide 2 weeks → Church of Jesus Christ 3 months (+ wheat, white rice, beans: 30+ years)
- Wasser: 1 gallon / person / day · „Never ration water.“
- Reihenfolge bei Stromausfall: Fridge → Freezer → Pantry · Fridge ~4 h · Full freezer ~48 h · Half full ~24 h (USDA)
- Schlusskarte: „Could my family eat this without power?“

## B-Roll-Ideen je Punkt (ohne Markenaufdruck)
Dampfender Becher Kakao bei Kerzenlicht · Salzdose · Brühwürfel in heißem Wasser · Müsli in Dose mit Deckel · Cracker in Beutel in Blechdose · Trockenobst ins Schraubglas · Nüsse in Glas · Saftdosen · Milchkartons/Milchpulver · Dosensuppe auf Campingkocher · Dosen-Regal: neue nach hinten, alte nach vorn, Datum mit Marker · Reis/Nudeln in luftdichten Behältern · Fleischdosen + manueller Dosenöffner · Vitamindose · Glas Erdnussbutter, Cracker · Wasserkanister · Kühlschrank geschlossen halten, Gefriertruhe (SET06) · Fenster mit Schnee/Eis (Pixabay).
