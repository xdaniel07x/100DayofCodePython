# # Read to a file
# with open("Day 24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# a = append
# w = write mode

with open("Day 24/new_file.txt", mode="w") as file:
    file.write("New text.")
