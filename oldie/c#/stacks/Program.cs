using System;
using System.Collections.Generic;

namespace stacks
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Stacks");

            Stack stack = new Stack(7);

            Console.WriteLine(stack.isEmpty());
            Console.WriteLine(stack.isFull());
            Console.WriteLine("");
            stack.add(5);
            stack.add(7);

            stack.traverse();
            Console.WriteLine("");
            Console.WriteLine(stack.getSize());
            Console.WriteLine("");

            stack.add(3);
            stack.add(8);

            stack.traverse();
            Console.WriteLine("");

            int a = stack.remove();
            Console.WriteLine(a);
            Console.WriteLine(stack.getSize());
            Console.WriteLine("");

            stack.traverse();
            Console.WriteLine("");

            stack.resize(3);
            Console.WriteLine(stack.getDefSize());

            stack.add(99);

        }
    }
}
