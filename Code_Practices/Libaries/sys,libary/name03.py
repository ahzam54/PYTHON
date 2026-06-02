
# using sys.exit to exit program prematurely if there are too few or too many command-line arguments.
import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is ",sys.argv[1])