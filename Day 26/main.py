
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]

# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

num_list = [num * 2 for num in range(1, 5)]
print(num_list)

# Conditional List Comprehension

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
