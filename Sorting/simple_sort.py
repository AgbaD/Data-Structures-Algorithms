#! /usr/bin/python
# Author:	@BlankGodd


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
	s = input("Enter values of list seperated by commas \n")
	seq = [int(i) for i in s.split(',')]
	sort = Sort(seq)
	print(sort.seq)


