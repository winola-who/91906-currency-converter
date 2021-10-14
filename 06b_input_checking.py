# checks if something is valid
import re

invalid = "yes"
while invalid == "yes":
    filename = input("Please enter a filename: ")
    invalid = "no"
    valid_char = "[A-Za-z0-9_]"

    for letter in filename:
        # checks if the characters are in the valid range
        if re.match(valid_char, letter):
            continue
        elif letter == " ":
            error_msg = "No spaces allowed"
        else:
            error_msg = "No '{}' is allowed".format(letter)
        invalid = "yes"

    if filename == "":
        error_msg = "Filename cannot be blank"
        invalid = "yes"

    if invalid == "yes":
        print(error_msg)
    else:
        print("Filename {} is valid".format(filename))
