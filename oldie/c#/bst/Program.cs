using System;

namespace bst
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Binary Search Tree");

            Bst bst = new Bst();

            bst.traverse();
            Console.WriteLine("");

            bst.insert(3);
            bst.insert(2);

            
            bst.traverse();
            Console.WriteLine("");

            bst.insert(2);
            bst.insert(5);

            bst.traverse();
            Console.WriteLine("");

            Console.WriteLine(bst.getMin());
            Console.WriteLine("");
            Console.WriteLine(bst.getMax());
            Console.WriteLine("");

            bst.traverse();
            Console.WriteLine("");

            bst.delete(3);
            Console.WriteLine(bst.getRoot());
            Console.WriteLine("");
            bst.traverse();
            Console.WriteLine("");
        }
    }
}
