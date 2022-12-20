#!usr/bin/python3
# Author:   @AgbaD || @aba_dr3

class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:

    def __init__(self):
        self.root = None

    # insert start
    def prepend(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            temp = self.root
            self.root = Node(data)
            self.root.next = temp
            temp.prev = self.root

    # insert end
    def append(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            cur = self.root
            while cur.next:
                cur = cur.next

            temp = Node(data)
            cur.next = temp
            temp.prev = cur

    # remove start
    def pop(self):
        if not self.root:
            print("Double Linked List is empty!")
            return
        elif self.root.next:
            temp = self.root.next
            self.root = temp
            self.root.prev = None
        else:
            self.root = None

    # remove end
    def push(self):
        if not self.root:
            print("Double Linked List is empty!")
            return
        elif not self.root.next:
            self.root = None
        else:
            self.remove(self.root)

    def remove(self, node):
        if not node.next.next:
            node.next = None
        else:
            self.remove(node.next)

    def remove_value(self, value):
        if not self.root:
            print("Double Linked List is empty!")
            return
        elif self.root.data == value and not self.root.next:
            self.root = None
        elif self.root.data == value and self.root.next:
            temp = self.root.next
            self.root = temp
            self.root.prev = None
        elif self.root.data != value and not self.root.next:
            print("Double linked list does not contain value!")
            return
        else:
            self.rem(self.root, value)

    def rem(self, node, value):
        if node.next.data == value:
            if node.next.next:
                temp = node.next.next
                temp.prev = node
                node.next = temp
            else:
                node.next = None
        else:
            if node.next.next:
                self.rem(node.next, value)
            else:
                print("Double linked list does not contain value!")
                return

    def traverse(self):
        lst = []
        if not self.root:
            print("Double Linked List is empty!")
            return
        else:
            lst.append(self.root.data)
            cur = self.root
            while cur.next:
                cur = cur.next
                lst.append(cur.data)
        print(lst)


if __name__ == "__main__":
    lst = DoubleLinkedList()

    lst.traverse()

    lst.append(17)
    lst.prepend(16)
    lst.prepend(15)
    lst.prepend(14)
    lst.prepend(13)
    lst.prepend(12)

    lst.append(18)
    lst.append(19)

    lst.traverse()

    lst.pop()
    lst.push()
    lst.push()

    lst.traverse()

    lst.remove_value(15)
    lst.traverse()
