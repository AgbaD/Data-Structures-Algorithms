using System;

namespace tst
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Tenary Search Tree!");

            Tst t = new Tst();
            t.put("cat", 23);
            t.put("apple", 46);
            t.put("car", 6);
            t.put("cow", 112);

            int a = t.get("cow");
            if (a == -1)
            {
                Console.WriteLine("Key error!");
            }
            else
            {
                Console.WriteLine(a);
            }
            // Console.WriteLine(t.root.character);
        }
    }
}
