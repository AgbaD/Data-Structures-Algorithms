using System;

namespace bst
{
    class Node
    {
        public int data;
        public Node leftChild;
        public Node rightChild;

        public Node(int adata)
        {
            data = adata;
            leftChild = null;
            rightChild = null;
        }
    }
}