# Stocked & Ready V17 – 15 holiday foods you can freeze now. New Higgsfield B-roll (nano_banana_2 stills, cinematic_studio_video_v2 clips).
# No stores, no logos, no readable text. Big bulk packs are plain. Hair for this video: a neat low bun at the nape.
ISL='cbb2bac1-7cf6-47c2-89c5-71af4e45ba61'; STV='a1da0b5a-edce-47dd-bcdb-d4f29d5839a0'; SNK='ee912781-ba88-473c-8ef0-679bf6883266'
PAN='ff09b005-6b35-40df-ad18-7c9d4dd0cd91'; UTL='bedfa356-267d-49ca-b29f-5703735b2d64'; GDN='5cca4be9-7d1e-4ee5-923b-6ce4f4be6f34'
CATH='56d4cff3-ed6a-4690-8415-9851f93c7b0b'; ELEM='<<<b391e55a-d99b-41c9-8bb8-160047c89ba0>>>'
HAIR='warm ash-blonde hair worn in a neat low bun at the nape of her neck, a few soft strands framing the face'
LIVE="The kitchen looks lived-in and in use, cooking in progress: a few crumbs and drips on the counter, a used linen dish towel, a spoon and a knife lying around, an opened package or two, a cutting board with scraps, a couple of dishes or a pot in the background, nothing perfectly arranged, not a showroom."
END=(" Natural window light, shallow depth of field, background softly blurred, only a hint of the kitchen visible, real textures, slight imperfections, candid documentary photo."
     " Colorful, varied food and containers are welcome, but no letters, no words, no logos, no brand names, no price tags, no barcodes anywhere; bags and packs are plain without print."
     " If any window shows it is WHITE-painted with divided panes, any faucet is BRASS. Hands natural with five fingers, woman's hands in a sage-green knit cardigan sleeve. Photorealistic, 16:9.")
def K(d): return "Realistic close-up at the oak butcher-block kitchen island of the farmhouse kitchen from the set reference image. "+d+END
def Pn(d): return "Realistic close-up in the pantry from the set reference image (unpainted pine plank shelves softly blurred). "+d+END
def St(d): return "Realistic close-up at the stainless gas range with black cast-iron grates from the set reference image. "+d+END
def Ut(d): return "Realistic close-up in the utility room from the set reference image, at the open white chest freezer. "+d+END
def Fr(d): return "Realistic view into an open refrigerator in the farmhouse kitchen from the set reference image, plain white shelves, cold light. "+d+END
def G(d): return "Realistic photo in the garden from the set reference image (weathered raised beds, picket fence, white farmhouse softly blurred). "+d+END
def C(d): return f"{ELEM} The same woman as in the character reference, {HAIR}, sage-green knit cardigan over a white top. "+d+" Same room, same layout and fixtures as the set reference image. Candid documentary photo, natural window light, real skin texture, no text, no labels, no logos, photorealistic, 16:9."
DARK=(" Power outage in the evening: the only light is a warm metal camping lantern or a candle, deep shadows, cosy and calm, shallow depth of field, real textures, candid documentary photo."
      " No letters, no words, no logos, no brand names, no price tags, no barcodes anywhere; cans and packs are plain without print."
      " Hands natural with five fingers, woman's hands in a sage-green knit cardigan sleeve. Photorealistic, 16:9.")
def Kd(d): return "Realistic close-up at the oak butcher-block kitchen island of the farmhouse kitchen from the set reference image. "+d+DARK
def Pd(d): return "Realistic view in the pantry from the set reference image (unpainted pine plank shelves). "+d+DARK
A=[
('X01','S',ISL,K("A small kitchen trash bin with the lid open, holding a half carton of cream, a cup of egg whites, a plain bag of fresh cranberries and a bowl of leftover gravy, holiday leftovers about to be thrown away.")),
('X02','S',ISL,K("Little mounds of sweetened whipped cream spooned onto a parchment-lined metal tray, ready for the freezer.")),
('X03','S',ISL,K("A mug of hot cocoa with a small frozen mound of whipped cream melting on top, a fir sprig beside it.")),
('X04','S',ISL,K("Two blocks of cream cheese still in plain silver foil wrappers going into a plain clear freezer bag.")),
('X05','S',ISL,K("A big wedge of yellow cheddar cut into neat half-pound pieces on a board, two pieces already wrapped tightly in plastic wrap.")),
('X06','V',ISL,K("A woman's hand pours a little milk off the top of a plain clear plastic gallon milk jug into a glass, leaving room in the jug."),"she slowly pours a little milk into the glass, static camera"),
('X07','S',ISL,K("Four small plain freezer containers each holding one cup of buttermilk, a strip of masking tape on each lid, written on with a marker, soft and not legible.")),
('X08','S',STV,St("A woman's hand slides a tray of dinner rolls wrapped in aluminum foil into a warm oven.")),
('X09','S',ISL,K("A log of cookie dough wrapped in parchment beside a metal tray of evenly scooped cookie dough balls, ready to flash freeze.")),
('X10','S',UTL,Ut("Several unbaked pie crusts stacked flat with parchment between them in a plain clear freezer bag inside the open white chest freezer.")),
('X11','V',ISL,K("A frozen unbaked double-crust apple pie on the oak island, a woman's hand cutting small vents into the frosty top crust with a paring knife."),"she slowly cuts a small vent into the top crust, static camera"),
('X12','S',ISL,K("Leftover brown gravy ladled into three small round freezer containers with lids on the oak island.")),
('X13','S',STV,St("A baking dish of holiday stuffing being reheated on the stovetop, a simple dial food thermometer with no readable numbers pushed into the middle.")),
('X14','S',ISL,K("Sliced roast turkey breast arranged in shallow glass storage containers with a little broth, a carving board with the turkey carcass behind.")),
('X15','V',ISL,K("A woman's hand pours gently mixed whole egg from a glass measuring cup into a white silicone ice cube tray, one section at a time."),"she slowly pours the egg into the tray, static camera"),
('X16','S',ISL,K("Separated egg yolks in a small glass bowl with a pinch of salt being added from fingertips, egg whites in a second bowl.")),
('X17','S',STV,St("Heavy cream poured from a plain white carton without print into a pot of creamy potato soup on the gas range.")),
('X42','V',SNK,C("She stands at the farmhouse sink window on a soft grey late-November day, a bare garden outside, facing the camera, soft smile, medium shot."),"she gives a small calm goodbye wave with one hand, then lowers it, static camera"),
]
