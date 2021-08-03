using System;

namespace doubleLinkedList
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("We are Inside!");
            DLinkedList list = new DLinkedList();

            list.prepend(8);
            list.prepend(7);
            list.prepend(6);
            list.prepend(5);

            list.append(9);
            list.append(10);
            list.append(11);

            Console.WriteLine("...");
            Console.WriteLine("...");
            Console.WriteLine();

            list.pop();
            list.pop();

            list.push();

            list.removeValue(9);

            list.traverse();

        }
    }
}
