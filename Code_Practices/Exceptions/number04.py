
# use a while loop to prompt the user for a number, and output that number squared.
# If the user does not input a number, output an error message and prompt them again.

while True:
    try:
         x = int(input("What's x? "))
         break
    except ValueError:
        print("x is not an integer.")


print(f"x is {x}  ")