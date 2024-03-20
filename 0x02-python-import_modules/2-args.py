#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1
if num_args == 0:
    print("{} arguments.".format(num_args))
elif num_args == 1:
    print("{} argument:".format(num_args))
else:
    print("{} arguments:".format(num_args))
for i in range(1, len(argv)):
    print("{}: {}".format(i, argv[i]))
