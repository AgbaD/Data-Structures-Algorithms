using System;
using System.Linq;

namespace linkedList
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("We are Inside!");
            LinkedList lst = new LinkedList();

            // lst.traverse();

            lst.insertStart(8);
            lst.insertStart(7);
            lst.insertStart(6);
            lst.insertStart(5);

            lst.insertEnd(9);
            lst.insertEnd(10);
            lst.insertEnd(11);

            lst.removeEnd();
            lst.removeStart();

            lst.removeValue(13);
            lst.removeValue(10);


            lst.traverse();

            // foreach (int item in lst.llst)
            // {
            //     Console.WriteLine(item);
            // }
        }
    }
}
