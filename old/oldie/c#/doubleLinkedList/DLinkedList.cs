using System;
using System.Collections.Generic;

namespace doubleLinkedList
{
    class DLinkedList
    {
        public Node root;
        public List<int> dlist = new List<int>();

        // Constructor
        public DLinkedList()
        {
            root = null;
        }   

        // Insert Start
        public void prepend(int value)
        {
            Node a = new Node(value);
            if (root == null)
            {
                root = a;
            }
            else
            {
                Node b = root;
                root = a;
                root.next = b;
                b.prev = root;
            }
        }

        // Insert End
        public void append(int value)
        {
            Node a = new Node(value);
            if (root == null)
            {
                root = a;
            }
            else
            {
                insertEnd(root, a);
            }
        }

        public void insertEnd(Node node, Node newnode)
        {
            if (node.next == null)
            {
                node.next = newnode;
                newnode.prev = node;
            }
            else
            {
                insertEnd(node.next, newnode);
            }
        }

        // Remove Start
        public void pop()
        {
            if (root == null)
            {
                Console.WriteLine("Double Linked List is empty!");
            }
            else if (root.next == null)
            {
                root = null;
            }
            else
            {
                Node a = root.next;
                root = a;
                a.prev = null;
            }
        }

        // Remove End
        public void push()
        {
            if (root == null)
            {
                Console.WriteLine("Double Linked List is empty!");
            }
            else
            {
                removeEnd(root);
            }
        }

        public void removeEnd(Node node)
        {
            if (node.next != null)
            {
                removeEnd(node.next);
            }
            else
            {
                Node a = node.prev;
                a.next = null;
            }
        }

        // Remove Value
        public void removeValue(int value)
        {
            if (root == null)
            {
                Console.WriteLine("Double Linked List is empty!");
            }
            else if (root.data == value && root.next == null)
            {
                root = null;
            }
            else if (root.data != value && root.next == null)
            {
                Console.WriteLine("Double Linked List doesn't contain value!");
            }
            else if (root.data == value && root.next != null)
            {
                Node a = root.next;
                root = a;
                root.prev = null;
            }
            else
            {
                remove(root, value);
            }
        }

        public void remove(Node node, int value)
        {
            if (node.next.data == value)
            {
                if (node.next.next == null)
                {
                    node.next = null;
                }
                else
                {
                    Node a = node.next.next;
                    node.next = a;
                    a.prev = node;
                }
            }
            else
            {
                if (node.next.next != null)
                {
                    remove(node.next, value);
                }
                else
                {
                    Console.WriteLine("Double Linked List doesn't contain value!"); 
                }
            }
        }

        // Traverse
        public void traverse()
        {
            if (root == null)
            {
                Console.WriteLine("Double Linked List is empty!");
            }
            else
            {
                dlist.Add(root.data);

                if (root.next != null)
                {
                    traverseAll(root.next);
                }
            }
            foreach (int item in dlist)
            {
                Console.WriteLine(item);
            }
        }

        public void traverseAll(Node node)
        {
            dlist.Add(node.data);
            if (node.next != null)
            {
                traverseAll(node.next);
            }
        }
    }
}