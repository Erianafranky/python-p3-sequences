#!/usr/bin/env python3
""" 
The Fibonacci Sequence is a series of numbers
The next number is found by adding up the two numbers before it
function print_fibonacci() prints empty list when length = 0
prints 0 when length = 1
prints 0, 1 when length = 2
prints 0,1,1,2,3,5,8,13,21,34 when length = 10
 """

def print_fibonacci(length): 
    result = []
    counter = 0
    for i in range(length):
        result.append(counter)
        if counter == 0:
            counter = 1
        else:
            counter=result[i]+result[i-1]
        
    print(result)

