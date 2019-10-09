#!/usr/bin/python

import sys

cache = {}

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    # 0 cookies can only be eaten 1 way - not at all
    if n <= 0:
        return 1
    
    # One cookie can only be eaten in one way
    elif n == 1:
        return 1

    # Two cookies can be eaten in two ways
    elif n == 2:
        return 2

    # Three cookies can be eaten in four ways ([1, 2], [2,1], [1, 1, 1], [3])
    elif n == 3:
        return 4

    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')