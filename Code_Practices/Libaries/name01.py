
import sys

try:
    print("hello, my name is ",sys.argv[1])
except IndexError:
    print("No name provided. Please provide a name as a command-line argument.")

# now if we run this script without providing a name, it will catch the IndexError and print the message instead of crashing.