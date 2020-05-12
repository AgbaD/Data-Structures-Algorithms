#!/usr/bin/python
# Author:	@BlankGodd

class Stack:
	"""Last in First Out"""

	def __init__(self):
		self._stack = []
		self._size = 0

	def add(self, data):
		# adding to a stack
		self._stack.append(data)
		self._size += 1

	def remove(self):
		# getting the item top of the stack
		if self._size == 0:
			print("Stack is Empty!")
			return
		x = self._stack[-1]
		del(self._stack[-1])
		self._size -= 1
		return x

	def top(self):
		# display the item top of the stack without removing
		if self._size == 0:
			print("Stack is Empty!")
			return
		print(self._stack[-1])

	def length(self):
		return self._size

	def flip(self):
		# to turn the stack over
		if self._size == 0 or self._size == 1:
			return
		a,b = 0,1
		x = [i for i in self._stack]
		for i in range(self._size):
			self._stack[a] = x[-b]
			a += 1
			b += 1

	def display(self):
		print(self._stack)


