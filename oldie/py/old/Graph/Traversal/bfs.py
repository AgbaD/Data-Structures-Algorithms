#!/usr/bin/python
# Author:	@BlankGodd

class Node:

	def __init__(self, name):
		self.name = name
		self.neighbours = []
		self.visited = False
		self.pedecessor = None

class Bfs:
	"""Breadth first search implementation"""
	def __init__(self, startnode):
		# uses a queue for implementation

		q = []
		q.append(startnode)
		startnode.visited = True

		while q:
			node = q.pop(0)
			print('%s ' % node.name)

			for n in node.neighbours:
				if not n.visited:
					n.visited = True
					q.append(n)

"""
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.neighbours.append(node2)
node1.neighbours.append(node3)
node2.neighbours.append(node4)
node4.neighbours.append(node5)

Bfs(node1)
"""


