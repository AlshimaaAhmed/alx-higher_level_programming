#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (TypeError, IndexError, ValueError, ZeroDivisionError)as error:
        print("Exception:", error, file=sys.stderr)
        result = None
    return result
