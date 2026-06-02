
import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

#using [1:] to skip the first argument which is the script name itself.
# it slices the list 
for arg in sys.argv[1:]:
    print("hello, my name is ", arg)