# Prompt the user for a number, and output that number squared.
#  If the user does not input a number, output an error message.

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer.")