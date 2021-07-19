import pandas as pd

av_data = pd.read_csv("TrimmedAviation.csv")
na_data = pd.read_csv("TrimmedNonAviation.csv")

def get_month(time):
    first_slash_loc = time.find("/")
    return time[0:first_slash_loc]

def get_day(time):
    first_slash_loc = time.find("/")
    time = [(first_slash_loc+1):-1]
    second_slash_loc = time.find("/")
    return time[:second_slash_loc]

def get_year(time):
    first_slash_loc = time.find("/")
    time = [first_slash_loc+1:-1]
    second_slash_loc = time.find("/")
    time = [second_slash_loc+1:-1]
    return time

print(get_day("12/24/2001"))
print(get_month("12/24/2001"))
print(get_year("12/24/2001"))

