using System;

namespace linkedList
{
    class Node
    {
        public string data;
        public Node? next;

        public Node(char data)
        {
            data = data;
            next = null;
        }
    }
}