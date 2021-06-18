import pandas as pd
import re

the_col = "Event Description"

lookup = {
    "Destruction":["crashed", "crash", "collided"],
    "Fire":["fire", "fires"],
    "Laceration":["laceration", "cut", "lacerated", "cutting"],
    "Electrical shock":["electrical", "shock", "shocked"],
    "Tendon/ligament/muscle":["ankle", "fell", "ankles", "disclocated", "twisted", "strain", "strained", "dislocated", "dislocation"],
    "Optical Damage":["eye", "eyes", "eyelid", "eyelids", "shin", "shins"],
    "Skeletal Injury":["broke", "fractured", "broken", "fracture"], 
    "Crushed Appendage":["pinched", "jammed", "crushed", "crushing", "caught", "slammed", "dropped", "smashed"], 
    "Burn":["burn", "burns", "burned"], 
    "Head Blow":["face", "head", "concussion", "concussed", "slipped", "tripped"], 
    "Appendage Blow":["contusion", "tissue"],
    "Other Health":[],
    "Human Damage":[],
}

injuries = ["laceration", "tendon/ligament/muscle", "optical damage", "skeletal injury", "crushed appendage", 
"burn", "head blow", "appendage blow", "human damage"]

def lookup_word(word):
    found_one = False
    the_word = ""
    for key in lookup:
        if word in lookup[key] and not found_one:
            found_one = True
            the_word = key
        elif word in lookup[key] and found_one:
            the_word = "MANUAL_ENTRY"
            break
    return the_word

def word_parser(text):
    text = text.lower()
    word_list = re.findall(r"[\w']+", text)
    for word in word_list:
        the_word = lookup_word(word.lower())
        if the_word != "":
            return the_word

def injury_classifier(row):
    fatality = row["Injury Classification"]
    if type(fatality) == type("string"):
        fatality = fatality.lower()
        if "fatal" in re.findall(r"[\w']+", fatality):
            return "Death"
        elif fatality == "no injury or illness":
            return ""
    description = row["EventDescr"]
    if type(description) == type("string"):
        description = description.lower()
        if description in injuries:
            return "Injury"
    return ""

data = pd.read_csv("Combined.csv")
pd.set_option('display.max_row',1000)

#data["DescWord"] = data["Event Description"].apply(word_parser)
data["InjClass"] = data.apply(injury_classifier, axis=1)

data.to_csv("exported_combined.csv")


    
