import random

highest = 10
answer = random.randint(1, highest)
# print(answer)           # TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
guesses = 1

while guess != answer:
    if guess < answer:
        print("Please guess higher")
        guess = int(input())
        guesses += 1
    elif guess > answer:
        print("Please guess lower")
        guess = int(input())
        guesses += 1
while guess == answer:
    if guesses == 1:
        print("you got it right the first time, CONGRATULATIONS")
        break
    else:
        print("You got it right \nYou have guessed {} times.".format(guesses))
        break