# Graphics for Stocked & Ready V12 (pantry foods for a power outage). All numbers from HANDOFF.md. Anchors = (sentence, word).
BG='SR_kit9.png'
def life(name,a,b,ra,rb,la='Unopened',lb='Opened'):
    return dict(type='card', kicker=f'{name} · NDSU Extension', title=f'{la}: {a}', bg=BG, rows=[(la,a,ra),(lb,b,rb)])
GFX = {
 'cold':  dict(type='card', kicker='Power out · USDA', title='Keep the doors shut', bg=BG,
               rows=[('Refrigerator','≈ 4 hours',(22,'four')),('Full freezer','≈ 48 hours',(23,'fortyeight')),('Half-full freezer','≈ 24 hours',(23,'twentyfour'))]),
 'order': dict(type='steps', kicker='In an outage', title='Eat in this order', bg=BG,
               rows=[('Refrigerator',(25,'first')),('Freezer',(26,'then')),('Pantry',(27,'pantry'))]),
 'rule40':dict(type='quote', kicker='USDA', title='> 40 °F for 2 hours → throw it out', bg=BG, rows=[('When in doubt, throw it out',(33,None))]),
 'pb':    life('Peanut butter','6–24 months','2–3 months',(42,'unopened'),(43,'once')),
 'crack': life('Crackers','8 months','1 month',(50,'unopened'),(51,'once')),
 'cereal':life('Cereal','6–12 months','2–3 months',(79,'unopened'),(80,'once')),
 'dfruit':life('Dried fruit','6 months','1 month',(87,'unopened'),(88,'once')),
 'nuts':  dict(type='card', kicker='Nuts · NDSU Extension', title='Buy them in a sealed can', bg=BG,
               rows=[('Regular bag','3 months',(94,'regular')),('Vacuum-sealed can','1 year',(95,'vacuumsealed'))]),
 'treat': dict(type='card', kicker='Comfort food · NDSU Extension', title='Rotate the cookies', bg=BG,
               rows=[('Chocolate, unopened','1–2 years',(114,'unopened')),('Packaged cookies','2 months',(115,'packaged'))]),
 'notout':dict(type='check', kicker='Not outage food', title='Keep these for normal weeks', bg=BG, compact_rows=True,
               rows=[('Instant noodles, cup soups',False,(118,'instant')),('Rice, pasta, dry beans',False,(119,'rice')),('Powdered milk',False,(120,'powdered')),('Boxed meals, mixes, frozen food',False,(121,'boxed'))]),
 'water': dict(type='quote', kicker='FEMA · Ready.gov', title='1 gallon / person / day', bg=BG,
               rows=[('for drinking and basic cleaning',(131,'drinking')),('enough for several days',(131,'several'))]),
 'co':    dict(type='check', kicker='CDC warning · carbon monoxide', title='Never inside the house or garage', bg=BG, compact_rows=True,
               rows=[('Grill',False,(142,'grill')),('Camp stove',False,(142,'camp')),('Generator',False,(142,'generator'))]),
 'plan3': dict(type='steps', kicker='3 days from one shelf', title='Breakfast · Lunch · Dinner', bg=BG,
               rows=[('Breakfast: cereal, a box of milk, a fruit cup',(153,'breakfast')),('Lunch: tuna on crackers, dried fruit',(154,'lunch')),('Dinner: peanut butter crackers, fruit cup, nuts, a cookie',(155,'dinner'))]),
}
