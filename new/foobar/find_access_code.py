#!/usr/bin/python
# Author: AgbaD || BlankGodd

def solution(l):
    """
        Write a function solution(l) that takes a list of positive integers l 
        and counts the number of "lucky triples" of (li, lj, lk) where the 
        list indices meet the requirement i < j < k.  The length of l is between 
        2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  
        The solution fits within a signed 32-bit integer. Some of the lists are 
        purposely generated without any access codes to throw off spies, so if 
        no triples are found, return 0. 

        For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], 
        making the solution 3 total.
    """
    # dynamic programming
    c = [0] * len(l)
    count = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                c[i] += 1
                count += c[j]
    return count
