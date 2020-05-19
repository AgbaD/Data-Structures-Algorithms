#! /usr/bin/python
# Author:	@BlankGodd

def fib_evens(n):
	a,b = 1,2
	l = []
	for i in range(10):
		l.append(a)
		a,b=b,b+a
	less = list(filter(lambda x : x < n, l))
	even = list(filter(lambda y: y%2==0, less))
	return sum(even)


if __name__ == "__main__":
	ans = []
	t = int(input("Enter the number of test cases: \n"))
	for i in range(t):
		n = int(input("Enter the integer n: "))
		ans.append(fib_evens(n))
	for i in ans:
		print(i)
