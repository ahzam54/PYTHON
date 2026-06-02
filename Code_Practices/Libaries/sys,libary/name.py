# This is a simple Python script that prints the name of the script itself.

import sys

print("hello, my name is ",sys.argv[1])

# if name not provider, it will show index error, so we can use try and except to catch that error and print a message.