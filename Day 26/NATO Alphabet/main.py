import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv(
    "Day 26/NATO Alphabet/nato_phonetic_alphabet.csv")
nato_data_frame = pandas.DataFrame(data)

nato_dict = {row.letter: row.code for (
    index, row) in nato_data_frame.iterrows()}

# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = list(input("Enter a word: ").upper())

n_list = [row.code for i in user_input for (
    index, row) in nato_data_frame.iterrows() if i == row.letter]

print(n_list)


# Alt solution
word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)
