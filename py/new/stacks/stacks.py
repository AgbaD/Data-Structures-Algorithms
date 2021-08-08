#!/usr/bin/python
# Author:   @AgbaD || @agba_dr3


class Stack:

    def __init__(self, size):
        self.def_size = size
        self.cur_size = 0
        
        self.list = [None] * size

    def add(self, value):
        if self.cur_size >= self.def_size:
            print("Current stack is full")
            return
        self.list[cur_size] = value
        cur_size += 1

    def remove(self):
        if self.cur_size == 0:
            print("Current stack is empty")
            return
        val = self.list.pop(cur_size - 1)
        self.list.append(None)
        cur_size -= 1
        return val

    def resize(self, size):
        if size < self.cur_size:
            print("Current stack size is greater that new size")
            return
        if size < self.def_size:
            diff = self.def_size - size
            for i in range(diff):
                self.list.del(-1)
            self.def_size = size
        elif size == self.def_size:
            print("Current size equals new size")
        else:
            diff = size - self.def_size
            for i in range(diff):
                self.list.append(None)
            self.def_size = size

    def getSize(self):
        return self.cur_size

    def getDefSize(self):
        return self.def_size

    def isFull(self):
        if self.cur_size == self.def_size:
            return True
        return False
    
    def isEmpty(self):
        if self.cur_size == 0:
            return True
        return False

    def traverse(self):
        if self.cur_size == 0:
            print("Current stack is empty!")
            return
        lst =  [i for i in self.list if i]
        return lst[::-1]
