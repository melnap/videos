# Graphics for Stocked & Ready V14 (11 pantry staples under $5). Numbers exactly as in HANDOFF.md.
# No store or brand names in graphics: prices are "online price, Oct 22, 2026". Anchors = (sentence, first matching word).
BG = 'bg.png'
P = 'Online price · Oct 22, 2026'
def label(kick, title): return dict(type='label', kicker=kick, title=title, bg=BG)
def life(kick, title, rows): return dict(type='card', kicker=kick, title=title, bg=BG, rows=rows)
def price(n, item, size, cost, a, extra=None):
    rows = [(size, cost, a)] + ([extra] if extra else [])
    return dict(type='card', kicker=(f'Number {n} · {P}' if n != 'bonus' else f'Bonus · {P}'), title=item, bg=BG, rows=rows)
GFX = {
 'cpi':   life('Grocery prices · BLS CPI, Sept 2026', 'Up a little under 2 %', [('Groceries, past 12 months', '+1.8 %', (17, 'grocery'))]),
 'beef':  life('2026 forecast · USDA ERS', 'Beef costs more', [('Beef', '+9.4 %', (18, 'beef'))]),
 'n11':   label('Number 11', 'White vinegar'),
 'p11':   price(11, 'White vinegar', '1 gallon', '$3.94', (24, 'gallon'), ('Per ounce', '≈ 3¢', (25, 'thats'))),
 'vin':   life('White vinegar · NDSU Extension', 'Keeps for years', [('Unopened', '2 years', (34, 'two')), ('Opened', '1 year', (34, 'year'))]),
 'n10':   label('Number 10', 'Popcorn kernels'),
 'p10':   price(10, 'Popcorn kernels', '32 oz bag', '$2.47', (40, 'thirtytwoounce'), ('Per ounce', 'under 8¢', (41, 'thats'))),
 'pop':   life('Popcorn · NDSU Extension', 'Kernels outlast the bags', [('Kernels, airtight', '2 years', (46, 'two'))]),
 'n9':    label('Number 9', 'Chicken bouillon'),
 'p9':    price(9, 'Chicken bouillon', '3.75 oz jar', '$2.08', (54, 'threepointsevenfiveounce'), ('Per serving', '≈ 8¢', (54, 'twentyfive'))),
 'n8':    label('Number 8', 'Evaporated milk'),
 'p8':    price(8, 'Evaporated milk', '1 can', '$1.00', (63, 'evaporated')),
 'evap':  life('Evaporated milk · NDSU Extension', 'Out of the can once it’s open', [('Unopened, shelf', '12 months', (69, 'twelve')), ('Opened, fridge', '4–5 days', (70, 'four'))]),
 'n7':    label('Number 7', 'Canned diced tomatoes'),
 'p7':    price(7, 'Diced tomatoes', '28 oz can', '$1.67', (74, 'twentyeightounce')),
 'n6':    label('Number 6', 'Spaghetti'),
 'p6':    price(6, 'Spaghetti', '32 oz box', '$2.24', (84, 'twopound'), ('Per ounce', '≈ 7¢', (85, 'thats'))),
 'pasta': life('Pasta · NDSU Extension', 'Keep it airtight', [('Unopened', '2 years', (87, 'two')), ('Opened', '1 year', (87, 'year'))]),
 'n5':    label('Number 5', 'Cornmeal'),
 'p5':    price(5, 'Yellow cornmeal', '80 oz bag', '$4.28', (96, 'eightyounce')),
 'corn':  life('Cornmeal, opened · NDSU Extension', 'Keep it cold and closed', [('Pantry', '6–12 months', (100, 'six')), ('Refrigerator', '≈ 1 year', (100, 'about'))]),
 'n4':    label('Number 4', 'Peanut butter'),
 'p4':    price(4, 'Peanut butter', '40 oz jar', '$4.18', (106, 'fortyounce'), ('Per ounce', '≈ 10¢', (107, 'thats'))),
 'pb':    life('Peanut butter · NDSU Extension', 'Open one jar at a time', [('Unopened', '6–24 months', (110, 'six')), ('Opened, pantry', '2–3 months', (111, 'two'))]),
 'n3':    label('Number 3', 'Oats'),
 'p3':    price(3, 'Quick oats', '42 oz canister', '$4.18', (118, 'fortytwoounce'), ('Breakfasts', '≈ 30', (119, 'thirty'))),
 'oats':  life('Oats · NDSU Extension', 'Lid on tight', [('Unopened', '12 months', (123, 'twelve')), ('Opened', '6–12 months', (123, 'six'))]),
 'n2':    label('Number 2', 'Rice'),
 'p2':    dict(type='compare', kicker='Rice · price per pound', title='Well under the average', bg=BG,
              cols=[dict(head='5 lb bag, $3.52', big='≈ $0.70/lb', a=(128, 'thats'), accent=True),
                    dict(head='National avg. (BLS, Aug 2026)', big='$1.11/lb', a=(129, 'national'))]),
 'p1':    price(1, 'Pinto beans', '4 lb bag', '$3.82', (139, 'fourpound'), ('Per pound', 'under $1', (140, 'thats'))),
 'beans': life('Dried beans · NDSU Extension', 'Buy a year, not five', [('Airtight container', '12 months', (145, 'twelve'))]),
 'bonus': label('Bonus', 'All-purpose flour'),
 'pflour':price('bonus', 'All-purpose flour', '5 lb bag', 'under $3', (156, 'fivepound')),
 'flour': life('White flour, opened · NDSU Extension', 'Airtight container', [('Pantry', '6–8 months', (158, 'six')), ('Refrigerator', '≈ 1 year', (158, 'about'))]),
 'total': life('One of each · online prices, Oct 22, 2026', '11 staples, all under $5', [('Total', '≈ $33', (163, 'all'))]),
}
