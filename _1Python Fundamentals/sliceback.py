          #012345678901234567890123456
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1]
print(backwards)  # zyxwvutsrqponmlkjihgfedcb

# Create a slice that produces the characters qpo
qpo = letters[16:13:-1]

# Slice the string to produce edcba
edcba = letters[4::-1]

# Slice the string to produce the last 8 characters, in reverse order
lastEight = letters[25:17:-1]
print(lastEight)  # zyxwvuts

print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])