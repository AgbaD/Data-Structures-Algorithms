using System;
using System.Collections.Generic;

namespace bst
{
    class Bst
    {
        public Node root;
        public List<int> tree;

        public Bst()
        {
            root  = null;
        }

        // insert
        public void insert(int data)
        {
            Node temp = new Node(data);
            if (root == null)
            {
                root = temp;
            }
            else
            {
                if (root.data < data)
                {
                    if (root.rightChild != null)
                    {
                        insertNode(root.rightChild, temp);
                    }
                    else
                    {
                        root.rightChild = temp;
                    }
                }
                else if (root.data > data)
                {
                    if (root.leftChild != null)
                    {
                        insertNode(root.leftChild, temp);
                    }
                    else
                    {
                        root.leftChild = temp;
                    }
                }
                else
                {
                    Console.WriteLine("Value already present in binary search tree!");
                }
            }
        }

        public void insertNode(Node node, Node newnode)
        {
            if (newnode.data > node.data)
            {
                if (node.rightChild == null)
                {
                    node.rightChild = newnode;
                }
                else
                {
                    insertNode(node.rightChild, newnode);
                }
            }
            else if (newnode.data < node.data)
            {
                if (node.leftChild == null)
                {
                    node.leftChild = newnode;
                }
                else
                {
                    insertNode(node.leftChild, newnode);
                }
            }
            else {
                Console.WriteLine("Value already present in binary search tree!");
            }
        }

        // get minimum
        public int getMin()
        {
            if (root == null)
            {
                Console.WriteLine("Binary search tree is empty!");
                return 0;
            }
            else
            {
                return getMinimun(root);
            }
        }

        public int getMinimun(Node node)
        {
            if (node.leftChild != null)
            {
                return getMinimun(node.leftChild);
            }
            else
            {
                return node.data;
            }
        }

        // get maximum
        public int getMax()
        {
            if (root == null)
            {
                Console.WriteLine("Binary search tree is empty!");
                return 0;
            }
            else
            {
                return getMaximum(root);
            }
        }

        public int getMaximum(Node node)
        {
            if (node.rightChild != null)
            {
                return getMaximum(node.rightChild);
            }
            else
            {
                return node.data;
            }
        }
        // traverse
        public void traverse()
        {
            tree  = new List<int>();
            if (root == null)
            {
                Console.WriteLine("Binary search tree is empty!");
            }
            else
            {
                traverseTree(root);
            }
            foreach (int item in tree)
            {
                Console.WriteLine(item);
            }
        }

        public void traverseTree(Node node)
        {
            if (node.leftChild != null)
            {
                traverseTree(node.leftChild);
            }

            tree.Add(node.data);

            if (node.rightChild != null)
            {
                traverseTree(node.rightChild);
            }
        }
        // search
    }
}