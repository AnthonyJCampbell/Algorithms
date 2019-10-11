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

    # If amount is zero, there's only one way to change that.
    if amount == 0:
        print(f"Amount is 0, returning 1")
        return 1

    # If amount is less than zero, there's an error. Return 0
    if amount < 0:
        return 0


    if len(denominations) <= 0 and amount > 0:
        return 0

    else:
        return making_change(amount - denominations[-1], denominations) \
            + making_change(amount, denominations[:-1])

arr = [1,2,3]
print(arr[-1])

if __name__ == "__main__":
# Test our your implementation from the command line
# with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")