#!/usr/bin/python
# Author:	@BlankGodd

import sys

def sum_o_sq(num):
	a = [i**2 for i in range(1, num+1)]
	return sum(a)

def sq_o_sum(num):
	a = [i for i in range(1, num+1)]
	b = sum(a)
	return b**2

def main(num):
	a,b = sq_o_sum(num), sum_o_sq(num)
	if a > b:
		return a - b
	return b - a


if __name__ == "__main__":
	try:
		num = int(sys.argv[1])
	except:
		num = None
	if num:
		print(main(num))
	else:
		num = int(input("Enter value: "))
		print(main(num))
