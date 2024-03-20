#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("1 argument:")
        print("1: {}".format(arg[1]))
    else:
        print("{} arguments:".format(size))
        for i in range(1, size + 1):
            print("{}: {}".format(i, arg[i]))
