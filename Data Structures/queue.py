#!/usr/bin/python
# Author:	@BlankGodd

class Queue:
	"""First in first out"""
	# default size
	def_size = 7

	def __init__(self):
		self._line = [None] * Queue.def_size
		self._size = 0

	def resize(self, size):
		if size < Queue.def_size:
			if size < self._size:
				print("Current members greater than new size")
				return
			x = Queue.def_size - size
			if x == 1:
				del(self._line[-x])
			else:
				for i in range(x):
					del(self._line[-1])
			Queue.def_size = size
		else:
			x = size - Queue.def_size
			a = [None] * x
			self._line.extend(a)
			Queue.def_size = size

	def add(self, val):
		if self._size == Queue.def_size:
			print("Queue Full!!, please resize")
			return
		self._line[self._size] = val
		self._size += 1

	def remove(self):
		if self._size == 0:
			print("Can not remove from empty queue")
			return 
		a = self._line[0]
		del(self._line[0])
		self._size -= 1
		self._line.append(None)
		return a

	def display(self):
		queue = []
		if self._size == 0:
			print(queue)
			return
		for i in range(self._size):
			queue.append(self._line[i])
		print(queue)

	def length(self):
		return self._size

	def first(self):
		if self._size == 0:
			return "Empty Queue!"
		return self._line[0]	

	def last(self):
		if self._size == 0:
			return "Empty Queue!"
		return self._line[self._size - 1]


