#!/usr/bin/python
# Author:	@BlankGodd

class Queue:
	"""First in first out"""
	# default size
	def_size = 5

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
				for i in range(1,x+1):
					del(self._line[-i])
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


q = Queue()

q.display()
print(q.length())
q.add("Sade")
q.add("Tola")
q.add("Femi")

print()
q.display()

print(q.length())
print()

print(q.last())
print(q._line)
q.add("Nike")
q.add("Fola")

q.display()
print(q.length())

print()
q.add("Tobi")
q.display()
print(q._line)
q.remove()
q.remove()
q.display()
print(q._line)
print(q.length())
print()
print(q.def_size)
q.resize(2)
q.resize(4)
q.display()
print(q._line)
print(q.def_size)
q.resize(7)
q.display()
print(q._line)
print(q.length())

print(q.def_size)

q.resize(4)
print(q.def_size)
print(q.length())
q.display()
q.add('Simi')
print(q.length())
q.display()
