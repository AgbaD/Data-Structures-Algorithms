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


    
