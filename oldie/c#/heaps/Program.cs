using System;

namespace heaps
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Heaps");

            Heap a = new Heap();
            a.add(5);
            a.add(7);
            a.add(3);

            int b = a.remove();
            Console.WriteLine(b);
        }
    }
}
