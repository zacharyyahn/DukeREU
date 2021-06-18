import pandas as pd 
import re

data = pd.read_csv("Aviation.csv")

deck_keyword_list = ["HANDLING AREA", "QUARTERDECK", "MAST", "ANTENNA", "BROW", "FLIGHT DECK", 
"FLIGHT DECK TRIAGE", "MAIN DECK", "PATHWAY/SIDEWALK"]
no_deck_keyword = "A/C MACHINERY SPACE OR SHOP, TRASH PULPER ROOM, UTILITY STOREROOM, CLEANING GEAR SPACE OR SHOP, PREVENTIVE DENTISTRY, EJECTION SEAT SPACE OR SHOP, DEPARTMENT OFFICE, CLUB, COMMERCIAL BUILDING OTHER, MOUNT, HULL REPAIR SPACE OR SHOP, BRIDGE WING, EMERGENCY DIESEL SPACE OR SHOP, AUDIO BOOTH, ELEVATOR MACHINERY SPACE, OPS SPACE OR OFFICE, GARBAGE DISPOSAL SPACE, STERILIZING ROOM, LAUNCH ACCESS SPACE OR SHOP, ACID BATTERY SPACE OR SHOP, TOOL ISSUE SPACE OR SHOP, CREW BARBER, WEAPONS/ORDNANCE OTHER, METALSMITH SPACE OR SHOP, CHIEFS/CPO MESS, AREA (FUNCTIONAL PHYSICAL SPACE OR SHOPS) OTHER, TEST LAB, AUXILIARY BOILER SPACE, OXIDIZER SPACE OR SHOP, FILTER CLEANING SPACE OR SHOP, RAM, REWIND SHOP, MECHANICAL CALIBRATION FACILITY, METAL & PIPE SPACE OR SHOP, DISPLAY REPAIR SPACE OR SHOP, CPO/NCO SCULLERY, HOME/RESIDENCE AREA OTHER, REFRIGERATION MACHINERY ROOM, TROOP BERTHING, ELECTRICAL TOOL SPACE OR SHOP, READY ROOM, NIXIE EQUIPMENT SPACE OR SHOP, LIBRARY, ENGINEERING/AUX/REPAIR, SHOWER & WATER CLOSET, CHIEFS/CPO BERTHING, R-DIVISION SPACE, OFFICE OR SHOP, DIESEL SPACE OR SHOP, ESCAPE TRUNK, GUN SPACE OR SHOP, ARMORY SPACE OR SHOP, FUELING SPACE OR SHOP, FOOTBALL FIELD, VALVE SPACE OR SHOP, PARALOFT, BARRACKS, JP-5 FILTER SPACE, LIGHTING SPACE OR SHOP, AC&R MACHINERY SPACE OR SHOP, ENGINEERING/AUX/REPAIR OTHER, EXECUTIVE OFFICERS SPACE, COMMUNICATIONS SPACE, OPERATIONAL/INDUSTRIAL BUILDING/PLANT OTHER, MEDICAL/DENTAL OTHER, PORTABLE TOOL SHOP OR AREA, S-8 DIVISION OFFICE OR SPACE, FAN, COMPUTER SPACE OR SHOP, SOCKET POURING SPACE OR SHOP, CHT/BOILER SPACE OR SHOP, A-DIVISION OFFICE, SPACE OR SHOP, STEERING GEAR ROOM, DIESEL GENERATOR SPACE OR SHOP, MEDICAL RECORDS ROOM, MINOR OPERATING ROOM, JP5 PUMP SPACE, TIRE AND WHEEL SPACE OR SHOP, DECON SPACE OR STATION, POOL, COMPOSITE SPACE OR SHOP, ELECTRICAL REWIND SPACE OR SHOP, OBSTACLE COURSE, GENERAL WORKSHOP, FAN ROOM, HT  SPACE, OFFICE OR SHOP, RECREATIONAL AREA OTHER, VOID, TRASH ROOM, INCINERATOR, FUEL TEST SPACE OR SHOP, CRASH & SALVAGE AVIATION FUEL REPAIR SPACE OR SHOP, WARDROOM PANTRY, LAUNDRY ISSUE, EXAM ROOM, HULL/UNDERWATER/TANKS/VOIDS OTHER, JET ENGINE SPACE OR SHOP, NUCLEONICS SPACE OR SHOP, CRANE SPACE OR SHOP, JP-5 FILTER SPACE OR SHOP, WEAPONS FORKLIFT, SAIL LOFT, COMPRESSOR SPACE OR SHOP, PERSONNEL LANDING, WARD, PLOTTING ROOM, MAINTENANCE AREA, NAVIGATION, BRIG, UTILITY SPACE OR SHOP, REFRIGERATION MACHINERY  SPACE OR SHOP, FIRST LIEUTENANTS SPACE OR SHOP, CLASSIFIED DOCUMENT DESTRUCTION SPACE, RAM SPACE OR SHOP, REFUELING PITS, SHOP - ORDNANCE, ISSUE ROOM, CONVEYOR, RAST MACHINERY ROOM, LOG ROOM, NON-GOVT SMALL/SERVICE CRAFT - UNKNOWN/OTHER, BRIDGE, FACILITY/SCHOOL, AUXILIARY MACHINERY ROOM (AMR OR AUX), CIWS NR2/AVIATION SPACE, HEAD, HANGAR BAY, AIR DEPARTMENT SPACE, FUEL/OIL SPACE OR SHOP, BERTHING AREA, NON-GOVT SHIP - OTHER, HOSE AND TUBE SPACE OR SHOP, SMALL BOAT, PEDESTRIAN CROSSING, LEARNING RESOURCE CENTER, TRANSPORTS OTHER, HIKING/JOGGING PATH, LANDING ZONE, DIRECTOR SPACE, STORAGE BATTERY SPACE OR SHOP, KINGPOST, TANK, CHEM OR CBR WARFARE DEFENSE SPACE, RAS WINCH SPACE OR SHOP, FLAMMABLE CARGO, BREAD ROOM, OFFICE BUILDING OTHER, FORKLIFT SPACE OR SHOP, MOTOR GENERATOR ROOM, CORROSION CONTROL SPACE OR SHOP, PORT BOW, MEDICAL/CREW MESS ROOM, CABIN, DENTAL X-RAY, CO2 CYLINDER SPACE OR SHOP, FLAG OFFICER GALLEY, UTILITY ROOM, INPATIENT AREA, SAFETY OFFICERS SPACE, CHAIN LOCKER, HELO REPAIR SPACE OR SHOP, VERTICAL PACKAGE CONVEYOR, STRUCTURES SPACE OR SHOP, ELEVATOR SPACE OR SHOP, ENLISTED QUARTERS, CONFERENCE ROOM, RADAR ROOM, AIR, GOVERNMENT, MEDICAL DEPARTMENT OFFICE OR ADMIN, BARRICADE SPACE OR SHOP, HYDRAULIC PNEUMATIC SPACE OR SHOP, GUNNERY SPACE OR SHOP, FORKLIFT SPACE, CO2 CYLINDER STOREROOM, CHAPLAIN SPACE, EQUIPMENT SPACE OR STOREROOM, OIL PUMP SPACE, HOLD, NON-GOVT SHIP - UNKNOWN, MAIN STOREROOM, CIWS NR2/AVIATION SPACE OR SHOP, DISBURSING SPACE, WASHROOM, CAPSTAN MACHINERY SPACE OR SHOP, STATEROOM, LADDER WELL, YARD, OBOGS SPACE OR SHOP, ELEVATOR MACHINERY SPACE OR SHOP, GALLEY, DEPARTMENT SPACE OR OFFICE, CARGO HOLD, M-DIVISION SPACE, OFFICE OR SHOP, ENGINE ROOM, OIL ANALYSIS LAB, TOPSIDE, PIER, FIRST CLASS MESS, ELECTRONIC REPAIR SPACE OR SHOP, GEAR SPACE OR SHOP, INDUSTRIAL FACILITIES OTHER, HOUSE, UNREP/RAS SPACE OR SHOP, AVIONICS SPACE OR SHOP, GARAGE, GENERAL SPACE OR SHOP, GYM, INCINERATOR ROOM, ADMINISTRATIVE DEPT SPACE, WPNS/ORD DEPARTMENT SPACE, V2 MAINT SUPPORT/TOOL SPACE OR SHOP, REACTOR  ROOM, AIRFRAMES SPACE OR SHOP, GROUND SUPPORT EQUIPMENT (GSE) SPACE OR SHOP, BOILER SPACE OR SHOP, WARDROOM MESS, DEPARTMENT OFFICE OR SPACE, BARGE, GENERAL HABITABILITY SPACE, WARDROOM GALLEY, CREW SHELTER, PHOTO LAB, CENTRAL ADMIN SPACE OR SHOP, WARDROOM SCULLERY, BOAT SPACE OR SHOP, PHYSICAL FITNESS ROOM, SCULLERY, FUELING SPACE, EMERGENCY GENERATOR SPACE OR SHOP, HANDLING SPACE OR SHOP, CREW LAUNDRY, HANGAR DECK, AIRCRAFT ELEVATOR MACHINERY SPACE OR SHOP, HOLDS/SUPPLY AREAS, AIRCRAFT ELEVATOR SPACE OR SHOP, HYDRAULICS SPACE OR SHOP, MAGAZINE, FANTAIL, MESS DECK, ENGINE AREAS, FOOD SERVICE OFFICE OR SPACE, ADMINISTRATIVE AREAS, AVIATION/AIR/AIMD OTHER SPACE OR SHOP, CATAPULT SPACE OR SHOP, BOATSWAINS SPACE OR SHOP, SUPPORT FACILITY OTHER, TRASH DISPOSAL OPERATION, VEHICLE SPACE, PASSAGEWAY, PAINT MIXING & ISSUE, ORDNANCE SPACE OR SHOP, BILGE, ELEVATOR SPACE, ARRESTING GEAR MACHINERY SPACE OR SHOP, CALIBRATION SPACE OR SHOP, SUPPLY/STORES/CARGO OTHER, SHOWER, MAIN MEDICAL AREA, CREW MESS, VEG PREP ROOM, CREW SPACE OR SHOP, NDI SPACE OR SHOP, CARPENTER SPACE OR SHOP, CREW BERTHING, FUELS REPAIR SPACE OR SHOP, SWITCHBOARD ROOM, DECK OTHER, LOUNGE, JP5 PUMP ROOM, SHAFT ALLEY, MAIN MACHINERY ROOM (MMR), LAUNCHER SPACE OR SHOP, JET SHOP SPACE OR SHOP, RECREATION AREA OR SPACE, CHT PUMP ROOM OR SPACE, BAKERY, HAZMAT REUSE, SHIPS SERVICE STOREROOM, DENTAL STOWAGE, BOOM, SIGNAL BRIDGE, PULPER/SHREDDER ROOM, WAIST CATAPULT SPACE OR SHOP, HAZMINCEN, BATTLE DRESSING STATION, IC GYRO SPACE OR SHOP, HOIST SPACE OR SHOP, X-DIVISION SPACE, DEPARTMENT SPACE OR SHOP, PIPE SPACE OR SHOP, MACHINERY ROOM (MER), CLEANING GEAR SPACE, ET SPACE OR SHOP, PAINT STOREROOM, RADIO, MASTER AT ARMS SPACE, COMBAT INFORMATION CENTER (CIC), CANVAS SPACE OR SHOP, OPS/COMMS/SHIP CONTROL OTHER, GEAR LOCKER, REPAIR SPACE, OFFICE OR SHOP, ARMORY, ENGINEERING LOG ROOM, UPPER DECK(S), ORDNANCE/GUN SYSTEM SPACE OR SHOP, SWITCHBOARD SPACE, BATTERY SPACE OR SHOP, ATHLETIC FIELD, CONTROL SPACE, OTHER ELEVATED AREA, EQUIPMENT SPACE OR SHOP, PIPE AND DC SPACE OR SHOP, PLASTIC WASTE PROCESSOR ROOM, GENERAL MEDICAL SPACE OR AREA, REPAIR SPACE OR SHOP, MACHINE SPACE OR SHOP, METALSMITH & MACHINE SPACE OR SHOP, PUBLIC AFFAIRS SPACE, SUPPLY DEPT (SD) OFFICE OR SPACE, LAUNDRY PRESS, CHIEFS MESS, CONCRETE/ASPHALT PLANT, VESTIBULE, ELECTRICAL/DAMAGE CONTROL SPACE OR SHOP, ELECTRICAL SPACE OR SHOP, ANCHOR WINDLASS SPACE, SURVIVAL EQUIPMENT SPACE OR SHOP, BASKETBALL COURT, ADMINISTRATIVE OTHER, CREW SPACE - OTHER, WATER CLOSET, TRAINING SPACE, EQUIPMENT SPACE, CANVAS & BUNTING SPACE OR SHOP, GENERAL WORKSHOP OR SPACE, EQUIPMENT STOREROOM, ENGINE TEST SPACE OR SHOP, ELECTRICAL SERVICE SPACE OR SHOP, CLEANING GEAR ISSUE OR LOCKER, BLOOD BANK, UTILITY SPACE, CREW SCULLERY, PUMP ROOM, GUN SUPPORT SPACE OR SHOP, CVIC, MOTOR POOL/GARAGE, GENERAL OPERATIONS SPACE, BRIDGE/OPERATIONAL AREAS/SHIP CONTROL, GENERATOR SPACE, HABITABILITY OTHER, WARDROOM, CPO/NCO GALLEY, MEDICAL TREATMENT ROOM, MACHINE & WELD SPACE OR SHOP, SHIPS STORE/MINI-MART, LAUNDRY, WINCH/CRANE SPACE, AIRCRAFT FUELING SPACE OR SHOP, ELEVATOR, HANGAR, WEAPONS DEPT OFFICE OR SPACE, FORECASTLE, E-DIVISION SPACE OR OFFICE, TOWED ARRAY SPACE OR SHOP, GENERAL STOREROOM, CENTRAL ADMIN, TENNIS COURT" 
no_deck_keyword_list = no_deck_keyword.split(", ")

other_keyword_list = ["DECK", "FLIGHT"]
aviation_keyword_list = ["deck", "runway", "catapult", "touchdown", "landing"]

print(data.columns)

def find_deck_non_aviation(row):
    try:
        area = row["AREA"].upper()
        print(area)
    except:
        return ""

    if area in deck_keyword_list:
        print("Yes")
        return "Yes"
    elif area in no_deck_keyword_list:
        print("No")
        return "No"
    else:
        narr = row["BRIEF_NARR"].lower()
        word_list = re.findall(r"[\w']+", narr)
        for word in word_list:
            if word in other_keyword_list:
                print("Yes")
                return "Yes"

def find_deck_aviation(row):
    try:
        desc = row["INCDT_TYPE"].lower()
    except:
        return ""
    word_list = re.findall(r"[\w']+", desc)
    for word in word_list:
        if word in aviation_keyword_list:
            return "Yes"
    return ""
    
data["Deck?"] = data.apply(find_deck_aviation, axis=1)
data.to_csv("deck_aviation.csv")