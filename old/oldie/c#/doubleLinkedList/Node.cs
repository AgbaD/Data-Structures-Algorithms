namespace doubleLinkedList
{
    class Node
    {
        public int data;
        public Node prev;
        public Node next;

        public Node(int adata)
        {
            data = adata;
            prev = null;
            next = null;
        }
    }
}