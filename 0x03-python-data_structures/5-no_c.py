#!/usr/bin/python3
def no_c(my_string):
    filtered_chars = [item for item in my_string if item not in('C','c')]
    result_string = ''.join(filtered_chars)
    return result_string
