import pandas as pd

av_data = pd.read_csv("Aviation.csv")
na_data = pd.read_csv("Non Aviation.csv")

non_human_incidents = ["weather damage", "machine damage", "destruction", "fire", "impact, machine"]

def human_involved(text):
    try:
        text = text.lower()
        if text in non_human_incidents:
            return "No"
        else:
            return "Yes"
    except:
        return "ERROR"

av_data["Human Involved?"] = av_data["Event Description"].apply(human_involved)
na_data["Human Involved?"] = na_data["Event Description"].apply(human_involved)

av_data.to_csv("exported_aviation.csv")
na_data.to_csv("exported_non_aviation.csv")
