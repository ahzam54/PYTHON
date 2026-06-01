


# use a while loop to prompt the user for a number, and output that number squared.
# If the user does not input a number, output an error message and prompt them again.


def main():
    x = GET_INT()
    print(f"x is {x}  ")




def GET_INT():
    while True:
        try:
             x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer.")
        else:
            return x

main()