#!/usr/bin/python
# Author: AgbaD || BlankGodd

from functools import reduce

def solution(xs):
    """
        Write a function solution(xs) that takes a list of integers 
        representing the power output levels of each panel in an array,
        and returns the maximum product of some non-empty subset of 
        those numbers. So for example, if an array contained panels with 
        power output levels of [2, -3, 1, 0, -5], then the maximum product 
        would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, 
        giving the product 2*(-3)*(-5) = 30.  So solution([2,-3,1,0,-5]) will be "30",
        solution([2, 0, 2, 2, 0]) will be "8", and solution([-2, -3, 4, -5]), will be "60.
    """
    # Your code here
    neg = sorted([i for i in xs if i < 0])
    pos = sorted([i for i in xs if i > 0])
    neg = neg[:-1] if len(neg) % 2 != 0 else neg
    product = reduce(lambda a, b: a * b, neg) if len(neg) != 0 else 0

    if len(pos) == 0:
        neg = [i for i in xs if i < 0]
        return str(neg[0]) if len(neg) == len(xs) else '0' if product == 0 else str(product)
    else:
        pos = pos[1:] if (len(pos) + len(neg)) == len(xs) else pos
        return str(reduce(lambda a, b: a * b, pos)) if product == 0 else str(reduce(lambda a, b: a * b, pos + [product]))
        
