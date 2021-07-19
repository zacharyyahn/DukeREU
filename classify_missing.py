import pandas as pd
import matplotlib.pyplot as plt

na_data = pd.read_csv("TrimmedNonAviation.csv")
av_data = pd.read_csv("TrimmedAviation.csv")

added_columns = ["Error", "Deck?", "Fault", "High/Low","Event Description","Continue","Human Involved?","anomaly","(Y/S) drop incident due to lack of information for interpretation", "valid?"]
removed_columns = ["PCN_NAME","EVOL","NEC_C","DESG_C", "Problem Columns"]

av_freq_dict = {}
na_freq_dict = {}

def av_add_to_dict(word):
    if word in av_freq_dict:
        av_freq_dict[word] += 1
    else:
        av_freq_dict[word] = 0

def na_add_to_dict(word):
    if word in na_freq_dict:
        na_freq_dict[word] += 1
    else:
        na_freq_dict[word] = 0

for item in na_data.columns:
    if item not in added_columns:
        na_add_to_dict(item)

for item in av_data.columns:
    if item not in added_columns:
        av_add_to_dict(item)



def na_search_for_missing(row):
    #print(row)
    missing = ""
    for i in range(0, len(row)-9):

        if str(row[i]) == "nan" and na_data.columns[i] not in removed_columns and na_data.columns[i] not in added_columns:
            missing += na_data.columns[i] + ", "
            if row["Human Involved?"] == "Yes":
                na_add_to_dict(na_data.columns[i])
    return missing

def av_search_for_missing(row):
    missing = ""
    # print(row[-1])
    # if row[-1] == "Valid ":
    for i in range(0, len(row)-9):
        if str(row[i]) == "nan" and av_data.columns[i] not in removed_columns and av_data.columns[i] not in added_columns:
            missing += av_data.columns[i] + ", "
            if row["Human Involved?"] == "Yes":
                av_add_to_dict(av_data.columns[i])   
    return missing     
    # return missing

def error_type(entry):
    if entry != "":
        return "Missing"
    else:
        return ""



na_data["Problem Columns"] = na_data.apply(na_search_for_missing, axis=1)
av_data["Problem Columns"] = av_data.apply(av_search_for_missing, axis=1)

na_data["ErrorType"] = na_data["Problem Columns"].apply(error_type)
av_data["ErrorType"] = av_data["Problem Columns"].apply(error_type)

na_data.to_csv("TrimmedNonAviation_exported.csv")
av_data.to_csv("TrimmedAviation_exported.csv")

print(av_freq_dict)
# print(na_freq_dict)

av_keys = av_freq_dict.keys()
av_values = av_freq_dict.values()

na_keys = na_freq_dict.keys()
na_values = na_freq_dict.values()

plt.barh(list(na_keys), list(na_values))
plt.yticks(fontsize=6)
plt.title("Number of Missing Entries for Non-Aviation (out of ~7200)")

for index, value in enumerate(na_values):
    if value != 0:
        plt.text(value, index, str(value))

plt.show()
plt.bar(na_keys, na_values)