import pandas as pd
import matplotlib

data = pd.read_csv("Non Aviation.csv")
av_data = pd.read_csv("Aviation.csv")
pd.set_option('display.max_rows', 50)

print("----NON-AVIATION----")
print(data["RPRTG_UNIT_CODE"].value_counts())

print("\n\n")
print("----AVIATION----")
print(av_data["RPRTG_UIC"].value_counts())