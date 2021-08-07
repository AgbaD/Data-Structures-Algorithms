using System;
using System.Collections.Generic;

namespace queues
{
    class Queue
    {
        // Queue can not contain zero value
        public List<int> queue = new List<int>();
        public int def_size; // default size
        public int cur_size = 0;

        public Queue(int asize)
        {
            def_size = asize;
            for (int i = 0; i < def_size; i++)
            {
                queue.Add(0);
            }
        }

        // Add to queue
        public void enqueue(int data)
        {
            if (cur_size >= def_size)
            {
                Console.WriteLine("Current Queue is full. Please dequeue or resize!");
            }
            else
            {
                if (data == 0)
                {
                    Console.WriteLine("Can not add zero value to queue");   
                }
                else
                {
                    queue.Insert(cur_size, data);
                    cur_size++;
                }
            }
        }

        // Remove from queue
        public int dequeue()
        {   
            if (queue[0] == 0)
            {
                Console.WriteLine("The queue is empty!");
                return 0;
            }
            else
            {
                int val = queue[0];
                queue.RemoveAt(0);
                queue.Add(0);
                cur_size--;
                return val;
            }
            // int ind = cur_size - 1;
            // int val = queue[ind];
            // queue[ind] = null;
        }

        // get size
        public int getSize()
        {
            return cur_size;
        }

        public int getDefSize()
        {
            return def_size;
        }

        // Resize
        public void resize(int size)
        {
            if (size < cur_size)
            {
                Console.WriteLine("Current queue size is greater that new size");
            }
            else
            {
                if (size < def_size)
                {
                    // and new size = 5
                    int diff = def_size - size;
                    for (int i=0; i < diff; i++);
                    {
                        queue.RemoveAt(queue.Count - 1);
                    }
                    def_size = size;
                }
                else if (size == def_size)
                {
                    Console.WriteLine("Current size equals new size");
                }
                else 
                {
                    int diff = size - def_size;
                    for (int i=0; i < diff; i++)
                    {
                        queue.Add(0);
                    }
                }
            }
        }

        // is full
        public bool isFull()
        {
            if (cur_size == def_size)
            {
                return true;
            }
            return false;
        }

        // is empty
        public bool isEmpty()
        {
            if (cur_size == 0)
            {
                return true;
            }
            return false;
        }

        // traverse
        public void traverse()
        {
            if (cur_size == 0)
            {
                Console.WriteLine("Current queue is empty!");
            }
            else
            {
                for (int i=0; i < cur_size; i++)
                {
                    Console.WriteLine(queue[i]);
                }
            }
        }
    }
}