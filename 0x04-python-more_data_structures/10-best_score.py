#!/usr/bin/python3
def best_score(a_dictionary):
    board = a_dictionary
    player = None
    score = 0
    if type(a_dictionary) == dict or a_dictionary is not None:
        for k in a_dictionary:
            if board.get(k) > score:
                score = board.get(k)
                player = k

    return player
