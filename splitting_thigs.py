panagram = """The quick brown
fox jumps\tover
the lazy dog"""
words = panagram.split()  # returns a list
print(words)

numbers = "9,332,372,036,854,775,807"
number_list = numbers.split(",")
print(number_list)

for item in range(len(number_list)):
    number_list[item] = int(number_list[item])

print(numbers)

integer_values = []
for value in number_list:
    integer_values.append(int(value))

print(integer_values)

