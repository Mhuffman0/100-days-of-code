# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
with open('nato_phonetic_alphabet.csv') as file:
    nato_dict = dict(file.read())
print(nato_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
