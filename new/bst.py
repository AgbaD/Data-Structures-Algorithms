#!/usr/bin/python
# Author:   @AgbaD | @agba_dr3

class Node:
    value = None
    left_child = None
    right_child = None

    def __init__(value):
        self.value = value


class Bst:
    root = None

    def insert(self, value):
        if self.root:
            self.insert_child(value, root)
        else:
            self.root = Node(value)

    def insert_child(self, value, node):
        if value > node.value:
            if node.right_child:
                self.insert_child(value, node.right_child)
            else:
                temp = Node(value)
                node.right_child = temp
        if value < node.value:
            if node.left_child:
                self.insert_child(value, node.left_child)
            else:
                temp = Node(value)
                node.left_child = temp

    def get_min(self):
        if self.root.left_child:
            return self.get_minimum(self.root.left_child)
        return self.root.value

    def get_minimum(self, node):
        if node.left_child:
            return self.get_minimum(node.left_child)
        return node.value

    def get_max(self):
        if self.root.right_child:
            return self.get_maximum(self.root.right_child)
        return self.root.value

    def get_maximum(self, node):
        if node.right_child:
            return self.get_maximum(node.right_child)
        return node.value

    def search(self, value):    # to see if a value is in a bst
        if value < self.root.value:
            return self.search_left(value, self.root)
        elif value > self.root.value:
            return self.search_right(value, self.root)
        else:
            if value != self.root.value:
                return False
            return True
    
    def search_left(self, node):
        if value == node.value:



    
