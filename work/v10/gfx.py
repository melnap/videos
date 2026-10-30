# Graphics for Stocked & Ready V10 (freezer before winter, 20 tricks). All numbers from HANDOFF.md (USDA FSIS, NDSU). Anchors: (sentence, word); None = shot start.
BG='SR_kit9.png'
GFX = {
 'part1': dict(type='quote', kicker='Part 1 of 4', title='Set it up', bg=BG, rows=[]),
 'part2': dict(type='quote', kicker='Part 2 of 4', title='Stock it for winter', bg=BG, rows=[]),
 'part3': dict(type='quote', kicker='Part 3 of 4', title='Never freeze', bg=BG, rows=[]),
 'part4': dict(type='quote', kicker='Part 4 of 4', title='Thaw & protect', bg=BG, rows=[]),
 'safe':  dict(type='quote', kicker='USDA Food Safety and Inspection Service', title='0 °F = safe indefinitely', bg=BG,
               rows=[('freezer chart times are for quality only',(25,'quality'))]),
 'full':  dict(type='card', kicker='Without power · USDA', title='A full freezer holds longer', bg=BG,
               rows=[('Full freezer','≈ 48 hours',(34,'fortyeight')),('Half full','≈ 24 hours',(34,'twentyfour'))]),
 'cran':  dict(type='card', kicker='Cranberries · NDSU Extension', title='A year in the freezer', bg=BG,
               rows=[('Refrigerator','about 2 months',(73,'refrigerator')),('Freezer','about 12 months',(74,'freezer'))]),
 'turkey':dict(type='card', kicker='Turkey · best quality', title='Freeze it in broth', bg=BG,
               rows=[('Cooked pieces, plain','about 4 months',(88,'four')),('Covered in broth or gravy','about 6 months',(89,'six')),('Leftovers in the fridge','3–4 days',(90,'three'))]),
 'eat':   dict(type='card', kicker='USDA cold storage chart', title='Eat first, keep back', bg=BG, compact_rows=True,
               rows=[('Steaks','6–12 months',(116,'steaks')),('Roasts','4–12 months',(116,'roasts')),('Ground beef','3–4 months',(117,'ground')),('Chicken pieces','about 9 months',(118,'chicken'))]),
 'short': dict(type='card', kicker='The short-timers', title='Use these within weeks', bg=BG,
               rows=[('Bacon','about 1 month',(124,'bacon')),('Hot dogs, lunch meat, sausage','1–2 months',(125,'hot'))]),
 'thaw':  dict(type='card', kicker='Thawing a turkey · USDA', title='24 h for every 4–5 lb', bg=BG,
               rows=[('20-lb turkey in the fridge','4 days',(157,'twentypound')),('In cold water','change it every 30 min',(158,'change'))]),
 'coin':  dict(type='check', kicker='The coin in a cup', title='What the coin tells you', bg=BG,
               rows=[('Coin still on top: stayed frozen',True,(174,'top')),('Coin sank: it thawed and refroze',False,(175,'sank'))]),
}
