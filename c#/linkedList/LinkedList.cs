using System;
using  System.Collections.Generic;

namespace linkedList
{
    class LinkedList
    {
        public Node root;
        public List<int> llst = new List<int>();

        // Constructor
        public LinkedList()
        {
            root = null;
        }


        // Insert Start
        public void insertStart(int value)
        {
            Node a = new Node(value);
            if(root == null)
            {
                root = a;
            }
            else
            {
                Node b = root;
                root = a;
                root.next = b;
            }
        }

        // Insert End
        public void insertEnd(int value)
        {
            Node a = new Node(value);
            if (root == null)
            {
                root = a;
            }
            else
            {
                ise(root, a);
            }
        }

        public void ise(Node node, Node newnode)
        {
            if (node.next == null)
            {
                node.next = newnode;
            }
            else
            {
                ise(node.next, newnode);
            }
        }
        
        // Remove Start
        public void removeStart()
        {
            if (root == null)
            {
                Console.WriteLine("Linked List is empty");
            }
            else if (root.next == null)
            {
                root = null;
            }
            else
            {
                Node n = root.next;
                root = n;
            }
        }

        // Remove End
        public void removeEnd()
        {
            if (root == null)
            {
                Console.WriteLine("Linked List is empty");
            }
            else if (root.next == null)
            {
                root = null;
            }
            else
            {
                remove(root);
            }
        }

        public void remove(Node node)
        {
            if (node.next.next == null)
            {
                node.next = null;
            }
            else
            {
                remove(node.next);
            }
        }

        // Remove Value
        public void removeValue(int value)
        {
            if(root == null)
            {
                Console.WriteLine("Linked List is empty!");
            }
            else if (root.data == value && root.next == null)
            {
                root = null;
            }
            else if (root.data != value && root.next == null)
            {
                Console.WriteLine("Linked List does not contain value!");
            }
            else if (root.data == value && root.next != null)
            {
                Node temp = root.next;
                root = temp;
            }
            else
            {
                rm(root, value);
            }
        }

        public void rm(Node node, int value)
        {
            if (node.next.data == value)
            {
                if (node.next.next == null)
                {
                    node.next = null;
                }
                else
                {
                    Node temp = node.next.next;
                    node.next = temp;
                }
            }
            else
            {
                if (node.next.next != null)
                {
                    rm(node.next, value);
                }
                else
                {
                    Console.WriteLine("Linked list does not contain value!");
                }
            }
        }

        // Traverse
        public void traverse()
        {
            if(root == null)
            {
                Console.WriteLine("Linked List is empty!");
            }
            else
            {
                llst.Add(root.data);

                if(root.next != null)
                {
                    tra(root.next);
                }
            }
            foreach (int item in llst)
            {
                Console.WriteLine(item);
            }
        }

        public void tra(Node node)
        {
            llst.Add(node.data);
            if (node.next != null)
            {
                tra(node.next);
            }
        }
    }
}