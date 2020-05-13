#!/usr/bin/python
# Author:	@BlankGodd

import sys
import math

def is_prime(n):
	# Dosen't cover negative values
	sqr = int(math.sqrt(n))
	if n <= 1:
		return False
	elif n == 2 or n == 3:
		return True
	else:
		for x in range(2,sqr+1):
			if n%x==0:
				return False
		return True

# first n primes
def fnprime(n):
	a = []
	i = 2
	while len(a) < n:
		if is_prime(i):
			a.append(i)
		i += 1
	return a[-1]


if __name__ == "__main__":
	try:
		num = int(sys.argv[1])
	except:
		num = None
	if num:
		print(fnprime(num))
	else:
		num = int(input("Enter value: "))
		print(fnprime(num))