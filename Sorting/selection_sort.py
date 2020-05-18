#!/usr/bin/python
# Author:	@BlankGodd

import sys

def sort(seq):
	# [5,3,6,1,8,7,2]
	length = len(seq)
	for i in range(length):
		small = i
		for j in range(i+1, length):
			if seq[j] < seq[small]:
				small = j
		seq[i],seq[small] = seq[small],seq[i]


if __name__ == "__main__":
	a = input("Enter list seperated by commas: \n")
	try:
		s = [int(i) for i in a.split(",")]
	except:
		print("Invalid entry")
		sys.exit(2)
	sort(s)
	print(s)


