using System;
using System.Collections.Generic;

namespace stacks
{
    class Stack
    {
        public List<int> stack = new List<int>();
        public int def_size;
        public int cur_size = 0;

        public Stack(int asize)
        {
            def_size = asize;
            for (int i = 0; i < def_size; i++)
            {
                stack.Add(0);
            }
        }

        public void add(int value)
        {
            if (cur_size >= def_size)
            {
                Console.WriteLine("Current Stack is full. Please remove or resize!");
            }
            else
            {
                if (value == 0)
                {
                    Console.WriteLine("Can not add zero value to stack");   
                }
                else
                {
                    stack.Insert(cur_size, value);
                    cur_size++;
                }
            }
        }

        public int remove()
        {
            if (cur_size == 0)
            {
                Console.WriteLine("Current Stack is empty. Please add");
                return 0;
            }
            else
            {
                int val = stack[cur_size - 1];
                stack.RemoveAt(cur_size - 1);
                stack.Add(0);
                cur_size--;
                return val;
            }
        }

        // get size
        public int getSize()
        {
            return cur_size;
        }

        // get default size
        public int getDefSize()
        {
            return def_size;
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

        // resize
        public void resize(int size)
        {
            if (size < cur_size)
            {
                Console.WriteLine("Current stack size is greater than new size");
            }
            else
            {
                if (size < def_size)
                {
                    // and new size = 5
                    int diff = def_size - size;
                    for (int i=0; i < diff; i++);
                    {
                        stack.RemoveAt(stack.Count - 1);
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
                        stack.Add(0);
                    }
                    def_size = size;
                }
            }
        }

        // traverse
        public void traverse()
        {
            if (cur_size == 0)
            {
                Console.WriteLine("Current stack is empty!");
            }
            else
            {
                for (int i=1; i <= cur_size; i++)
                {
                    Console.WriteLine(stack[cur_size - i]);
                }
            }
        }
    }
}