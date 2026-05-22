
def main():
    print_Square(3)

def print_Square(size):

    # for each row in the square
    for i in range(size):
        
        # for each block in the row
        for j in range(size):

            # print a block without moving to the next line
            print("#", end="")
        print()

main()