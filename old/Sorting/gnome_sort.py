#!/usr/bin/python
# Author:	@BlankGodd

import sys

def sort(seq):
	"""Gnome sort implementation"""
	length = len(seq)
	i, j = 1, 2

	while i < length:
		if seq[i-1] < seq[i]:
			i, j = j, j+1
		else:
			seq[i-1], seq[i] = seq[i], seq[i-1]
			i -= 1
			if i == 0:
				i,j = j, j+1

if __name__ == "__main__":
	a = input("Enter list Seperated by commas: \n")
	try:
		seq = [int(i) for i in a.split(",")]
	except:
		print("Invalid entry")
		sys.exit(2)
	sort(seq)
	print(seq)

