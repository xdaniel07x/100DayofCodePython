import random

# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]

# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# num_list = [num * 2 for num in range(1, 5)]
# print(num_list)

# Conditional List Comprehension

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)

# Dictionary Comprehension

# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: value for (
    student, value) in student_scores.items() if value >= 60}
print(passed_students)
