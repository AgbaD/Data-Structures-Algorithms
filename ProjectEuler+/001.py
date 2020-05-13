#!/usr/bin/python
# Author:	@BlankGodd


def s_m(n):
	a = [i for i in range(1, n) if i%3==0 or i%5==0]
	return sum(a)

if __name__ == "__main__":
	ans = []
	t = int(input("Enter the number of test cases: \n"))
	for i in range(t):
		n = int(input("Enter the integer n: "))
		ans.append(s_m(n))

	for i in ans:
		print(i)


