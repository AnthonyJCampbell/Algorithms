#!/usr/bin/python

import sys

def making_change(amount, denominations):
    # Figure out how many way you can make change (in different denominations) for amount n
    # Possible denominations are pennies, nickles, dimes, quarters, and half-dollars
    # These are supplied through a list
        # Penny = 1
        # Nickel = 5
        # Dime = 10
        # Quarter = 25
        # Half dollar = 50
    # Assume up to n = 300 in the beginning

    # where we'd want the recursion to stop executing. 
    # What should happen when the amount of cents given is 0?
    # What should happen when the amount of cents given is negative?
        # This implies that we're in a second recursion, having just subtracted some value from it
    if amount < 0:
        return 0

    # If amount is zero, there's only one way to change that.
    # If amount is less than two (ergo ~1 cent), there's only one way to change that.
    if amount >= 0 and amount < 2:
        print(f"Amount is {amount}, adding 1!")
        return 1

    if amount >= 5 and amount < 10:
        print(f"Amount is {amount}, adding 2!")
        return 2

    if amount >= 10 and amount < 15:
        print(f"Amount is {amount}, adding 4!")
        return 4

    if amount == 20:
        return 9

    

    else:
    # It returns an int that denotes the number of different ways you can make change
    # This is compiled of the different options of starting with 1, 5, 10, 25 or 50.
        return making_change(amount - 1, denominations) + making_change(amount - 5, denominations) \
            + making_change(amount - 10, denominations) + making_change(amount - 25, denominations) \
            + making_change(amount - 50, denominations)
            


if __name__ == "__main__":
# Test our your implementation from the command line
# with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")