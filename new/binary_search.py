#!/usr/bin/python3
# Author: BlankGodd

def binary_search(lst: list, e: int):
    # upper limit
    u: int = len(lst) - 1
    # lower limit
    l: int = 0
    while l <= u:
        # middle element
        m: int = (u + l) // 2
        # guess
        g = lst[m]
        if g < e:
            l = m + 1
        elif g > e:
            u = m - 1
        else:
            return m
    return None


if __name__ == "__main__":
    lst: list = [1,2,3,4,5,6,7]
    e: int = 7
    print(binary_search(lst, e))
