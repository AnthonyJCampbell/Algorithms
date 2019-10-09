#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    # In any given round of RPS, you can have three possible plays, for n rounds
    # We should return a single list which contains all options that start with rock, all options that start with paper, and all options that start with scissors, and so on.
    # Declare list
    list_of_moves = []
    options = ["rock", "paper", "scissors"]

    # If 0 rounds are played, the amount of possible moves is zero - hence an empty list
    if n == 0:
        return []

    # Declare a recursive function within rps()
    def rps_rec(played_moves, n):
        # Establish a base-case to cut off the recursion
        if n == 0:
            return list_of_moves.append(played_moves)
        else:
            for i in range(len(options)):
                rps_rec(played_moves + [options[i]], n-1)

    # Initial call to recursive helper
    rps_rec([], n)

    # return list that has all options 
    return list_of_moves

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')