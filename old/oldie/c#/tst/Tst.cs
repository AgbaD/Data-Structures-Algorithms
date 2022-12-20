using System;
using System.Collections.Generic;
using System.Linq;

namespace tst
{
    class Tst
    {
        // negative values are not allowed
        public Node root;
        public Node pointer;
        public string alpha;

        public Tst()
        {
            root = null;
            pointer = null;
            alpha = "abcdefghijklmnopqrstuvwxyz";
        }

        // insertion
        public void put(string word, int value)
        {
            if (root == null)
            {
                int ind = 0;
                root = new Node(word[ind]);
                pointer = root;
                int last = word.Length - 1;
                for (int i=ind+1; i < word.Length; i++)
                {
                    if (i == last)
                    {
                        Node temp = new Node(word[i]);
                        temp.value = value;
                        pointer.middle = temp;
                    }
                    else
                    {
                        Node temp = new Node(word[i]);
                        pointer.middle = temp;
                        pointer = pointer.middle;
                    }
                }
            }
            else
            {
                pointer = root;
                int ind = 0;
                while (true)
                {
                    int pointer_ind = alpha.IndexOf(pointer.character);
                    int word_ind = alpha.IndexOf(word[ind]);

                    if (word_ind < pointer_ind)
                    {
                        if (pointer.left == null)
                        {
                            if (word.Length > ind+1)
                            {
                                pointer.left = new Node(word[ind]);
                                pointer = pointer.left;
                                int last = word.Length - 1;
                                for (int i=ind+1; i < word.Length; i++)
                                {
                                    if (i == last)
                                    {
                                        Node temp = new Node(word[i]);
                                        temp.value = value;
                                        pointer.middle = temp;
                                    }
                                    else
                                    {
                                        Node temp = new Node(word[i]);
                                        pointer.middle = temp;
                                        pointer = pointer.middle;
                                    }
                                }
                            }
                            else
                            {
                                pointer.left = new Node(word[ind]);
                                pointer.left.value = value;
                            }
                            break;
                        }
                        else
                        {
                            pointer = pointer.left;
                        }
                    }
                    else if (word_ind > pointer_ind)
                    {
                        if (pointer.right == null)
                        {
                            if (word.Length > ind+1)
                            {
                                pointer.right = new Node(word[ind]);
                                pointer = pointer.right;
                                int last = word.Length - 1;
                                for (int i=ind+1; i < word.Length; i++)
                                {
                                    if (i == last)
                                    {
                                        Node temp = new Node(word[i]);
                                        temp.value = value;
                                        pointer.middle = temp;
                                    }
                                    else
                                    {
                                        Node temp = new Node(word[i]);
                                        pointer.middle = temp;
                                        pointer = pointer.middle;
                                    }
                                }
                            }
                            else
                            {
                                pointer.right = new Node(word[ind]);
                                pointer.right.value = value;
                            }
                            break;
                        }
                        else
                        {
                            pointer = pointer.right;
                        }
                    }
                    else // word_ind == pointer_ind
                    {
                        pointer = pointer.middle;
                        ind++;
                    }
                }
            }
        }

        // Removal
        public int get(string key)
        {
            
            pointer = root;
            int ind = 0;
            int last = key.Length - 1;
            while (true)
            {
                int pointer_ind = alpha.IndexOf(pointer.character);
                int key_ind = alpha.IndexOf(key[ind]);

                if (key_ind < pointer_ind)
                {
                    if (pointer.left != null)
                    {
                        pointer = pointer.left;
                    }
                    else
                    {
                        break;
                    }
                }
                else if (key_ind > pointer_ind)
                {
                    if (pointer.right != null)
                    {
                        pointer = pointer.right;
                    }
                    else
                    {
                        break;
                    }
                }
                else // key_ind == pointer_ind
                {
                    if (ind == last)
                    {
                        try
                        {
                            return pointer.value;
                        }
                        catch (System.Exception)
                        {
                            break;
                            throw;
                        }
                    }
                    if (pointer.middle != null)
                    {
                        pointer = pointer.middle;
                        ind++;
                    }
                    else
                    {
                        break;
                    }
                }
            }
            return -1;
        }
    }
}