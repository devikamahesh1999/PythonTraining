# Create a program to read a file which contains large set of some noval.
# Get the frequencies of all words in the file and finally show the frequencies
# for each word in a pandas dataframe.

import pandas as pd
import re
from collections import Counter


def filter_words(data):
    """Function to filter out words only."""
    return re.findall(r"\b[\w’-]+\b", data.lower())


def count_words(data):
    """Function to get each word count."""
    return Counter(data)


try:
    with open("novel.txt", "r", encoding="utf8") as file:
        file_content = file.read()
except FileNotFoundError:
    print("'novel.txt' file not found.")

file_content = filter_words(file_content)
word_frequencies = count_words(file_content)

# Final dataframe
print(pd.DataFrame(list(word_frequencies.items()), columns=["Word", "Count"]))
      

