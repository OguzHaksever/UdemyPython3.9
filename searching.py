shopping_list = ["milk", "pasta", "eggs", "bread", "spam", "rice"]

item_to_find = "yumurt"
found_at = None

# for index in range(len(shopping_list)):     # len(shopping_list) means length, will return 6
#     if shopping_list[index] == item_to_find:    # indexing a list
#         found_at = index
#         break
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
