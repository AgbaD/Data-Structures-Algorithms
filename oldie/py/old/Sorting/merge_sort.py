#!/usr/bin/python
# Author:	@BlankGodd

import sys

def merge(s1, s2, s):
	# s has to be a predefined list
	i,j = 0,0
	while i + j < len(s):
		if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
			s[i + j] = s1[i]
			i += 1
		else:
			s[i + j] = s2[j]
			j += 1

def sort(s):
	n = len(s)
	if n < 2:
		return
	mid = n//2
	s1 = s[:mid]
	s2 = s[mid:]

	sort(s1)
	sort(s2)

	merge(s1, s2, s)


if __name__ == "__main__":
	a = input("Enter list Seperated by commas: \n")
	try:
		s = [int(i) for i in a.split(",")]
	except:
		print("Invalid entry")
		sys.exit(2)
	sort(s)
	print(s)

	