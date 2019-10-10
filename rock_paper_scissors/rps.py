#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    # In any given round of RPS, you can have three possible plays, for n rounds
    # We should return a single list which contains all options that start with rock, all options that start with paper, and all options that start with scissors, and so on.
    # Declare list
    list_of_moves = []
    possible_plays = ["rock", "paper", "scissors"]

    # If 0 rounds are played, the amount of possible moves is zero - hence an empty list

    # Declare a recursive function within rps()
    # It is passed a list of the moves that have been played already and the number of rounds left
    def rps_rec(played_moves, n):
        # If 
        if n == 0:
            return list_of_moves.append(played_moves)
        else:
            # For every iteration of n, rerun the recursive function.
            # In range is done to account for each of the three possible plays
            for i in range(len(possible_plays)):
                # So we take the list of played moves and add any future possible plays to it.
                rps_rec(played_moves + [possible_plays[i]], n-1)

    if n == 0:
        return [[]]
    else:
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