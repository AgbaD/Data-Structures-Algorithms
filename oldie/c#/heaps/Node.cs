using System;
using System.Collections.Generic;

namespace heaps
{
    class Node
    {
        public int data;
        public Node left;
        public Node right;
        public Node parent;

        public Node(int adata)
        {
            data = adata;
            parent = null;
            left = null;
            right = null;
        } 
    }
}