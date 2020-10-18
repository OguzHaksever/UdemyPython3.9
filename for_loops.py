number = input("Please enter a series of numbers, using any seperators you like: ")
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
