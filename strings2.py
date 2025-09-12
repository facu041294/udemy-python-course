#
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian
print(parrot[:9])   # Norwegian
print(parrot[10:14])# Blue
print(parrot[10:])  # Blue
print(parrot[:])    # Norwegian Blue
print(parrot[:6] + parrot[6:])  # Norwegian Blue

print()

print(parrot[-4:-2]) # Bl
print(parrot[-4:12]) # Bl

print()

print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

number = "9,223,372,036,854,775,807" 
print(number[1::4])  # ,,,,,, 
seperators = number[1::4]
print(seperators)     # ,,,,,,

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])  # [9, 223, 372, 36, 854, 775, 807]

print()

print(parrot)
# indexing
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
# negative indexing
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
# arithmetic operators with indexing
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])