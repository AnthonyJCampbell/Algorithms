#!/usr/bin/python

import sys

cache = {}

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
possibilities = 0
def eating_cookies(n, cache=None):
    global possibilities

    # Base case happens when n < 0
    if n < 1:
        possibilities = 1
        return possibilities

    elif n >= 1 and n <= 3:
        if n - 1 == 0:
            possibilities += 1
        if n - 2 == 0:
            possibilities += 2
        if n - 3 == 0:
            possibilities += 4
        return possibilities
    else:
        eating_cookies(n-1)
        eating_cookies(n-2)
        eating_cookies(n-3)

    

    return possibilities

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')