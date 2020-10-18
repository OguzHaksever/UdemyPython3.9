# print a number of option, user will select, display options, continue
# to loop until user chooses 0, if valid choice, print a short message
# message = value they typed, invalid, display the menu agai

the_list = ["1. Learn Python", "2. Learn Java", "3. Go swimming",
            "4. Have dinner", "5. Got to bed", "6. Play games",
            "0. Exit"]

choice = ""

while choice != "0":
    print("Please choose an option down below: ")
    for i in range(len(the_list)):
        print(the_list[i])
    choice = input()
    if choice in "123456":  # ["1", "2", "3", "4", "5", "6"]
        print("You choose {}".format(choice))
    elif choice == "0":
        print("You have exited the program")
        break
