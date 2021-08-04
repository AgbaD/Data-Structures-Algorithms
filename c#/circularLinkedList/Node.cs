namespace circularLinkedList
{
    class Node
    {
        public int data;
        public Node next;
        public Node prev;

        public Node(int adata)
        {
            data = adata;
            next = null;
            prev = null;
        }
    }
}