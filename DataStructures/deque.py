#!/usr/bin/python
# Author:	@BlankGodd

class Deque:
	"""Double-ended queue"""
	# default size
	def_size = 5

	def __init__(self):
		self._deque = [None] * Deque.def_size
		self._size = 0

	def resize(self, size):
		if size < Deque.def_size:
			if size < self._size:
				print("Current members greater than new size")
				return
			x = Deque.def_size - size
			if x == 1:
				del(self._deque[-x])
			else:
				for i in range(x):
					del(self._deque[-1])
			Deque.def_size = size
		else:
			x = size - Deque.def_size
			a = [None] * x
			self._deque.extend(a)
			Deque.def_size = size

	def add_front(self, data):
		if self._size == Deque.def_size:
			print("Deque Full!! please resize")
			return
		self._deque.insert(0, data)
		del(self._deque[-1])
		self._size += 1

	def add_back(self, data):
		if self._size == Deque.def_size:
			print("Deque Full! please resize")
			return
		self._deque[self._size] = data
		self._size += 1

	def remove_front(self):
		if self._size == 0:
			print('Empty Deque')
			return
		x = self._deque[0]
		del(self._deque[0])
		self._size -= 1
		self._deque.append(None)
		return x

	def remove_back(self):
		if self._size == 0:
			print('Empty Deque')
			return
		x = self._deque[self._size -1]
		del(self._deque[self._size - 1])
		self._size -= 1
		self._deque.append(None)
		return x

	def lenght(self):
		return self._size

	def display(self):
		a = []
		if self._size == 0:
			print(a)
			return
		for i in range(self._size):
			a.append(self._deque[i])
		print(a)

	def first(self):
		if self._size == 0:
			print("Empty deque!")
			return
		return self._deque[0]

	def last(self):
		if self._size == 0:
			print("Empty Queue!")
			return
		return self._deque[self._size - 1]



