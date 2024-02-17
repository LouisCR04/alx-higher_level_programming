#!/usr/bin/python3
"""Finds peak in a list"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    li = list_of_integers
    eng = len(li)
    if eng == 0:
        return
    m = eng // 2
    if (m == eng - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != eng - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
