# for sorting iterable object, strings and lists
pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)

numbers = [1.2,3.4,5.6,7.8,9.0,3.6]
sorted_numbers = sorted(numbers)   #does not alter the list
print(sorted_numbers)
print(numbers)

numbers.sort()  # changes the list, funtcion sort doesn't return anything
# cant assign the result to a variable
print(numbers)

missing_letter = sorted("The quick brown fox jumps over the lazy dog",
                        key=str.casefold)
# case insensitive sorting

print(missing_letter)

names = ["Graham", "John", "terry", "eric", "Terry", "michael"]
names.sort(key=str.casefold)
print(names)
