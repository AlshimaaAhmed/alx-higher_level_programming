#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for counter in range(x):
            print("{:d}".format(my_list[counter]), end="")
            counter += 1
    except IndexError:
        pass
    print()
    return counter
          
