#!/usr/bin/python3
if __name__=="__main__":
    import sys
    n = len(sys.argv)
    i = 1
    cant = 0
    while i < n :
        cant = cant + int(sys.argv[i])
        i = i + 1
    print("{:d}".format(cant))
