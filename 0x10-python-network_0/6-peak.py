#!/usr/bin/python3
"""
this script defind a function to find a peak
"""

def find_peak(list_of_integers):
    ls = list_of_integers
    peak = None
    if not ls:
        return peak
    cur = int(len(ls) / 2)
    if ls[0] > ls[1] and ls[0] > ls[-1]:
        return ls[0]
    elif ls[-1] > ls[-2]:
        return ls[-1]

    if ls[cur - 1] <= ls[cur] and ls[cur] >= ls[cur + 1]:
        peak = ls[cur]
    if not peak:
        peak = find_peak(ls[cur:])
    if not peak:
        peak = find_peak(ls[0:(cur - 1)])

    return peak
    
    
if __name__ == "__main__":
    pass
