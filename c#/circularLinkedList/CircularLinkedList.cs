using System;
using System.Collections.Generic;

namespace circularLinkedList
{
    class CircularLinkedList
    {
        public Node head;
        public List<int> list = new List<int>();
    	
        public CircularLinkedList()
        {
            head = null;
        }

    	// Insert Start
        public void prepend(int value)
        {
            Node a = new Node(value);
            if (head == null)
            {
                head = a;
            }
            else
            {
                if (head.next != null)
                {
                    
                } 
            }   
        }
    }
}