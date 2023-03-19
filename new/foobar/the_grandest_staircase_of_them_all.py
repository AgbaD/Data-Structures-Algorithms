#!/usr/bin/python
# Author: AgbaD || BlankGodd

"""
    Write a function called solution(n) that takes a positive integer n 
    and returns the number of different staircases that can be built from 
    exactly n bricks. n will always be at least 3 (so you can have a staircase at all),
    but no more than 200, because Commander Lambda's not made of money!

    Each type of staircase should consist of 2 or more steps.  No two steps are allowed 
    to be at the same height - each step must be lower than the previous one. All steps 
    must contain at least one brick. A step's height is classified as the total amount 
    of bricks that make up that step.
    
    For example, when N = 3, you have only 1 choice of how to build the staircase, [2,1].
    When N = 200, you have 487067745 choices.
"""

# submitted solution
def sSolution(n):
    # your code here
    memo = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    return staircase(1, n, memo) - 1

def staircase(h, l, memo):
    if memo[h][l] != 0:
        return memo[h][l]
    if l == 0:
        return 1
    if l < h:
        return 0
    memo[h][l] = staircase(h + 1, l - h, memo) + staircase(h + 1, l, memo)
    return memo[h][l]


# working solution
# returns correct answer but fails test cases
def wSolution(n):
    # dynamic programming
    if not n or n < 3: 
        return 0
    base = [1, *([0]*(n))]
    for i in range(1, n):
        for j in range(n, i-1, -1):
            base[j] += base[j-i]  
    return base[n]


def fib(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b
    print(b)

if __name__ == "__main__":
    fib(200)