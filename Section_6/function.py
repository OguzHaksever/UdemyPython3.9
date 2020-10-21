def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    return string.casefold() == string[::-1].casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return string[::-1].casefold() == string.casefold()


sentence = input("Please enter a sentence to check: ")
if palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a planidrome".format(sentence))
