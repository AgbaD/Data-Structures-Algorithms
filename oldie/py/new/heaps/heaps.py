#!/usr/bin/python3
# Author:   @AgbaD || @agba_dr3

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class Heap:

    def __init__(self):
        self.root = None
        self.pointer = None
        self.count = 0

    def add(self, data):
        newnode = Node(data)
        if not self.root:
            self.root = newnode
            count += 1
        else:
            pointer = self.root
            bitcount = bin(int(self.count + 1)).replace('0b', '')
            for i in range(1, len(bitcount)):
                if bitcount[i] == '0':
                    if pointer.left == None:
                        pointer.left = newnode
                        pointer.left.parent = pointer
                    pointer = pointer.left
                else:
                    if pointer.right == None:
                        pointer.right = newnode
                        pointer.right.parent = pointer
                    pointer = pointer.right
            while True:
                if pointer == self.root:
                    break
                if pointer.data < pointer.parent.data:
                    temp = pointer.data
                    pointer.data = pointer.parent.data
                    pointer.parent.data = temp
                    pointer = pointer.parent
                else:
                    break
            count += 1

    def remove(self):
        value = self.root.data
        pointer = self.root
        bitcount = bin(int(self.count)).replace('0b', '')
        for i in range(1, len(bitcount)):
            if bitcount[i] == '0':
                pointer = pointer.left
            else:
                pointer = pointer.right
        self.root.data = pointer.data
        try:
            if pointer.parent.left == pointer:
                pointer.parent.left = None
            else:
                pointer.parent.right = None
            count -= 1
            self.heapify()
        except:
            self.root = None
        return value

    def heapify(self):
        pointer = self.root
        compare = None
        while True:
            if pointer.left == None:
                if pointer.right == None:
                    break
                else:
                    if pointer.right.data < pointer.data:
                        temp = pointer.data
                        pointer.data = pointer.right.data
                        pointer.right.data = temp
                        pointer = pointer.right
                    else:
                        break
            else:
                if pointer.right == None:
                    if pointer.left.data < pointer.data:
                        temp = pointer.data
                        pointer.data = pointer.left.data
                        pointer.left.data = temp
                        pointer = pointer.left
                    else:
                        break
                else:
                    if pointer.left.data <= pointer.right.data:
                        compare = pointer.left
                    else:
                        compare = pointer.right
                    
                    if compare.data < pointer.data:
                        temp = pointer.data
                        pointer.data = compare.data
                        compare.data = temp
                        pointer = compare
                    else:
                        break
