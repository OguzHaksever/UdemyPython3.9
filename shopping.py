shopping_list = ["milk", "pasta", "eggs", "bread", "spam", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue        # causes everything else in the loop to be skipped

    print("Buy " + item)
