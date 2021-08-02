using System;

namespace linkedList
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            LinkedList lst = new LinkedList();

            lst.insertStart('8');
            foreach (string i in lst.traverse())
            {
                Console.WriteLine(i);
            }
        }
    }
}
