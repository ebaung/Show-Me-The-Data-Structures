#!/usr/bin/env python
# coding: utf-8

# In[13]:


import sys
import queue
from collections import Counter

a_great_sentence = "the bird is the word"
next_verse = "Uma mao mao"

class HuffmanNode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root     # Why?  Not needed for anything.
    def children(self):
        return((self.left, self.right))

#freq = [(7, 'A'), (3, 'B'), (7, 'C'), (2, 'D'), (6, 'E')] 
#freq = {7:'A', 3:'B', 7:'C', 2:'D', 6:'E'}
test_str = a_great_sentence

# using collections.Counter() to get  
# count of each element in string  
res = dict(Counter(test_str.replace(" ","")))

# printing result  
print ("Unique characters count of all characters in '" + test_str + "' is :\n " +  str(res)) 
    
def huffman_encoding(frequencies):
    p = queue.PriorityQueue()
    for value in frequencies:    # 1. Create a leaf node for each symbol
        p.put(value)             #    and add it to the priority queue
    while p.qsize() > 1:         # 2. While there is more than one node
        l, r = p.get(), p.get()  # 2a. remove two highest nodes
        node = HuffmanNode(l, r) # 2b. create internal node with children
        p.put((l[0]+r[0], node)) # 2c. add new node to queue      
    return p.get()               # 3. tree is complete - return root node


def huffman_decoding(data,tree):
    return(code)

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


# In[ ]:


node = create_tree(data)
print(node)


# In[ ]:


# Recursively walk the tree down to the leaves,
#   assigning a code value to each symbol
def walk_tree(node, prefix="", code={}):
    return(code)

code = walk_tree(node)
for i in sorted(freq, reverse=True):
    print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])

