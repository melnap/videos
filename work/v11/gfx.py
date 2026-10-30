# Graphics for Stocked & Ready V11 (butter in November). All numbers from HANDOFF.md. Anchors (sentence, word) are filled in after alignment.
BG='SR_kit9.png'
GFX = {
 'third': dict(type='card', kicker='Butter, per pound', title='Stores pay about 1/3', bg=BG,
               rows=[('Wholesale · USDA Dairy Market News, Sept 29, 2026','≈ $1.32',(28,'dollar')),('Store · BLS, August 2026','≈ $4.02',(29,None))]),
 'down':  dict(type='quote', kicker='BLS · August 2026', title='−17 % vs. last year', bg=BG, rows=[('a pound averaged ≈ $4.02 in August',(33,'four'))]),
 'fcst':  dict(type='quote', kicker='USDA forecast', title='2026 wholesale ≈ $1.65 / lb', bg=BG, rows=[]),
 'keep':  dict(type='card', kicker='How long butter keeps · USDA FoodKeeper, NDSU', title='Freezer: 6–9 months', bg=BG,
               rows=[('Refrigerator','1–2 months',(38,'refrigerator')),('Freezer (best quality)','6–9 months',(39,'freezer'))]),
 'math':  dict(type='card', kicker='How much to buy', title='1 stick a week', bg=BG,
               rows=[('× 24 weeks','= 24 sticks',(51,'twentyfour')),('= 6 lb','+ holiday baking',(52,'six'))]),
 'cal':   dict(type='check', kicker='Butter sale season', title='Watch the weekly ads', bg=BG, compact_rows=True,
               rows=[('Thanksgiving · Nov 26',True,(25,None)),('Black Friday week',True,(26,'black')),('Christmas baking',True,(26,'christmas'))]),
 'stick': dict(type='quote', kicker='At about $4 a pound', title='≈ $1 per stick', bg=BG, rows=[]),
 'mist':  dict(type='check', kicker='Mistakes that ruin frozen butter', title='Skip these four', bg=BG, compact_rows=True,
               rows=[('Thin store wrapper only',False,(145,'mistake')),('Thaw and refreeze',False,(145,'buying')),('No date on the bag',False,(145,'family')),('Buying more than 6 months’ worth',False,(146,'sale'))]),
}
