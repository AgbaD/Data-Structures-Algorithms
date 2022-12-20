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

        // get root
        public int getRoot()
        {
            return root.data;
        }

        // delete
        public void delete(int value)
        {
            if (root == null)
            {
                Console.WriteLine("Binary Search Tree is empty!");
            }
            else if (root.data == value)
            {
                if (root.rightChild == null)
                {
                    if (root.leftChild == null)
                    {
                        root = null;
                    }
                    else
                    {
                        root = root.leftChild;
                    }
                }
                else {
                    if (root.leftChild == null)
                    {
                        root = root.rightChild;
                    }
                    else
                    {
                        Node temp = root.rightChild;
                        root = root.leftChild;
                        insertNode(root, temp);
                    }
                }
            }
            else
            {
                deleteNode(root, value);
            }
        }

        public void deleteNode(Node node, int value)
        {
            if (value < node.data)
            {
                if (node.leftChild.data == value)
                {
                    if (node.leftChild.rightChild == null)
                    {
                        if (node.leftChild.leftChild == null)
                        {
                            node.leftChild = null;
                        }
                        else
                        {
                            node.leftChild = node.leftChild.leftChild;
                        }
                    }
                    else {
                        if (node.leftChild.leftChild == null)
                        {
                            node.leftChild = node.leftChild.rightChild;
                        }
                        else
                        {
                            Node temp = node.leftChild.rightChild;
                            node.leftChild = node.leftChild.leftChild;
                            insertNode(node.leftChild, temp);
                        }
                    }
                }
                else
                {
                    deleteNode(node.leftChild, value);
                }
            }
            else
            {
                if (node.rightChild.data == value)
                {
                    if (node.rightChild.rightChild == null)
                    {
                        if (node.rightChild.leftChild == null)
                        {
                            node.rightChild = null;
                        }
                        else
                        {
                            node.rightChild = node.rightChild.leftChild;
                        }
                    }
                    else
                    {
                        if (node.rightChild.leftChild == null)
                        {
                            node.rightChild = node.rightChild.rightChild;

                        }
                        else
                        {
                            Node temp = node.rightChild.rightChild;
                            node.rightChild = node.rightChild.leftChild;
                            insertNode(node.rightChild, temp);
                        }
                    }
                }
                else
                {
                    deleteNode(node.rightChild, value);
                }
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