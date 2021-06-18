import pandas as pd
import re

data = pd.read_csv("Combined.csv")

the_col = "Event Description"
throw_away_words = ["the", "a", "of", "on", "and", "to", "in", "while"]

massive_string = ""
for item in data[the_col]:
    massive_string += item

massive_string = massive_string.lower()
all_words_list = re.findall(r"[\w']+", massive_string)

word_freq_dict = {}
for word in all_words_list:
    if word not in throw_away_words:
        if word in word_freq_dict:
            word_freq_dict[word] += 1
        else:
            word_freq_dict[word] = 1

sorted_dict = {k: v for k, v in sorted(word_freq_dict.items(), key=lambda item: item[1])}

print(sorted_dict)

