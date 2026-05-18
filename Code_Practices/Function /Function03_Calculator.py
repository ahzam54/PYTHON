def main():
    x = float(input("What is x? "))
    print("x squared is", square(x))

# Function to calculate the square of a number
def square(n):
    return n * n
    # return n ** 2 # Alternative way to calculate the square
    # return pow(n,2) # Another alternative way to calculate the square

# Calling main function
main()