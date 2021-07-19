import pandas as pd

av_data = pd.read_csv("TrimmedNonAviation.csv")

def get_month(time):
    first_slash_loc = time.find("/")
    return time[0:first_slash_loc]

def get_day(time):
    first_slash_loc = time.find("/")
    time = time[first_slash_loc+1:]
    second_slash_loc = time.find("/")
    return time[:second_slash_loc]

def get_year(time):
    first_slash_loc = time.find("/")
    time = time[first_slash_loc+1:]
    second_slash_loc = time.find("/")
    time = time[second_slash_loc+1:]
    return time[0:4]

print(get_day("12/24/2001"))
print(get_month("12/24/2001"))
print(get_year("12/24/2001 12:00:00AM"))

av_data["Year"] = av_data["Date and Time (EVENT_DATE_TIME)"].apply(get_year)
av_data["Month"] = av_data["Date and Time (EVENT_DATE_TIME)"].apply(get_month)
av_data["Day"] = av_data["Date and Time (EVENT_DATE_TIME)"].apply(get_day)

av_data.to_csv("TrimmedNonAviation_exported.csv")

