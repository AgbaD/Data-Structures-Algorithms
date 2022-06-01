#!/usr/bin/python

def dcp_608(lst, start, end):
    seq = []
    i, j = 0, 0
    while j < len(start):
        for v in start:
            if start not in seq:
                seq.append(start)
            if v != end[i]:
                temp = start.replace(v, end[i])
                if temp in lst:
                    start = temp
            i += 1
        i = 0
        j += 1

    if start == end:
        return seq
    else:
        return None


if __name__ == "__main__":
    lst = ["dot", "dop", "dat", "cat"]
    start = 'dog'
    end = 'cat'
    print(dcp_608(lst, start, end))
