parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print()
# Slicing a String
print("Slicing a String")
print()

print(parrot[0:6])  # Norweg, does not  include the 6th index
print(parrot[3:5])
print()
print(parrot[:9])   # from the start up to 9th
print()
print(parrot[10:14])
print(parrot[10:])   # from the 10th index until the end
print()
print(parrot[:6] + parrot[6:])
print(parrot[:])

# Step Slicing
print(parrot[0:6:2])
print(parrot[0:6:3])
