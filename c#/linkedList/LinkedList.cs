using System;
using  System.Collections.Generic;

namespace linkedList
{
    class LinkedList
    {
        public Node root;
        public List<string> llst = new List<string>();

        // Constructor
        public LinkedList()
        {
            root = null;
        }


        // InsertStart
        public void insertStart(char value)
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

        // Traverse
        public List<string> traverse()
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
                    tra(llst, root.next);
                }
            }

            return llst;
        }

        public void tra(List<string> list, Node node)
        {
            llst.Add(node.data);
            if (node.next != null)
            {
                tra(llst, node.next);
            }
        }
    }
}