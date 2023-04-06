# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Day 24 - Extended/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    num = names.readlines()
    length = len(num)

    for i in range(length):
        with open("Day 24 - Extended/Mail Merge Project Start/Input/Letters/starting_letter.txt") as names:
            read = names.readlines()
            list = "".join(read)
            new_name = num[i].strip("\n")
            new_letter = list.replace("[name]", f"{new_name}")
            with open(f"Day 24 - Extended/Mail Merge Project Start/Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as new_file:
                new_file.write(f"{new_letter}")
