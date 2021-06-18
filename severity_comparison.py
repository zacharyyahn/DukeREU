import pandas as pd

av_data = pd.read_csv("Aviation.csv")
na_data = pd.read_csv("Non Aviation.csv")

av_sev_code = av_data["EVENT_SEVTY_C"]
av_event_class = av_data["EVENT_CLASSN_C"]

total = 0
data_amount = 0
num_floats = 0
different = 0
for i in range(len(av_sev_code)):
    try:
        if av_sev_code[i] == av_event_class[i][1]:
            total+=1
        else:
            #print(str(av_sev_code[i]) + ", " + str(av_event_class[i]))
            different += 1
    except:
        #print(av_sev_code[i], av_event_class[i])
        num_floats += 1

    data_amount += 1

print("Same: " + str(total))
print("Different: " + str(different) + " (note that most of these are because there are pure numbers)")
print("Errors: " + str(num_floats))
print("Amount of Entries: " + str(data_amount))
