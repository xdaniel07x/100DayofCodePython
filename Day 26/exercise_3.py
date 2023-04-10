
with open("Day 26\.file1.txt") as file1:
    with open("Day 26\.file2.txt") as file2:
        file_1 = file1.read().splitlines()
        file_2 = file2.read().splitlines()
        result = [int(num) for num in file_1 if num in file_2]
# Write your code above 👆

print(result)
