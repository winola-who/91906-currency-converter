def value_check():
    error = 1
    error_msg = " "
    while error == 1:
        try:
            value = float(input("Convert value: "))
            if value <= 0:
                error_msg = "Please enter a number that is greater than 0."
                print(error_msg)
            else:
                error = 0
                return value
        except ValueError:
            error_msg = "Please enter a number."
            print(error_msg)


ratio = ""
symbol = ""
convert_from = input("Convert from: ").upper()
convert_to = input("Convert to: ").upper()
convert = value_check()
if convert_from == "USD":
    if convert_to == "RMB":
        ratio = 6.47
        converted = convert * ratio
        symbol = "¥"
        print(symbol, converted)
    elif convert_to == "USD":
        convert_error = "Please choose a different currency to convert to"
        print(convert_error)
