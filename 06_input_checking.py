error = 1
error_msg = " "
while error == 1:
    try:
        value = float(input("Enter a value: "))
        if value < 0:
            error_msg = "Please enter a number that is greater than 0."
            print(error_msg)
        else:
            print(value)
            error = 0
    except ValueError:
        error_msg = "Please enter a number."
        print(error_msg)
