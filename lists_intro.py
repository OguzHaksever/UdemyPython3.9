parts = ["computer",
         "monitor",
         "keyboard",
         "mouse",
         "mat"
         ]
#
# for part in parts:
#     print(part)
#
# print(parts[3])
#
# print(parts[0:4])     # lists first four items
# print(parts[-2])

print(parts)
parts[3] = "trackball"
print(parts)
parts[0:3] = parts
print(parts)