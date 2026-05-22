
# 4: Using a while loop to prompt the user for a non-negative integer until they provide one
# This code will keep asking the user for input until they provide a non-negative integer.

while True:
    n = int(input("What's n?"))
    if n < 0:
        continue
    else:
        break