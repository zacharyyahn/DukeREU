import pandas as pd 

waste_disposal = """trash pulper room
garbage disposal space
acid battery space or shop
trash room
incinerator
incinerator room
trash disposal operation
hazmat reuse
pulper/shredder room
hazmincen
plastic waste processor room
plastic waste processing room
classified document destruction space""".split("\n")

storage = """utility storeroom
utility space
utility room
equipment space or storeroom
hold
main storeroom
cargo hold
holds/supply areas
supply/stores/cargo other
ships service storeroom
utility space or shop
paint storeroom
gear locker
vehicle space
equipment space
equipment storeroom
general storeroom
storage battery space or shop
gear space or shop
cleaning gear space
cleaning gear space or shop
gear battery space or shop
equipment space or shop
co2 cylinder storeroom
""".split("\n")

ship_maintenance = """
general workshop
area (functional physical space or shops) other
ground support equipment (gse) space or shop
hull repair space or shop
repair space, office or shop
ht  space, office or shop
ht space, office or shop
v2 maint support/tool space or shop
a-division office, space or shop
general workshop or space
launcher space or shop
m-division space, office or shop
refrigeration machinery  space or shop
r-division space, office or shop
filter cleaning space or shop
composite space or shop
electrical rewind space or shop
maintenance area
corrosion control space or shop
structures space or shop
engineering/aux/repair
engineering/aux/repair other
m-division space
industrial facilities other
general space or shop
boatswains space or shop
paint mixing & issue
canvas space or shop 
repair space
et space or shop
engineering log room
canvas & bunting space or shop
oxidizer space or shop
operational/industrial building/plant other
ht space
tool issue space or shop
mechanical calibration facility
display repair space or shop
repair space or shop
electronic repair space or shop
metalsmith & machine space or shop
machine & weld space or shop
repair space or shop
metalsmith space or shop
rewind shop
fuel/oil space or shop
hose and tube space or shop
electrical tool space or shop
refrigeration machinery room
oil pump space
ac&r machinery space or shop
portable tool shop or area
hull/underwater/tanks/voids other
machine space or shop
carpenter space or shop
survival equipment space or shop
decon space or station
metal & pipe space or shop
valve space or shop
lighting space or shop
computer space or shop
socket pouring space or shop
refrigeration machinery space or shop
hydraulics space or shop
pipe space or shop
battery space or shop
pipe and dc space or shop
electrical/damage control space or shop
electrical space or shop
electrical service space or shop
hydraulic pneumatic space or shop
compressor space or shop
co2 cylinder space or shop
bilge
""".split("\n")

ship_operations = """
escape trunk
steering gear room
main machinery room (mmr)
machinery room (mer)
auxiliary machinery room (amr or aux)
motor pool/garage 
combat information center (cic)
sail loft 
r-division space (damage control)
pump room
after steering
capstan machinery space or shop
plotting room
cht pump room or space
anchor windlass space
chain locker
cvic
central admin space or shop
""".split("\n")

material_handling = """
kingpost
winch/crane space 
ras winch space or shop
conveyor
vertical package conveyor
crane space or shop
unrep/ras space or shop
handling space or shop
hoist space or shop
forklift space or shop
flammable cargo
boom
handling area
rast machinery room
diesel space or shop
diesel generator space or shop
forklift space
""".split("\n")

misc_ship_locations = """
photo lab
open ocean
mount
elevator
elevator space
pier
void
main deck
barge
boat space or shop
transports other
fan
fan room
amidships
stern
waterfront area other
control space
other elevated area
port bow
vestibule
brow
forecastle
fantail
""".split("\n")

personnel_support = """
barracks
recreation area or space
recreation area or space
crew barber
wardroom scullery
lounge
physical fitness room
facility/school
crew shelter
wardroom galley
reacreation area or space
chiefs/cpo mess
cpo/nco scullery
library
recreational area other
wardroom pantry
laundry issue
personnel landing
ward
brig
issue room
learning resource center
bread room
inpatient area
conference room
chaplain space
galley
first class mess
gym
wardroom mess
scullery
crew laundry
mess deck
x-division space
support facility other
main medical area
crew mess
veg prep room
Lounge
bakery
battle dressing station
laundry press
chiefs mess
basketball court
training space
cleaning gear issue or locker
crew scullery
wardroom
cpo/nco galley
ships store/mini-mart
laundry
flag officer galley
quarterdeck
minor operating room
test lab
""".split("\n")

medical_dental = """
preventive dentistry
sterilizing room
medical/dental other
medical records room
dental stowage
medical department office or admin
medical treatment room
blood bank
general medical space or area
medical/crew mess room
dental x-ray
exam room
""".split("\n")

personnel_quarters = """
troop berthing
shower & water closet
chiefs/cpo berthing
head
berthing area
cabin
enlisted quarters
washroom
stateroom
general habitability space
crew space - other
water closet
habitability other 
first lieutenants space or shop
crew space or shop
crew berthing
shower
""".split("\n")

hangar = """
hangar bay
hangar deck
hangar 
""".split("\n")

weapons_and_defense = """
weapons/ordnance other
weapons forklift
chem or cbr warfare defense space
ciws
magazine
ordnance space or shop
armory
gun support space or shop
weapons dept office or space
ram space or shop
shop - ordnance
gunnery space or shop
ordnance/gun system space or shop
gun space or shop
armory space or shop
ram
nixie equipment space or shop
ciws nr2/aviation space or shop
towed array space or shop
""".split("\n")

aircraft_support = """
ejection seat space or shop
airframes space or shop
air, government
ciws nr2/aviation space
launch access space or shop
tire and wheel space or shop
crash & salvage aviation fuel repair space or shop
jet engine space or shop
jp-5 filter space or shop
fuel test space or shop
helo repair space or shop
avionics space or shop
garage
aircraft elevator machinery space or shop
aircraft elevator space or shop
aviation/air/aimd other space or shop
catapult space or shop
arresting gear machinery space or shop
calibration space or shop
fuels repair space or shop
jet shop space or shop
aircraft fueling space or shop
ready room 
refueling pits
fueling space
jp5 pump room
fueling space or shop
obogs space or shop
paraloft
jp-5 filter space
jp5 pump space
elevator machinery space
air department space
tank
barricade space or shop
elevator space or shop
launcher space or sho
waist catapult space or shop
elevator machinery space or shop
ic gyro space or shop
ndi space or shop
a/c machinery space or shop
engine test space or shop
""".split("\n")

administration = """
department office
ops space or office
executive officers space
s-8 division office or space
a-division office
office or shop
log room
director space
safety officers space
disbursing space
department space or office
administrative dept space
wpns/ord department space
department office or space
food service office or space
administrative areas
master at arms space
department space or shop
public affairs space
administrative other
general operations space
e-division space or office
supply dept (sd) office or space
central admin
""".split("\n")

walkways_and_passages = """
ladder well
passageway
shaft alley
""".split("\n")

bridge = """
bridge wing
navigation
bridge
signal bridge
bridge/operational areas/ship control
""".split("\n")

power_generation = """
boiler space or shop
emergency diesel space or shop
auxiliary boiler space
motor generator room
engine room
oil analysis lab
engine areas
generator space
nucleonics space or shop
emergency generator space or shop
plenum
cht/boiler space or shop
reactor room
reactor  room
""".split("\n")

flight_deck = """
landing zone
topside
flight deck triage
flight deck
deck other
upper deck(s)
platform
""".split("\n")

communications = """
audio booth
communications space
sses
radar room
switchboard room
radio
ops/comms/ship control other
antenna
switchboard space 
mast
""".split("\n")

global bad_count
bad_count = 1

def strip_words(the_list):
    for i in range(0, len(the_list)-1):
        the_list[i] = the_list[i].strip(" ")
print("hi")
strip_words(waste_disposal)
strip_words(storage)
strip_words(ship_maintenance)
strip_words(ship_operations)
strip_words(material_handling)
strip_words(misc_ship_locations)
strip_words(personnel_support)
strip_words(medical_dental)
strip_words(personnel_quarters)
strip_words(hangar)
strip_words(weapons_and_defense)
strip_words(aircraft_support)
strip_words(administration)
strip_words(walkways_and_passages)
strip_words(bridge)
strip_words(power_generation)
strip_words(flight_deck)
strip_words(communications)

def get_area_category(area):
    if type(area) == type(1.0):
        return "Unknown"
    area = area.lower().strip(" ")
    if area in waste_disposal:
        return "1"
    elif area in storage:
        return "2"
    elif area in ship_maintenance:
        return "3"
    elif area in ship_operations:
        return "4"
    elif area in material_handling:
        return "5"
    elif area in misc_ship_locations:
        return "6"
    elif area in personnel_support:
        return "7"
    elif area in medical_dental:
        return "8"
    elif area in personnel_quarters:
        return "9"
    elif area in hangar:
        return "10"
    elif area in weapons_and_defense:
        return "11"
    elif area in aircraft_support:
        return "12"
    elif area in administration:
        return "13"
    elif area in walkways_and_passages:
        return "14"
    elif area in bridge:
        return "15"
    elif area in power_generation:
        return "16"
    elif area in flight_deck:
        return "17"
    elif area in communications:
        return "18"
    else:
        print(area + " " + str(bad_count))
        return ""

data = pd.read_csv("TrimmedNonAviation.csv")

bad_count = 0

data["AreaCategory"] = data["Area (AREA)"].apply(get_area_category)

data.to_csv("TrimmedNonAviation_exported.csv")


