'''
for _ in range(3):
    print("#") '''

def main():
    print_coloum(3)

def print_coloum(height):
    # print("#\n" * height ,end="")
    for _ in range(height):
        print("#")

main()