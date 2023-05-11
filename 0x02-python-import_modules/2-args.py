#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = len(sys.argv)
    arg = num - 1

    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(arg))
        for i in range(1, num):
            print("{:d}: {:s}".format(i, sys.argv[i]))
