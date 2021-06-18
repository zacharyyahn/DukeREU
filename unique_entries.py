import pandas as pd

pd.set_option('display.max_row',1000)

data = pd.read_csv("Aviation.csv")

f = open("aviation-unique.txt", "w")

for col in data.columns:
    unique_list = data[col].unique()
    try:
        unique_list.sort()
    except:
        pass

    f.write("\n\n---------" + col.upper() + "---------\n")

    the_list = ""
    for item in unique_list:
        try: 
            item = int(item)
        except:
            pass
        the_list += str(item) + ", "
    f.write(the_list)

f.close()

 
