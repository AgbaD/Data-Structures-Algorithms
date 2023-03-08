#!/usr/bin/python
# Author: AgbaD || BlankGodd

import math

def solution(src, dest):
    """
        Write a function called solution(src, dest) which takes in two parameters: 
        the source square, on which you start, and the destination square, which 
        is where you need to land to solve the puzzle. The function should return an 
        integer representing the smallest number of moves it will take for you to 
        travel from the source square to the destination square using a chess knights 
        moves (that is, two squares in any direction immediately followed by one square 
        perpendicular to that direction, or vice versa, in an “L” shape). Both the source
        and destination squares will be an integer between 0 and 63, inclusive, and 
        are numbered like the example chessboard below:

        0	1	2	3	4	5	6	7
        8	9	10	11	12	13	14	15
        16	17	18	19	20	21	22	23
        24	25	26	27	28	29	30	31
        32	33	34	35	36	37	38	39
        40	41	42	43	44	45	46	47
        48	49	50	51	52	53	54	55
        56	57	58	59	60	61	62	63

        So solution(19, 36) will be 1, and solution(0, 1) will be 3.
    """
    # breath first search
    q, visited = [(src, 0)], set()
    while q:
        n = q.pop(0)
        if n[0] == dest:
            return n[1]
        x, y = int(math.floor(n[0]/8)), int(n[0]%8)
        row = [2, 2, -2, -2, 1, 1, -1, -1]
        col = [-1, 1, 1, -1, 2, -2, 2, -2]
        if (x, y) not in visited:
            visited.add((x, y))
            for i in range(8):
                u, v = x + row[i], y + col[i]
                q.append((u + v * 8, (n[1] + 1))) if (u >= 0 and u < 8 and v >= 0  and v < 8) else q
    return -1

