using System;
using System.Collections.Generic;

namespace queues
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Queues");

            Queue queue = new Queue(7);

            Console.WriteLine(queue.isEmpty());
            Console.WriteLine(queue.isFull());
            Console.WriteLine("");
            queue.enqueue(5);
            queue.enqueue(7);

            queue.traverse();
            Console.WriteLine("");
            Console.WriteLine(queue.getSize());
            Console.WriteLine("");

            queue.enqueue(3);
            queue.enqueue(8);

            queue.traverse();
            Console.WriteLine("");

            int a = queue.dequeue();
            Console.WriteLine(queue.getSize());
            Console.WriteLine("");

            queue.traverse();
            Console.WriteLine("");

            queue.resize(3);
            Console.WriteLine(queue.getDefSize());

            queue.enqueue(99);

        }
    }
}
