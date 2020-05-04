#!/usr/bin/python
# Author:	BlankGodd

class Sort:
	"""Bubble sort implementation"""

	def __init__(self, seq):
		self.seq = seq
		# seq = [4,8,6,3,7,2]

		length = len(self.seq)
		for i in range(length - 1):
			sorted = True
			for j in range(length - 1):
				if self.seq[j] > self.seq[j+1]:
					self.seq[j],self.seq[j+1] = self.seq[j+1],self.seq[j]
					sorted = False

			if sorted:
				break

if __name__ == "__main__":
	s = input("Enter values of list seperated by commas \n")
	seq = [int(i) for i in s.split(',')]
	sort = Sort(seq)
	print(sort.seq)


