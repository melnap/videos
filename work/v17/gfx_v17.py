# Graphics for Stocked & Ready V17 (15 holiday foods you can freeze now). Numbers exactly as in HANDOFF.md.
# No brand names or logos. Anchors = (sentence, first matching word).
BG = 'bg.png'
N = 'NDSU Extension'
MO = 'Univ. of Missouri Extension'
FS = 'FoodSafety.gov'
def label(kick, title, small=False): return dict(type='label', kicker=kick, title=title, bg=BG, small=small)
def card(kick, title, rows): return dict(type='card', kicker=kick, title=title, bg=BG, rows=rows)
GFX = {
 'rule':    card(f'The one rule · {FS}', 'Frozen at 0°F', [('Safety', 'indefinitely', (20, 'indefinitely')), ('Storage times', 'quality only', (21, 'quality'))]),
 'n15':     label('Number 15', 'Fresh herbs'),
 'n14':     label('Number 14', 'Cranberries'),
 'cran':    card('Cranberries · Penn State Extension', 'Straight from the bag', [('In the freezer', 'up to 12 months', (40, 'twelve')),
                                                                              ('Before cooking', 'rinse, no thawing', (41, 'rinse'))]),
 'n13':     label('Number 13', 'Heavy cream'),
 'cream':   card(f'Heavy cream · {N}', 'It needs the fat', [('Freezes well', '40 % butterfat or more', (46, 'forty')),
                                                           ('Light cream, half-and-half', "don't freeze well", (47, 'lighter'))]),
 'n12':     label('Number 12', 'Cream cheese'),
 'n11':     label('Number 11', 'Hard cheese'),
 'cheese1': card(f'Hard cheese · {N}', 'Cut it first', [('Pieces of', '½ lb or less', (65, 'half'))]),
 'cheese2': card('Cheddar, Swiss · WSU Extension', 'Good for cooking', [('In the freezer', '≈ 6 months', (69, 'six'))]),
 'n10':     label('Number 10', 'Milk'),
 'n9':      label('Number 9', 'Buttermilk'),
 'n8':      label('Number 8', 'Bread & rolls'),
 'bread':   card(f'Bread & rolls · {MO}', 'Bake ahead', [('In the freezer', '≈ 3 months', (93, 'three')), ('To serve', 'thaw, foil, warm oven', (94, 'thaw'))]),
 'n7':      label('Number 7', 'Cookie dough'),
 'cookie':  card(f'Cookie dough · {MO}', 'Make it in November', [('In the freezer', '≈ 3 months', (99, 'three'))]),
 'n6':      label('Number 6', 'Pie crust'),
 'crust':   card(f'Pie crust · {MO}', 'No thawing needed', [('Unbaked crust', '6–8 weeks', (107, 'six'))]),
 'n5':      label('Number 5', 'Unbaked fruit pies'),
 'fpie':    card(f'Unbaked fruit pie · {MO}', 'Bake from frozen', [('In the freezer', '≈ 8 months', (113, 'eight'))]),
 'pump':    card(f'Pumpkin pie · {MO}', 'Much shorter', [('In the freezer', '4–5 weeks', (116, 'four'))]),
 'n4':      label('Number 4', 'Gravy'),
 'gravy':   card(f'Gravy & sauces · {MO}', 'Small rigid containers', [('In the freezer', '3–4 months', (125, 'three'))]),
 'n3':      label('Number 3', 'Stuffing'),
 'stuff':   card(f'Stuffing · {MO}', 'Eat it before Christmas', [('In the freezer', '≈ 1 month', (133, 'thaw')), ('Reheat to', '165 °F all the way through', (133, 'hundred'))]),
 'n2':      label('Number 2', 'Leftover turkey'),
 'two':     card('The 2-hour rule · USDA', 'Within 2 hours of dinner', [('Room temperature', 'max. 2 hours', (138, 'two')),
                                                                          ('Turkey', 'off the bones, sliced, shallow containers', (139, 'meat'))]),
 'poultry': card('Cooked turkey in the freezer', 'Meal-sized portions', [(f'Roast poultry · {MO}', '2–4 months', (142, 'two')),
                                                                         (f'Cooked poultry · {FS}', '2–6 months', (142, 'six'))]),
 'n1':      label('Number 1', 'Eggs'),
 'eggs1':   card('Eggs · NCHFP', 'Out of the shell', [('Never', 'in the shell', (152, 'freeze')), ('3 Tbsp mixed egg', '= 1 egg', (152, 'three'))]),
 'eggs2':   card('Egg whites · NCHFP', 'Nothing added', [('2 Tbsp', '= 1 white', (157, 'two'))]),
 'yolk':    card('Egg yolks · NCHFP', 'So they don’t turn gummy', [('Stir in', 'a pinch of salt or sugar', (160, 'pinch'))]),
 'twelve':  card(f'Raw whites & yolks · {FS}', 'A whole year', [('In the freezer', '≈ 12 months', (162, 'twelve'))]),
 'final':   card('The habit', 'Could this go in the freezer instead?', [('Freeze it', 'flat, small portions', (170, 'flat')),
                                                                         ('Press out', 'the air', (170, 'air')),
                                                                         ('Write', 'name and date', (170, 'name'))]),
}
