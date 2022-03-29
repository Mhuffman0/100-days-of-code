with open("input/names/invited_names.txt", "r") as file:
    names_list = file.read().splitlines()
    print(names_list)

with open("input/letters/starting_letter.txt", "r") as file:
    letter = file.read()

for name in names_list:
    print(name)
    with open(
        f"Output/ReadyToSend/letter_{name.replace(' ', '_').lower()}.txt", "w"
    ) as file:
        file.write(letter.replace("[name]", name))
