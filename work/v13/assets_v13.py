# Stocked & Ready V13 – 10 Costco foods for winter, 5 never. New Higgsfield B-roll (nano_banana_2 stills, cinematic_studio_video_v2 clips).
# No stores, no logos, no readable text. Big bulk packs are plain. Hair for this video: ash-blonde shoulder-length, worn down.
ISL='cbb2bac1-7cf6-47c2-89c5-71af4e45ba61'; STV='a1da0b5a-edce-47dd-bcdb-d4f29d5839a0'; SNK='ee912781-ba88-473c-8ef0-679bf6883266'
PAN='ff09b005-6b35-40df-ad18-7c9d4dd0cd91'; UTL='bedfa356-267d-49ca-b29f-5703735b2d64'; GDN='5cca4be9-7d1e-4ee5-923b-6ce4f4be6f34'
CATH='56d4cff3-ed6a-4690-8415-9851f93c7b0b'; ELEM='<<<b391e55a-d99b-41c9-8bb8-160047c89ba0>>>'
HAIR='ash-blonde shoulder-length hair worn down, loose and natural'
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
CALM='. calm, slow, gentle movement, single simple action, static or very slow camera, unhurried, peaceful'
# (id, kind S=still V=video start frame, set ref, prompt, [motion for V])
A=[
('N01','S',ISL,K("Wide close view across the oak island crowded with a just-unpacked bulk haul: a huge plain three-liter tin of olive oil, a giant clear clamshell of fresh baby spinach, a flat of five dozen brown eggs in a plain pulp tray, a stack of pale-yellow butter boxes without print, a big plain woven sack of rice, a large plain coffee bag. Abundant, slightly too much.")),
('N02','S',PAN,Pn("A huge plain unlabeled three-liter metal tin of olive oil and a tall plain glass bottle of olive oil on a pine shelf, a little dust, dim cool light.")),
('N03','S',ISL,K("An open clear plastic clamshell of baby spinach going bad: dark, wet, slimy wilted leaves stuck to the plastic, beside a kitchen trash bin lid. Unappetizing but realistic.")),
('N04','S',ISL,K("A flat of five dozen brown eggs in a plain grey pulp egg tray stacked two high on the oak island, close-up.")),
('N05','S',ISL,Fr("Butter blocks in plain white paper wrappers on the refrigerator door shelf, close-up, a carton of milk without print blurred behind.")),
('N07','S',ISL,K("A long curled paper store receipt lying on the oak island next to a white coffee mug; the printing is too small and blurred to read.")),
('N08','S',ISL,K("A colorful assortment of plain groceries on the oak island: cans with bright solid-color labels showing only simple food illustrations, a plain paper sack of flour, a jar of rice, apples, a bag of carrots.")),
('N09','S',ISL,K("A woman's hand with a pencil writing simple sums on a small notepad beside a plain calculator on the oak island; the handwriting is soft and not legible.")),
('N10','S',STV,St("A plain brown paper sack of sugar standing on the counter right beside the gas range while a pot simmers and steam drifts toward the sack.")),
('N11','S',PAN,Pn("A big plain white woven polypropylene sack of rice, folded open at the top, sitting on the pantry floor, rice grains visible inside.")),
('N12','S',PAN,Pn("Four clear airtight food storage containers full of white jasmine rice with snap-lock lids lined up on a pine shelf.")),
('N13','S',UTL,"Realistic close-up on a concrete garage floor: a plain paper sack of rice slumped against the wall, a damp darker patch on the paper at the bottom corner, cold light."+END),
('N14','V',ISL,K("A woman's hands scoop white rice from a big plain open sack with a steel scoop into a clear airtight container on the oak island."),"she slowly pours one scoop of rice into the container, static camera"),
('N15','S',PAN,Pn("Pine pantry shelf with clear airtight containers of rice, flour and sugar and two jars of canned chicken, neat but lived-in, morning light.")),
('N16','V',ISL,K("A woman's hands spoon white flour from a large plain paper flour sack into a clear freezer bag on the oak island."),"she slowly spoons the flour into the bag, a little flour dust, static camera"),
('N17','S',ISL,K("A sealed clear freezer bag of white flour just out of the freezer resting on the oak island, a faint frost on the outside, a small towel beside it.")),
('N18','S',ISL,K("Six stacked short cans of chicken with plain solid-color labels showing only a simple painted chicken illustration, on the oak island.")),
('N19','S',ISL,K("A bowl of chicken noodle soup with carrots and celery, steam rising, a spoon and a folded napkin on the oak island, warm evening light.")),
('N20','V',ISL,K("A woman's hand spoons canned chicken from an opened can into a small glass storage container with a blue lid on the oak island."),"she slowly spoons the chicken into the glass container, static camera"),
('N21','S',ISL,Fr("An opened can of chicken with the lid bent back sitting on a refrigerator shelf, cold light.")),
('N22','S',UTL,Ut("Big plain clear bags of frozen broccoli, green beans and mixed vegetables lying in the open chest freezer, frost on the bags.")),
('N23','S',ISL,K("A big plain clear bag of frozen blueberries on the oak island, frost on the berries, close-up.")),
('N24','S',ISL,K("A bowl of oatmeal topped with a handful of frozen blueberries and a drizzle of honey, morning sun, a spoon beside it.")),
('N25','S',ISL,K("An open bag of frozen blueberries left on the counter, sweating and starting to thaw, a small puddle of purple juice under it.")),
('N26','V',ISL,K("A woman's hands press the air out of a clear bag of frozen blueberries and seal the zipper on the oak island."),"she slowly presses the air out and seals the bag, static camera"),
('N27','V',ISL,K("A woman's hands drop walnuts and pecans from a big plain bag into a small clear freezer bag on the oak island."),"she slowly pours the nuts into the small bag, static camera"),
('N28','S',PAN,Pn("A large plain clear bag of mixed walnuts and pecans sitting on a pine pantry shelf, a little light from the side.")),
('N29','S',ISL,K("Several individually wrapped raw thin-sliced chicken breasts in plain clear plastic, lying in a large plain clear bag on the oak island.")),
('N30','S',ISL,K("Five glass meal-prep containers with sliced cooked chicken breast, rice and broccoli lined up on the oak island.")),
('N31','V',ISL,K("A woman's hand spoons whole coffee beans from a large plain kraft coffee bag into small glass jars on the oak island."),"she slowly spoons the beans into a jar, static camera"),
('N32','S',UTL,Ut("Three small glass jars of whole coffee beans with metal lids standing upright in the open chest freezer between frozen packages.")),
('N33','S',ISL,Fr("A woman's hand takes one block of butter in a white paper wrapper from the refrigerator door shelf, close-up.")),
('N34','S',ISL,K("Four pale-yellow butter blocks in plain white paper wrappers stacked in a neat pile on the oak island, close-up.")),
('N35','V',STV,St("A tablespoon of golden olive oil poured from a plain glass bottle into a black cast-iron skillet on the gas range."),"the oil slowly flows into the pan, static camera"),
('N36','S',ISL,K("A giant plain plastic tub of ground cinnamon with no label next to three small glass spice jars on the oak island.")),
('N37','S',ISL,Fr("A refrigerator shelf crammed full of stacked plain pulp egg cartons, cold light.")),
('N38','S',ISL,K("A single plain grey pulp carton of a dozen brown eggs, lid open, on the oak island, morning light.")),
('N39','V',PAN,Pn("A woman's hand slides an older jar of rice to the front of the pine shelf and places a new full jar behind it."),"she slowly moves the jar forward, static camera"),
('N40','S',PAN,Pn("A well-stocked, tidy but lived-in pantry shelf at golden morning light: airtight containers of rice, flour and sugar, jars, colorful cans with plain solid-color labels.")),
('N43','S',ISL,K("Macro of frozen broccoli florets with fine frost crystals in a clear bowl.")),
('N44','S',GDN,G("A few brown hens pecking in the grass beside the raised beds, soft autumn morning light.")),
('N42','V',SNK,C("She stands at the farmhouse sink window in soft late-autumn light, facing the camera, soft smile, medium shot."),"she gives a small calm goodbye wave with one hand, then lowers it, static camera"),
]
