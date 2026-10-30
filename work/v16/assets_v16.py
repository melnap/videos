# Stocked & Ready V16 – 15 foods FEMA says to store for winter. New Higgsfield B-roll (nano_banana_2 stills, cinematic_studio_video_v2 clips).
# No stores, no logos, no readable text. Big bulk packs are plain. Hair for this video: one loose low side braid over the left shoulder.
ISL='cbb2bac1-7cf6-47c2-89c5-71af4e45ba61'; STV='a1da0b5a-edce-47dd-bcdb-d4f29d5839a0'; SNK='ee912781-ba88-473c-8ef0-679bf6883266'
PAN='ff09b005-6b35-40df-ad18-7c9d4dd0cd91'; UTL='bedfa356-267d-49ca-b29f-5703735b2d64'; GDN='5cca4be9-7d1e-4ee5-923b-6ce4f4be6f34'
CATH='56d4cff3-ed6a-4690-8415-9851f93c7b0b'; ELEM='<<<b391e55a-d99b-41c9-8bb8-160047c89ba0>>>'
HAIR='warm ash-blonde hair worn in one loose low side braid resting over her left shoulder, a few soft strands framing the face'
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
('W01','S',PAN,Pd("A fully stocked pantry in near darkness: shelves packed with flour sacks, dry beans, pasta boxes and baking mixes, lit only by one camping lantern on the floor.")),
('W02','S',ISL,Kd("A steaming mug of hot cocoa next to a lit candle and a small plain jar of instant coffee with a closed lid.")),
('W03','S',PAN,Pn("A tall plain metal storage tin with a tight lid full of dry cereal and granola on a pine shelf, the lid just lifted to show the cereal.")),
('W04','S',ISL,K("A woman's hands slide crackers wrapped in a clear plastic bag into a plain round metal tin with a lid.")),
('W05','V',ISL,K("A woman's hand pours dried apricots and raisins from an opened plain bag into a glass screw-top jar."),"the dried fruit slowly pours into the jar, static camera"),
('W06','S',PAN,Pn("A row of small plain unlabeled juice cans in solid colours, orange, red and green, on a pine pantry shelf.")),
('W07','S',PAN,Pn("Plain white shelf-stable milk cartons without print stacked on a pine shelf beside a plain metal can of powdered milk.")),
('W08','S',ISL,Kd("A bowl of canned vegetable soup eaten lukewarm by lantern light, a spoon in the bowl, an opened plain can beside it.")),
('W09','S',PAN,Pn("A dented and slightly swollen plain can set apart from a neat row of good cans on a pine shelf.")),
('W10','V',ISL,K("A woman's hand turns the key of a simple manual can opener on a plain can of chicken."),"she slowly turns the can opener, static camera"),
('W11','S',PAN,Pn("A small open emergency supply bin on a pine shelf: a manual can opener, candles, matches in a jar, a flashlight and a few plain cans.")),
('W12','S',PAN,Pn("A plain white vitamin bottle without label and a small plain pill organizer next to the emergency supply bin on a pine shelf.")),
('W13','S',ISL,Kd("Crackers spread with peanut butter on a small plate by lantern light, an opened plain jar of peanut butter with a knife.")),
('W14','S',PAN,Pn("Several clear one-gallon water jugs without labels lined up on the pantry floor under the pine shelves.")),
('W15','S',ISL,Kd("A closed white refrigerator in a dark kitchen during a power outage, a woman's hand resting on the closed door, lantern light.")),
('W16','S',PAN,Pn("Large sealed white food-grade buckets with lids and big plain metal cans for wheat, white rice and beans on the lowest pine shelf.")),
('W42','V',SNK,C("She stands at the farmhouse sink window on a snowy winter day, fresh snow outside, facing the camera, soft smile, medium shot."),"she gives a small calm goodbye wave with one hand, then lowers it, static camera"),
]
