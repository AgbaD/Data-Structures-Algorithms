using System;
using System.Collections.Generic;

namespace heaps
{
    class Heap
    {
        public Node root;
        public Node pointer;
        public int count;

        public Heap ()
        {
            root = null;
            count = 0;

        }

        // Add
        public void add(int value)
        {
            Node temp = new Node(value);
            if (root == null)
            {
                root = temp;
                count++;
            }               
            else
            {
                pointer = root;
                // convert count to binary
                string bitcount = Convert.ToString(count + 1, 2);
                int i;
                for (i=1; i < bitcount.Length; i++)
                {
                    if (bitcount[i] == '0')
                    {
                        if (pointer.left == null)
                        {
                            pointer.left = temp;
                            pointer.left.parent = pointer;
                        }
                        pointer = pointer.left;
                    }
                    else
                    {
                        if (pointer.right == null)
                        {
                            pointer.right = temp;
                            pointer.right.parent = pointer;
                        }
                        pointer = pointer.right;
                    }
                }
                while (true)
                {
                    if (pointer == root)
                    {
                        break;
                    }
                    if (pointer.data < pointer.parent.data)
                    {
                        int a = pointer.data;
                        pointer.data = pointer.parent.data;
                        pointer.parent.data = a;
                        pointer = pointer.parent;
                    }
                    else {
                        break;
                    }
                }
                count++;
            } 
        }

        // Remove root
        public int remove()
        {
            int value = root.data;
            pointer = root;
            string bitcount = Convert.ToString(count, 2);
            for (int i=1; i < bitcount.Length; i++)
            {
                if (bitcount[i] == '0')
                {
                    pointer = pointer.left;
                }
                else
                {
                    pointer = pointer.right;
                }
            }
            root.data = pointer.data;
            try
            {
                if (pointer.parent.left == pointer)
                {
                    pointer.parent.left  = null;
                }
                else
                {
                    pointer.parent.right = null;
                }
                count--;
                heapify();
            }
            catch (System.Exception)
            {
                root = null;
            }
            return value;
        }

        // Heapify
        public void heapify()
        {
            pointer = root;
            Node compare;
            while (true)
            {
                if (pointer.left == null)
                {
                    if (pointer.right == null)
                    {
                        break;
                    }
                    else
                    {
                        if (pointer.right.data < pointer.data)
                        {
                            int t = pointer.data;
                            pointer.data = pointer.right.data;
                            pointer.right.data = t;
                            pointer = pointer.right;
                        }
                        else
                        {
                            break;
                        }
                    }
                } 
                else
                {
                    if (pointer.right == null)
                    {
                        if (pointer.left.data < pointer.data)
                        {
                            int t = pointer.data;
                            pointer.data = pointer.left.data;
                            pointer.left.data = t;
                            pointer = pointer.left
                        }
                        else
                        {
                            break;
                        }
                    }
                    else
                    {
                        if (pointer.left.data <= pointer.right.data)
                        {
                            compare = pointer.left;
                        }
                        else
                        {
                            compare = pointer.right
                        }

                        if (compare.data < pointer.data)
                        {
                            int t = pointer.data;
                            pointer.data = compare.data;
                            compare.data = t;
                            pointer = compare;
                        }
                        else
                        {
                            break;
                        }
                    }
                }
            }
        }
    }
}