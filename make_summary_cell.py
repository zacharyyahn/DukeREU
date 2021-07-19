import pandas as pd

av_data = pd.read_csv("TrimmedAviationFinal.csv")
na_data = pd.read_csv("TrimmedNonAviation.csv")

def av_make_summary_cell(row):
    current_string = ""
    for column in av_data.columns[:-11]:
        current_string += column + ": " + str(row[column]) + "; "
    return current_string

def na_make_summary_cell(row):
    current_string = ""
    for column in na_data.columns[:-8]:
        current_string += column + ": " + str(row[column]) + "; "
    return current_string

av_data["Summary"] = av_data.apply(av_make_summary_cell, axis=1)
na_data["Summary"] = na_data.apply(na_make_summary_cell, axis=1)

av_data.to_csv("TrimmedAviationFinal_exported.csv")
na_data.to_csv("TrimmedNonAviation_exported.csv")