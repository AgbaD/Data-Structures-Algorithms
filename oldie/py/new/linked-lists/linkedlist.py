#!/usr/bin/python3
# Author:   @AgbaD || @agba_dr3


# ================ Linked List =================== #

class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def insert_start(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            new_node = Node(value)
            cur = self.root
            self.root = new_node
            new_node.next = cur

    def insert_end(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.insert(self.root, value)

    def insert(self, node, value):
        if node.next:
            self.insert(node.next, value)
        else:
            new = Node(value)
            node.next = new

    def remove_start(self):
        if not self.root:
            print("Linked list has no values")
            return
        else:
            if self.root.next:
                temp = self.root.next
                self.root = temp
            else:
                self.root = None

    def remove_end(self):
        if not self.root:
            print("Linked list has no values")
            return
        elif self.root.next:
            self.remove(self.root)
        else:
            self.root = None

    def remove(self, node):
        if node.next:
            if node.next.next:
                self.remove(node.next)
            else:
                node.next = None

    def remove_value(self, value):
        if not self.root:
            print("Linked list has no values")
            return
        elif self.root.value == value and not self.root.next:
            self.root = None
        elif self.root.value != value and not self.root.next:
            print("Linked list does not contain value")
            return
        elif self.root.value == value and self.root.next:
            temp = self.root.next
            self.root = temp
        else:
            self.rm(self.root, value)

    def rm(self, node, value):
        if node.next.value == value:
            if node.next.next:
                temp = node.next.next
                node.next = temp
            else:
                node.next = None
        else:
            if node.next.next:
                self.rm(node.next, value)
            else:
                print("Linked list does not contain value")
                return

    def traverse(self):
        if not self.root:
            print("Linked list has no values")
            return
        lst = []
        lst.append(self.root.value)
        if self.root.next:
            self.add(lst, self.root)
        print(lst)

    def add(self, lst, node):
        lst.append(node.next.value)
        if node.next.next:
            self.add(lst, node.next)


if __name__ == "__main__":
    l = LinkedList()
    l.traverse()

    l.insert_start(7)
    l.insert_start(5)
    l.insert_start(3)

    l.traverse()

    l.insert_end(9)
    l.insert_end(11)

    l.traverse()

    l.remove_end()

    l.traverse()

    l.remove_start()

    l.traverse()

    l.remove_value(7)

    l.traverse()