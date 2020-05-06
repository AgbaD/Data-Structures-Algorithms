#!/usr/bin/python
# Author:	@BlankGodd

import sys

def gcd(a,b):
	if a == 0:
		return b
	return gcd(b%a, a)

def lcm(a,b):
	return (a*b)/gcd(a,b)


def main(n):
	a = [i for i in range(2,n+1)]
	b = lcm(a[0], a[1])
	i = 2
	while i < len(a):
		d = b
		b = lcm(d, a[i])
		i += 1
	return int(b)

if __name__ == "__main__":
	try:
		n = int(sys.argv[1])
	except:
		n = None
	if n:
		print(main(n))
	else:
		n = int(input("Enter value: "))
		print(main(n))

