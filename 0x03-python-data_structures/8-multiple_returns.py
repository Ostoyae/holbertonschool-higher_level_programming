#!/usr/bin/python3
def multiple_returns(sentence):
    ls = list(sentence)
    if len(sentence) == 0:
        return (0, None)

    return (len(sentence), ls[0])
