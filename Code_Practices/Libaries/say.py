
# code that draw a cow and say hello to the name you input in the command line
import cowsay

import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, my name is " + sys.argv[1])