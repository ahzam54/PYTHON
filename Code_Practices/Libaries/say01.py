
# this code draw a dinosaur and say hello to the name you input in the command line
import cowsay

import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, my name is " + sys.argv[1])