import pandas
import random

# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]

# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# num_list = [num * 2 for num in range(1, 5)]
# print(num_list)

# List Comprehension

# [new_list for letter in word]

# Conditional List Comprehension

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)

# Looping through dictionaries

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
# Dictionary Comprehension

# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: value for (
    student, value) in student_scores.items() if value >= 60}
print(passed_students)
