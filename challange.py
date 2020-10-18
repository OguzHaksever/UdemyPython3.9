name = input("What is your name ?")
age = int(input("Please enter your age {}".format(name)))

if 18 <= age <= 30:
    print("You are allowed to go {}".format(name))
else:
    print("{}, you must be between 18 and 30 to be allowed, sorry.".format(name))
