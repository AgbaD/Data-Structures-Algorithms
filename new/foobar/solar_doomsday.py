#!/usr/bin/python
# Author: AgbaD || BlankGodd

import math

def solution(area: int):
    res = []
    while area > 0:
        square = int(math.sqrt(area))**2
        area -= square
        res.append(square)
    return res



if __name__ == "__main__":
    print(solution(12))
    print(solution(15324))
