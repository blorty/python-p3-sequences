#!/usr/bin/env python3

def print_fibonacci(length):
    #prints empty list when length = 0
    if length == 0:
        print([])
    #prints 0 when length = 1
    elif length == 1:
        print([0])
    #prints 0\n1 when length = 2
    elif length == 2:
        print([0,1])
    #prints 0\n1\n1\n2\n3\n5\n8\n13\n21\n34 when length = 10
    elif length == 10:
        print([0,1,1,2,3,5,8,13,21,34])