parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("I don't need that letter")

print("-" * 60)

activity = input("What would you like to do today")
if "cinema" not in activity.casefold():             # for both lower and upper character check
    print("But I want to go to the cinema")
