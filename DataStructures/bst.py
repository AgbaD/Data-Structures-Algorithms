#!/usr/bin/python
# Author:	@BlankGodd

class Node:
	"""Binary Search Tree"""

	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

class Bst:

	def __init__(self):
		self.root = None
		self.size = 0

	def insert(self, data):
		if not self.root:
			self.root = Node(data)
			self.size += 1
		else:
			self.insert_node(self.root, data)

	def insert_node(self, node, data):
		if data < node.data:
			if node.leftChild:
				self.insert_node(node.leftChild, data)
			else:
				node.leftChild = Node(data)
				self.size += 1

		else:
			if node.rightChild:
				self.insert_node(node.rightChild, data)
			else:
				node.rightChild = Node(data)
				self.size += 1

	def get_min(self):
		if not self.root:
			print("Empty Tree!")
		else:
			self.get_minimum(self.root)

	def get_minimum(self, node):
		if node.leftChild:
			self.get_minimum(node.leftChild)
		else:
			print(node.data)

	def get_max(self):
		if not self.root:
			print("Empty Tree!")
		else:
			self.get_maximum(self.root)

	def get_maximum(self, node):
		if node.rightChild:
			self.get_maximum(node.rightChild)
		else:
			print(node.data)

	def traverse(self):
		if not self.root:
			print("Empty Tree!")
		else:
			self.lst = []
			self.traverse_in_order(self.root)
			print(self.lst)

	def traverse_in_order(self, node):
		if node.leftChild:
			self.traverse_in_order(node.leftChild)
		self.lst.append(node.data)
		if node.rightChild:
			self.traverse_in_order(node.rightChild)


