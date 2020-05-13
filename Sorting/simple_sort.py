#! /usr/bin/python
# Author:	@BlankGodd

import sys

class Sort:
	"""For sorting a list with non-repeating values"""

	def __init__(self, seq):
		self.seq = seq
		self.a = max(seq)
		self.b = {}
		i = set(self.seq)
		if len(i) != len(self.seq):
			print("Sequence consists of repeating values")
			return
		self.sort()

	def sort(self):
		i = 0
		k = 0
		while i <= self.a:
			if i in self.seq:
				self.b[k] = i
				k += 1
			i += 1

		for k,v in self.b.items():
			self.seq[k] = v
	

	def __repr__(self):
		return ''

if __name__ == "__main__":
	a = input("Enter list Seperated by commas: \n")
	try:
		seq = [int(i) for i in a.split(",")]
	except:
		print("Invalid entry")
		sys.exit(2)
	sort = Sort(seq)
	print(sort.seq)


