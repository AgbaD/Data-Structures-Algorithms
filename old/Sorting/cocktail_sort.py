#!/usr/bin/python
# Author:	@BlankGodd

import sys

def sort(seq):
	"""Cocktail sort implementation"""
	# [5,3,6,1,8,7,2]

	length = len(seq)
	left, right = 0, length - 1 

	while left <= right:
		for i in range(left, right):
			if seq[i] > seq[i+1]:
				seq[i], seq[i+1] = seq[i+1], seq[i]
		right -= 1
		for i in range(right, left, -1):
			if seq[i-1] > seq[i]:
				seq[i-1], seq[i] = seq[i], seq[i-1]
		left += 1


if __name__ == "__main__":
	a = input("Enter list Seperated by commas: \n")
	try:
		seq = [int(i) for i in a.split(",")]
	except:
		print("Invalid entry")
		sys.exit(2)
	sort(seq)
	print(seq)


