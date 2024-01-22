#!/usr/bin/python3
if __name__ == "__main__":
 import sys
 arg_number = len(sys.argv)
 counter = 1
 add = 0
 while counter < arg_number:
    add += int(sys.argv[counter])
    counter += 1
print(add)
