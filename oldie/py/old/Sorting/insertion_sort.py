#!/usr/bin/python
# Author:	@BlankGodd

import sys

def sort(seq):
	# [5,3,6,1,8,7,2]
	b = 1
	while b < len(seq):
		a = b
		while a > 0: 
			if seq[a] < seq[a-1]:
				seq[a-1], seq[a] = seq[a], seq[a-1]
			else:
				break
			a -= 1 
		b += 1

if __name__ == "__main__":
	a = input("Enter list Seperated by commas: \n")
	try:
		seq = [int(i) for i in a.split(",")]
	except:
		print("Invalid entry")
		sys.exit(2)
	sort(seq)
	print(seq)


		