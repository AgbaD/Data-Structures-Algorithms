#!/usr/bin/python
# Author:	@BlankGodd

class Node:

	def __init__(self, name):
		self.name = name
		self.neighbours = []
		self.visited = False
		self.pedecessor = None


class Dfs:
	"""Depth First search implementation"""

	def dfs(self, startnode):
		# using recursion, stacks are internally implemented

		startnode.visited = True
		print("%s " % startnode.name)

		for i in startnode.neighbours:
			if not i.visited:
				self.dfs(i)


