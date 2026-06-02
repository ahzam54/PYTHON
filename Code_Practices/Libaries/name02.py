
import sys

# check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is ",sys.argv[1])

# This script checks the number of command-line arguments provided. If there are too few or too many arguments, 
# it prints an appropriate message. If exactly one argument is provided, it prints a greeting with that argument as the name. 