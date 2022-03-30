with open("file1.txt") as file:
    file1 = file.read().splitlines()

with open("file2.txt") as file:
    file2 = file.read().splitlines()

result = [int(num) for num in file1 if num in file2]
# Write your code above 👆

print(result)
