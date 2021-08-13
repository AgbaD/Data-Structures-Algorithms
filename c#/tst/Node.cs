using System;

namespace tst
{
    class Node
    {
        public char character;
        public int value;
        public Node left;
        public Node right;
        public Node middle;

        public Node(char acharacter)
        {
            character = acharacter;
            left = null;
            right = null;
            middle = null;
        }
        
    }
}