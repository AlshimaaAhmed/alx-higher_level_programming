#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    arr = dir(hidden_4)
    for i in range(0, len(arr)):
        if arr[i][:2] != "__":
            print("{:s}".format(arr[i]))
