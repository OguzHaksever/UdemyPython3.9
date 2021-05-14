import random


def get_integer(prompt):
    """
    Gets an integer from Standart Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    Args:
        prompt ([type]): The string that the user wikk see, when
        they're prompted to enter the value.

    Returns:
        [type]: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:    Not necessary as if if is true, return will
        # terminate the loop and won't run the print function
        print("This is not a valid choice")


highest = 10
answer = random.randint(1, highest)
# print(answer)           # TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = get_integer(": ")
guesses = 1

while guess != answer:
    if guess < answer:
        print("Please guess higher")
        guess = get_integer(": ")
        guesses += 1
    elif guess > answer:
        print("Please guess lower")
        guess = get_integer(": ")
        guesses += 1
while guess == answer:
    if guesses == 1:
        print("you got it right the first time, CONGRATULATIONS")
        break
    else:
        print("You got it right \nYou have guessed {} times.".format(guesses))
        break
