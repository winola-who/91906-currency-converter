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
    if len(all_conversions) >= 5:
        # The most recent 5
        for item in range(0, 5):
            print(all_conversions[len(all_conversions) - item - 1])
    else:
        for item in all_conversions:
            print(all_conversions[len(all_conversions) - all_conversions.index(item)])
