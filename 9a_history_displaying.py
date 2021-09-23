# list for storing history

all_conversions = []

# get items from input
conversion = ""
while conversion != "no":
    conversion = input("Enter an item: ")
    if conversion == "no":
        break
    all_conversions.append(conversion)

if len(all_conversions) == 0:
    print("No conversion history")
else:
    all_conversions.reverse()
    if len(all_conversions) >= 5:
        print("most recent 5")
        # The most recent 5
        print(*all_conversions[:5], sep="\n")
    else:
        print(*all_conversions, sep="\n")
