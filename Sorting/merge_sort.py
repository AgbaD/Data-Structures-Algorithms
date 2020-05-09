#!/usr/bin/python
# Author:	@BlankGodd

import sys

def sort(seq, count):
	length = len(seq)
	if length > 1:
		mid = length // 2
		left = seq[:mid]
		right = seq[mid:]
		count = sort(left, count)
		count = sort(right, count)

		# left_index, right_index, index
		li, ri, i = 0, 0, 0
		while li < len(left) and ri < len(right):
			if left[li] < right[ri]:
				seq[i] = left[li]
				li += 1
			else:
				seq[i] = right[ri]
				ri += 1
			i += 1

		while li < len(left):
			seq[i] = left[li]
			li += 1
			i += 1

		while ri < len(right):
			seq[i] = right[ri]
			ri += 1
			i += 1

		count += 1

	if len(seq) == length:
		return
	return count


if __name__ == "__main__":
	a = input("Enter list Seperated by commas: \n")
	try:
		seq = [int(i) for i in a.split(",")]
	except:
		print("Invalid entry")
		sys.exit(2)
	count = 0
	sort(seq, count)
	print(seq)
