loop = "yes"
while loop == "yes":
    value = float(input("Enter a number: "))

    if value % 1 == 0:
        rounded = value
        print(rounded)
        loop = input("loop? ")
    else:
        rounded = round(value, 2)
        print(rounded)
        loop = input("loop? ")
