
# 5: Using functions to organize code and avoid repetition

def main():
    number = get_number()
    meow(number)

# This function prompts the user for a non-negative integer and keeps asking until they provide one.

def get_number():
    while True:
        n = int(input("What's n?"))
        if n >= 0:
            break
    return n

# This function takes a number n and prints "meow" n times.

def meow(n):
    for _ in range(n):
        print("meow")

# Call the main function to execute the program.

main()