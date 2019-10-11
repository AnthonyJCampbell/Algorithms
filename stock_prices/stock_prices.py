#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # An easy way to initialize the value is to take the largest value in the array and make it negative
    max_profit = -max(prices)
    arr = prices.copy()

    # Loop over the list
    for i in range(len(prices)):
        # Take the first element off the copied array to account for the other items in the list.
        arr.pop(0)

        # Loop over all the remaining items in the list, done through arr
        for j in arr:
            # If the difference between j and i is greater than max_profit
            if j-prices[i] > max_profit:
                # print(f"{j} is larger than {prices[i]} and makes for a profit of {j - prices[i]}, which is larger than our previous highest!")
                max_profit = j - prices[i]
    print(max_profit)
    return max_profit




if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))