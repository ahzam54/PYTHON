
# using a function to get an integer from the user, and output that number squared.
# usind pass to ignore the error message and prompt the user again.
# use a while loop to prompt the user for a number, and output that number squared.
# If the user does not input a number, output an error message and prompt them again.


def main():
    x = GET_INT()
    print(f"x is {x}  ")




def GET_INT():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

main()