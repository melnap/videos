# Stocked & Ready V12 – 10 pantry foods for a power outage. Higgsfield B-roll; no readable text or brands, colorful mixed goods allowed.
# NO grill, camp stove or generator anywhere in the house (task rule).
ISL='cbb2bac1-7cf6-47c2-89c5-71af4e45ba61'; STV='a1da0b5a-edce-47dd-bcdb-d4f29d5839a0'; SNK='ee912781-ba88-473c-8ef0-679bf6883266'
PAN='ff09b005-6b35-40df-ad18-7c9d4dd0cd91'; UTL='bedfa356-267d-49ca-b29f-5703735b2d64'; CATH='56d4cff3-ed6a-4690-8415-9851f93c7b0b'
ELEM='<<<b391e55a-d99b-41c9-8bb8-160047c89ba0>>>'
HAIR='ash-blonde shoulder-length hair worn down, loose and natural'
END=(" Natural window light, shallow depth of field, background softly blurred, only a hint of the kitchen visible, real textures, slight imperfections, candid documentary photo."
     " Colorful, varied food and containers are welcome (bright solid-color lids and containers, colorful food), but no letters, no words, no logos, no brand names, no price tags anywhere; freezer bags are plain clear without print. Tight framing angled away from the window; if any window shows it is WHITE-painted with divided panes, any faucet is BRASS, never chrome. The range has no logo and no text on its control panel. Hands natural with five fingers, woman's hands in a sage-green knit cardigan sleeve. Photorealistic, 16:9.")
def K(d): return "Realistic close-up at the oak butcher-block kitchen island of the farmhouse kitchen from the set reference image. "+d+END
def Pn(d): return "Realistic close-up in the pantry from the set reference image (unpainted pine plank shelves softly blurred). "+d+END
def St(d): return "Realistic close-up at the stainless gas range with black cast-iron grates from the set reference image. "+d+END
def Ut(d): return "Realistic close-up in the utility room from the set reference image, at the open white chest freezer. "+d+END
def C(d): return f"{ELEM} The same woman as in the character reference, {HAIR}, sage-green knit cardigan over a white top. "+d+" Same room, same layout and fixtures as the set reference image. Candid documentary photo, natural window light, real skin texture, no text, no labels, no logos, photorealistic, 16:9."
CALM='. calm, slow, gentle movement, single simple action, static or very slow camera, unhurried, peaceful'
def Sk(d): return "Realistic close-up at the white fireclay farmhouse sink with the brass bridge faucet from the set reference image. "+d+END
def Fr(d): return "Realistic view into an open refrigerator in the farmhouse kitchen from the set reference image, plain white shelves, cold light. "+d+END
# Outage mood: power is off, only lantern / flashlight / grey daylight.
ENDN=(" Power outage: no electric light, the room is lit only by a battery lantern or flashlight and a little grey winter daylight, warm-cool contrast, calm, cozy, not scary. Shallow depth of field, background softly blurred, real textures, candid documentary photo."
      " Colorful, varied food packages are welcome (bright solid colors), but no letters, no words, no logos, no brand names, no price tags, no barcodes anywhere; all packages are plain. Never a grill, camp stove, gas canister or generator. Hands natural with five fingers, woman's hands in a sage-green knit cardigan sleeve. Photorealistic, 16:9.")
def KN(d): return "Realistic close-up at the oak butcher-block kitchen island of the farmhouse kitchen from the set reference image. "+d+ENDN
def PnN(d): return "Realistic close-up in the pantry from the set reference image (unpainted pine plank shelves). "+d+ENDN
A=[
('A01','V',PAN,PnN("Dark pantry at night, a flashlight beam falls on full pine shelves: big glass jars of white rice, dry pasta and dried beans, a plain paper bag of flour; everything else is in darkness."),"the flashlight beam slowly sweeps across the shelves from left to right, static camera"),
('A02','V',ISL,K("The farmhouse kitchen in the evening seen wide from the island, warm pendant lights glowing above the island, winter darkness outside the white-painted windows, nobody in the room."),"the pendant lights flicker twice and go out, the room turns dark blue, static camera"),
('A03','V',ISL,KN("A woman's hand pushes the closed white refrigerator door firmly shut in a dim kitchen, grey morning light."),"her hand slowly presses the refrigerator door shut and moves away, static camera"),
('A04','S',UTL,"Realistic close-up in the utility room from the set reference image: an open blue picnic cooler packed with ice, a plain white milk jug, wrapped meat packages, a small plastic container of leftovers and a round dial thermometer standing in the ice."+ENDN),
('A05','S',ISL,Fr("Refrigerator door shelves holding a wedge of orange cheddar, a red squeeze bottle, a yellow squeeze bottle, a jar of pickles, a jar of red jelly and a jar of peanut butter, all plain without labels.")),
('A06','V',ISL,KN("A woman's hand spreads peanut butter from a plain jar onto square crackers on a small wooden board, a battery lantern glowing beside it."),"she slowly spreads peanut butter on a cracker with a butter knife, static camera"),
('A07','S',PAN,PnN("A plain red cracker box standing open, four plain wax-paper cracker sleeves inside, one sleeve opened with crackers spilling onto the pine shelf.")),
('A08','S',ISL,KN("A row of small single-serve shelf-stable milk boxes in plain pastel colors (white, light blue, pale yellow), one with a straw, next to one large plain quart carton.")),
('A09','V',ISL,KN("A woman's hand pours crunchy cereal from a plain colorful box into a blue bowl, then milk from a small single-serve milk box, battery lantern beside it, grey morning light."),"she slowly pours milk from the small box over the cereal, static camera"),
('A10','V',ISL,KN("A woman's hands tear open a plain silver foil tuna pouch above a plate of crackers; no print on the pouch."),"she slowly tears the pouch open along the top, static camera"),
('A11','S',ISL,KN("A shallow wooden bowl of mixed dried fruit: dark raisins, orange dried apricots, prunes and red dried cranberries, a handful of almonds beside it.")),
('A12','S',PAN,PnN("A sealed glass jar of mixed nuts with a metal lid and a plain round metal can of nuts next to a soft clear plastic bag of nuts on a pine shelf.")),
('A13','V',ISL,KN("A woman's hand peels the foil lid off a small clear plastic fruit cup of peach pieces in juice, more plain fruit cups and applesauce cups nearby."),"she slowly peels back the lid, static camera"),
('A14','S',None,"Realistic close-up of an open car glove compartment holding a few granola bars in plain colorful wrappers and a small flashlight, winter daylight, no logos, no text, no brand, photorealistic, 16:9."),
('A15','V',ISL,KN("A small plate of homemade-looking cookies and squares of dark chocolate next to a plain bag of hard candies, a candle and a battery lantern glowing, a cozy blanket edge in the frame."),"a woman's hand slowly takes one cookie from the plate, static camera"),
('A16','S',PAN,PnN("Several plain clear gallon water jugs and sealed water bottles standing on the pantry floor below the pine shelves.")),
('A17','V',ISL,KN("A woman's hands turn the key of a simple manual hand can opener around the rim of a plain unlabeled can."),"she slowly turns the can opener key around the can, static camera"),
('A18','V',PAN,PnN("A plain clear plastic storage tote on a pine shelf filled with peanut butter jar, cracker box, small milk boxes, fruit cups, pouches and bars; a flashlight, batteries and a hand can opener lie on top."),"a woman's hand slowly lays a roll of paper towels on top of the box, static camera"),
('A19','S',PAN,PnN("One pine pantry shelf set apart as an emergency food shelf: a jar of peanut butter, a cracker box, small milk boxes, fruit cups, a jar of nuts, dried fruit and a box of cereal, neatly arranged, a strip of masking tape with an illegible handwritten date.")),
('A20','S',ISL,K("Things that are not outage food on the oak island: plain cups of instant noodles, a plain bag of dry pasta, a plain bag of rice, a plain box of baking mix and a plain pouch of powdered milk.")),
('A21','S',ISL,K("Small glass jars of baby food (pureed carrots, peas, apples) without labels and a bowl of dry dog kibble on the kitchen floor beside the island.")),
('A22','V',ISL,C("She sits at the oak island at dusk during a power outage, a battery lantern lighting her face, quietly eating crackers with peanut butter, calm and cozy, medium shot."),"she calmly takes a bite of a cracker, static camera"),
('A23','S',None,"Realistic photo of a snowy suburban front porch at dusk, a woman's hand in a sage-green cardigan sleeve knocking on a wooden front door, a small paper bag of food in the other hand, no house numbers, no text, photorealistic, 16:9."),
]
