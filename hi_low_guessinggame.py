low = 1
high = 1000

print("Please think of a number between {0} and {1}".format(low, high))
input("Press ENTER to start")

guess_count: int = 1
while low != high:
    guess = low + (high - low) // 2  # calculates the mid point between low and high points to generate the next guess

    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h, l, or c if my guess was correct".format(guess)).casefold()

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes 1 less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guess_count))
        break

    else:
        print("Please enter h, l or c")

    guess_count += 1
else:
    print("You though of the number {}".format(low))
    print("I got it in {} guesses".format(guess_count))