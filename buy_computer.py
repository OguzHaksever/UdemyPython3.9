available_parts = ["computer", "monitor", "keyboard",
                   "mouse", "mouse mat", "hdmi cable", "blue ray drive"]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts)+1):
    valid_choices.append(str(i))
current_choice = "-"
computer_parts = []  # create an empty list
while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_parts = available_parts[index]
        if chosen_parts in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_parts)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_parts)

        print("Your list now contains {}".format(computer_parts))

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
            # for part in available_parts:
            # there is much better way than tihs
            # print("{0}: {1}".format(available_parts.index(part) + 1, part))

    current_choice = input()
print(computer_parts)
# TODO BU YAZILIMI ÇALIŞ

