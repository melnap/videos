# Stocked & Ready V11 – buy butter in November, freeze it all winter. Higgsfield B-roll; no readable text or brands, colorful mixed goods allowed.
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
A=[
('B01','V',ISL,K("A woman's hands slide a plain pale-yellow butter box with no print into a heavy clear freezer bag on the oak island, three more plain butter boxes beside it."),"she slowly slides the box into the bag, static camera"),
('B02','S',ISL,K("A neat stack of plain pale-yellow butter boxes without any print and a few butter sticks in plain white paper wrappers on the oak island, a blue-lidded container and a red mixing bowl nearby.")),
('B03','V',ISL,K("A woman's hands press the air out of a clear freezer bag holding a plain butter box and seal the zipper on the oak island."),"she slowly presses the air out and seals the bag, static camera"),
('B04','V',ISL,K("A woman's hand writes a date with a black marker on a strip of tape on a freezer bag of butter boxes; the writing is soft and not legible."),"she writes slowly with the marker, static camera"),
('B05','V',UTL,Ut("A woman's hand places a sealed freezer bag of plain butter boxes at the back of the open chest freezer behind other frozen packages."),"she slowly sets the bag down at the back, static camera"),
('B06','V',ISL,Fr("A woman's hand places a frozen stick of butter in a plain white paper wrapper onto a small plate on the refrigerator shelf."),"she slowly sets the butter down, static camera"),
('B07','V',ISL,K("A frozen stick of butter is grated on the large holes of a stainless box grater straight into a glass bowl of flour on the oak island, woman's hands."),"she grates the frozen butter slowly, shreds fall into the flour, static camera"),
('B08','V',ISL,K("A fork gently tosses shreds of frozen butter into flour in a glass bowl on the oak island."),"the fork slowly tosses the butter shreds, static camera"),
('B09','S',STV,St("A baking sheet of tall golden flaky biscuits fresh from the oven resting on the stovetop.")),
('B10','S',ISL,K("A golden flaky double-crust pie cooling on a wire rack on the oak island.")),
('B11','V',ISL,K("A knife slices a cold stick of butter into tablespoon pats on a wooden board."),"the knife slowly cuts one pat, static camera"),
('B12','S',ISL,K("Tablespoon pats of butter laid in rows on a parchment-lined plate, lightly frosted from the freezer, a clear freezer bag beside it.")),
('B13','V',STV,St("A frozen pat of butter dropped onto steaming white rice in a pan on the gas range, starting to melt."),"the butter pat slowly melts into the rice, static camera"),
('B14','V',ISL,K("A spoon stirs honey and a sprinkle of cinnamon into softened butter in a small ceramic bowl on the oak island, a honey jar beside it."),"the spoon slowly folds the honey into the butter, static camera"),
('B15','V',ISL,K("A woman's hands roll softened herb butter into a neat log in clear plastic wrap on the oak island."),"she slowly rolls the log, static camera"),
('B16','S',ISL,K("A round slice of frozen garlic-herb butter melting on top of roasted potatoes in a blue dish.")),
('B17','V',STV,St("Butter foaming and turning golden brown in a stainless skillet on the gas range, brown flecks at the bottom."),"the butter foams gently and browns, slow, static camera"),
('B18','V',ISL,K("Golden brown butter poured slowly from a small saucepan into a silicone ice cube tray on the oak island."),"the brown butter pours slowly into the tray, static camera"),
('B19','S',ISL,K("A single stick of butter on a white butter dish with its lid off on the oak island, a butter knife beside it.")),
('B20','S',ISL,K("A knife cuts a thin dry white freezer-burned end off a stick of butter on a wooden board.")),
('B21','S',ISL,K("A small notepad and pen on the oak island next to a plain butter box, a short handwritten number list that is soft and not legible.")),
('B22','S',ISL,K("A bowl of mashed potatoes with a pat of butter melting on top, a holiday dinner table setting softly blurred.")),
('B23','V',STV,St("A whisk stirs a golden roux of butter and flour in a skillet on the gas range."),"the whisk slowly stirs the roux, static camera"),
('B24','S',STV,St("A golden grilled cheese sandwich in a cast-iron skillet on the gas range, a red bowl of tomato soup beside the range.")),
('B25','S',ISL,K("A stack of pancakes with a melting pat of butter and syrup on a plate on the oak island, snowy daylight in the soft background.")),
('Q02','V',ISL,C("She stands at the oak island and slowly writes a short list on a small notepad, plain butter boxes beside her, seen slightly from the side, medium shot, calm.")," she writes slowly, static camera"),
('Q03','V',SNK,C("She stands at the farmhouse sink window in soft late-autumn light, facing the camera, soft smile, medium shot."),"she gives a small calm goodbye wave with one hand, then lowers it, static camera"),
]
