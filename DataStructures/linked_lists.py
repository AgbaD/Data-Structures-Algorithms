#!/usr/bin/python
# Author:	@BlankGodd

class Node:
	
	def __init__(self, data=None):
		self.data = data
		self.prev = None
		self.next = None

class Linked_list:
	"""Doubly linked list"""
	def __init__(self):
		self.head = Node()
		self.size = 0

	def append(self, data):
			if not self.head.data:
				self.head.data = data
				self.size += 1
			else:
				self.append_node(self.head, data)

	def append_node(self, node, data):
		if node.next:
			self.append_node(node.next, data)
		else:
			new_node = Node(data)
			node.next = new_node
			new_node.prev = node
			self.size += 1

	def prepend(self, data):
		if not self.head.data:
			self.head.data = data
		else:
			cur = self.head
			new_node = Node(data)
			new_node.next = cur
			cur.prev = new_node
			self.head = new_node
		self.size += 1

	def length(self):
		print(self.size)

	def display(self):
		if not self.head.data:
			print("List is empty!")
		else:
			self.display_nodes()	

	def display_nodes(self):
		lst = []
		cur = self.head
		lst.append(cur.data)
		while cur.next:
			lst.append(cur.next.data)
			cur = cur.next
		print(lst)

	def pop(self):
		# To remove the last data
		if not self.head.data:
			print("Empty List!")
		else:
			self.pop_value(self.head)

	def pop_value(self, node):
		if node.next:
			self.pop_value(node.next)
		else:
			prev = node.prev
			print(node.data)
			prev.next = None
			self.size -= 1


