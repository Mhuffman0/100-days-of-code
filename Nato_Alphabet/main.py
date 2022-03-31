import pandas

with open("nato_phonetic_alphabet.csv") as file:
    nato_df = pandas.read_csv(file)
    nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
    nato_dict[" "] = ""

for letter in input("What would you like to spell out?\n").upper():
    print(nato_dict[letter])
