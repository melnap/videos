# Graphics for Stocked & Ready V18 (10 foods your freezer ruins). Facts exactly as spoken in script.txt / HANDOFF.md.
# No brand names or logos. Anchors = (sentence, first matching word, normalised: lowercase letters and digits only).
BG = 'bg.png'
N = 'NDSU Extension'
MO = 'Univ. of Missouri Extension'
WSU = 'WSU Extension'
FS = 'FoodSafety.gov'
DO = 'Do this instead'
def label(kick, title, small=False): return dict(type='label', kicker=kick, title=title, bg=BG, small=small)
def card(kick, title, rows): return dict(type='card', kicker=kick, title=title, bg=BG, rows=rows)
GFX = {
 'ice':     card('Why it happens', 'Ice crystals', [('Water in food', 'turns into ice crystals', (22, 'ice')),
                                                    ('The crystals', 'push through soft cell walls', (23, 'push')),
                                                    ('After thawing', 'water runs out, texture collapses', (23, 'water'))]),
 'emul':    card('USDA food safety guidance', 'Creamy mixtures split', [('Mayonnaise or cream', 'separate and look curdled', (26, 'separate'))]),
 'src':     card('Sources in this video', 'Where the facts come from', [('USDA', 'freezing guidance', (28, 'usdas')),
                                                                         (FS, 'storage chart', (28, 'storage')),
                                                                         ('Extension guides', 'Missouri · NDSU · Mississippi State · WSU', (28, 'extension'))]),
 'n10':     label('Number 10', 'Lettuce & salad greens'),
 'i10':     card(DO, 'Buy greens for this week', [('Salad greens', 'this week only, not the month', (35, 'week')),
                                                  ('For cooking', 'a bag of frozen spinach', (36, 'frozen'))]),
 'n9':      label('Number 9', 'Mayonnaise salads'),
 'i9':      card(DO, 'Freeze the parts, not the salad', [('Cooked diced chicken', 'freezes well on its own', (46, 'chicken')),
                                                         ('Cooked pasta', 'freeze it plain', (47, 'pasta')),
                                                         ('Mayo & crunchy veg', 'stir in the day you serve', (48, 'stir'))]),
 'n8':      label('Number 8', 'Eggs in the shell'),
 'i8':      card(DO, 'Freeze eggs out of the shell', [('Beat gently', 'pour into an ice cube tray', (57, 'pour')),
                                                      ('1 cube', '= 1 egg for baking', (57, 'cube'))]),
 'n7':      label('Number 7', 'Hard-boiled eggs'),
 'i7':      card(DO, 'Boil only what you need', [('Deviled eggs', 'make them fresh', (66, 'fresh'))]),
 'n6':      label('Number 6', 'Sour cream'),
 'i6':      card(f'{DO} · {N}', 'Use it in cooking', [('About to go bad?', 'freeze it anyway', (76, 'bad')),
                                                      ('The grainy texture', 'still works in cooking', (76, 'cooking'))]),
 'n5':      label('Number 5', 'Cream sauces & milk gravies', small=True),
 'i5':      card(DO, 'Add the cream when you reheat', [('Gravy', 'broth-based freezes better', (90, 'brothbased')),
                                                       (f'Creamy sauce · {MO}', 'thicken with waxy rice flour', (92, 'waxy'))]),
 'n4':      label('Number 4', 'Custard & cream pies'),
 'i4':      card(f'{DO} · {MO}', 'Freeze the crust, not the pie', [('Unbaked crust', '6–8 weeks in the freezer', (100, 'six'))]),
 'n3':      label('Number 3', 'Boiled & baked potatoes', small=True),
 'i3':      card(f'{DO} · {WSU}', 'Mashed is different', [('Mashed potatoes', 'a freeze-ahead food', (109, 'mashed')),
                                                          ('Soup or stew', 'leave the potatoes out', (110, 'soup'))]),
 'n2':      label('Number 2', 'Pasta & rice in a sauce', small=True),
 'i2':      card(DO, 'Freeze the sauce alone', [('Freezes well', 'spaghetti sauce, chili, soup base', (118, 'spaghetti'))]),
 'n1':      label('Number 1', 'Food left in the can'),
 'can':     card('Frozen cans · USDA', 'Rusted or burst seams', [('Throw it out', 'immediately', (131, 'immediately')),
                                                                  ('Never', 'taste it', (132, 'taste'))]),
 'i1':      card(DO, 'Never freeze food in its can', [('Leftovers', 'into a freezer container', (135, 'move')),
                                                      ('Garage or shed', 'bring cans in before the first hard freeze', (136, 'bring'))]),
 'bacon':   card('Cured meats · USDA', 'Use them first', [('Bacon & sausage', '1–2 months in the freezer', (146, 'one'))]),
 'hcream':  card(f'Cream · {N}', 'Only heavy cream holds up', [('Light cream, half-and-half', 'don’t freeze well', (149, 'light')),
                                                               ('Heavy cream', '40 % fat or more', (150, 'forty'))]),
 'refrz':   card('Refreezing · USDA', 'Where did it thaw?', [('Thawed in the fridge', 'OK to refreeze', (164, 'safe')),
                                                             ('Thawed on the counter', 'never refreeze', (165, 'never'))]),
 'thaw':    card('Safe thawing · USDA', 'Only three safe ways', [('1', 'in the refrigerator', (166, 'refrigerator')),
                                                                 ('2', 'in cold water', (166, 'cold')),
                                                                 ('3', 'in the microwave', (166, 'microwave'))]),
 'final':   card('Before it goes in the freezer', 'Two questions', [('Mostly water?', 'like lettuce or a boiled potato', (173, 'water')),
                                                                    ('Creamy?', 'like mayonnaise or a cream sauce', (174, 'creamy')),
                                                                    ('Yes to either', 'freeze the parts, not the dish', (175, 'parts'))]),
}
