# Using conditionals to determine if a number is even or odd --- IGNORE ---

def main():  
    x = int(input("Enter a number: "))

    #if x % 2 == 0:
    if is_even(x):
        print("The number is even.")
    else:
        print("The number is odd.")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()
        