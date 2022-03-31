import csv

with open("nato_phonetic_alphabet.csv") as file:
    reader = csv.reader(file)
    next(reader)
    nato_dict = {letter: code for (letter, code) in reader}
    nato_dict[" "] = ""

for letter in input("What would you like to spell out?\n"):
    print(nato_dict[letter.upper()])
