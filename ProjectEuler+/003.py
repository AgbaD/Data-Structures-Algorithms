#! /usr/bin/python
# Author:	@BlankGodd

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
	
# max prime factor
def m_pf(n):
	a = [i for i in range(1, n+1) if n%i==0]
	b = [i for i in a if is_prime(i)]
	print(b)
	return max(b)


if __name__ == "__main__":
	ans = []
	t = int(input("Enter the number of test cases: \n"))
	for i in range(t):
		n = int(input("Enter the integer n: "))
		ans.append(m_pf(n))
	for i in ans:
		print(i)
