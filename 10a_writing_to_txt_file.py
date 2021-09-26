# checks if something is valid
import re


def validate():
    valid_char = "[A-Za-z0-9_]"
    invalid = "yes"
    while invalid == "yes":
        invalid = "no"
        name = input("Please enter a filename: ")
        # checks each character from the input
        for letter in name:
            if re.match(valid_char, letter):
                continue
            # checks for spaces
            elif letter == " ":
                error_msg = "No spaces allowed"
                invalid = "yes"
            # checks for invalid characters
            else:
                error_msg = "No '{}' is allowed".format(letter)
                invalid = "yes"

        # when there is no input
        if name == "":
            error_msg = "Filename cannot be blank"
            invalid = "yes"

        # prints error if the input is invalid
        if invalid == "yes":
            print(error_msg)
        else:
            return name


conv_hist = ["NZD $4.0 to RMB ¥18.2", "RMB ¥4.0 to USD $0.6", "RMB ¥4.0 to USD $0.6"]

filename = validate()

# add .txt suffix
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at end of each item
for item in conv_hist:
    f.write(item + "\n")

# close file
f.close()

