#!/usr/bin/python3
if __name__ == "__main__" :
    import sys
    arg_number = len(sys.argv)
    if arg_number == 1 :
        print("{} arguments.".format(arg_number - 1))
    else:
        print("{} arguments:".format(arg_number - 1))
        counter = 1
        while counter < arg_number:
         print("{}: {sys.argv[counter]}".format(counter))
         counter += 1
