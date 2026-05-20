# Using conditionals to determine if a number is even or odd --- IGNORE ---
# This version of the code is more concise. The is_even function returns the result of the expression n % 2 == 0 directly, which is a boolean value (True or False). This eliminates the need for an if-else statement, making the code cleaner and easier to read.
# more pythonic way to write the is_even function, using a single return statement without an if-else structure. The expression n % 2 == 0 evaluates to True if n is even and False if n is odd, so we can return that directly.
def main():  
    x = int(input("Enter a number: "))

    #if x % 2 == 0:
    if is_even(x):
        print("The number is even.")
    else:
        print("The number is odd.")

def is_even(n):
    return n % 2 == 0
    #return True if n % 2 == 0 else False
    
main()
        