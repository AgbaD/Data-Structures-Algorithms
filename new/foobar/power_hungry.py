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
    giving the product 2*(-3)*(-5) = 30.  So solution([2,-3,1,0,-5]) will be "30".
    """
    # Your code here
    neg = [i for i in xs if i < 0]
    pos = [i for i in xs if i > 0]
    
    if len(neg) % 2 != 0:
        neg = sorted(neg)
        neg.pop()
    
    product = 0
    if len(neg) != 0:
        product = reduce(lambda a, b: a * b, neg)

    if len(pos) == 0:
        if product == 0:
            neg = [i for i in xs if i < 0]
            if len(neg) == len(xs):
                return str(neg[0])
            return '0'
        return str(product)
    else:
        if (len(pos) + len(neg)) == len(xs):
            pos = [i for i in reversed(sorted(pos))]
            pos.pop()
            
        if product == 0:
            if len(pos) == 0:
                return '0'
            else:
                product = reduce(lambda a, b: a * b, pos)
                return str(product)
        else:
            pos += [product]
            product = reduce(lambda a, b: a * b, pos)
            return str(product)
        
    
if __name__ == "__main__":
    a = [2, -3, 1, 0, -5]
    b = [2, 0, 2, 2, 0]
    c = [-2, -3, 4, -5]
    print(solution(a))
    print(solution(b))
    print(solution(c))
