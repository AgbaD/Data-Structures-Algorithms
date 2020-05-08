#!/usr/bin/python
# Author:	@BlankGodd

from datetime import datetime

def is_prime(n):
	# Dosen't cover negative values
	if n <= 1:
		return False
	elif n == 2 or n == 3:
		return True
	else:
		for x in range(2,(n//2)+1):
			if n%x==0:
				return False
		return True

# first n primes
def fnprime(n):
	a = [i for i in range(2, n) if is_prime(i)]
	return sum(a)


if __name__ == "__main__":
	st = datetime.utcnow()
	print(fnprime(2_000_000))
	ed = datetime.utcnow()
	print(ed-st)

	