
# 4: Using a while loop to prompt the user for a non-negative integer until they provide one

n = int(input("What's n?"))
if n < 0:
    n = int(input("What's n?"))
    if n < 0:
        n = int(input("What's n?"))
        if n < 0:
            print("n must be non-negative.")
            exit(1)