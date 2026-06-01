
# use a while loop to prompt the user for a number, and output that number squared.
# If the user does not input a number, output an error message and prompt them again.

# making code dynamic by using a function to get an integer from the user, and output that number squared.
# prompt the user for a number, and output that number squared.
# If the user does not input a number, output an error message and prompt them again.

def main():
    x = GET_INT("What's x? ")
    print(f"x is {x}  ")




def GET_INT(promt):
    while True:
        try:
             return int(input(promt))
        except ValueError:
            pass

main()