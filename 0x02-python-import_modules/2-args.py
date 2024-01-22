#!/usr/bin/python3
if __name__ == "__main__" :
    import sys
    arg_number = len(sys.argv)
    if arg_number == 1 :
        print(f"{arg_number - 1} arguments.")
    else:
        print(f"{arg_number - 1} arguments:")
        counter = 1
        while counter < arg_number:
         print(f"{counter}: {sys.argv[counter]}")
         counter += 1
