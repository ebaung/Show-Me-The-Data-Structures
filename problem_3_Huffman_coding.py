#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import queue
from collections import Counter

#freq = [(2,'t'), (2,'h'), (2,'e'), (1,'b'), (2,'i'), (2,'r'), (2,'d'), (1,'s'), (1,'w'), (1,'o')]
#freq = [(1,'T'), (1, 't'), (2,'h'), (2,'e'), (1,'b'), (2,'i'), (2,'r'), (2,'d'), (1,'s'), (1,'w'), (1,'o'), (4, " ")]

test_str = 'The bird is the word'

# using dict and collections.Counter() to get  
# count of each element in string as a dictionary
#frequencies = dict(Counter(test_str.replace(" ","")))
frequencies = dict(Counter(test_str))

#convert dictionary frequencies pairs to tuples
freq = [(v, k) for k, v in frequencies.items()]
print(freq)


class HuffmanNode(object):
    
    # Overwrite the equal to comparator
    def __eq__(self, other):
        #return self.value == other.value
        #return self == other
        return 0
        
    # Overwrite the less than comparator
    def __lt__(self, other):
        #return self.value < other.value
        #return self < other
        return 0

    # Overwrite the greater than comparator
    def __gt__(self, other):
        #return self.value > other.value
        #return self > other
        return 0
    
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root     # Why?  Not needed for anything.
    def children(self):
        return((self.left, self.right))

    def create_tree(frequencies):
        p = queue.PriorityQueue()
        for value in frequencies:    # 1. Create a leaf node for each symbol
            p.put(value)             #    and add it to the priority queue
        while p.qsize() > 1:         # 2. While there is more than one node
            l, r = p.get(), p.get()  # 2a. remove two highest nodes
            node = HuffmanNode(l,r) # 2b. create internal node with children
            p.put((l[0]+r[0], node)) # 2c. add new node to queue      
        return p.get()               # 3. tree is complete - return root node

node = HuffmanNode.create_tree(freq)
print(node)

# Recursively walk the tree down to the leaves,
#   assigning a code value to each symbol
def walk_tree(node, prefix="", code={}):
    if isinstance(node[1].left[1], HuffmanNode):
        walk_tree(node[1].left,prefix+"0", code)
    else:
        code[node[1].left[1]]=prefix+"0"
    if isinstance(node[1].right[1],HuffmanNode):
        walk_tree(node[1].right,prefix+"1", code)
    else:
        code[node[1].right[1]]=prefix+"1"
    return(code)


code = walk_tree(node)
for i in sorted(freq, reverse=True):
    print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])
    #print(i[1], '{}'.format(i[0]), code[i[1]])


# In[3]:


def assign_code(nodes, label, result, prefix = ''):    
    childs = nodes[label]     
    tree = {}
    if len(childs) == 2:
        tree['0'] = assign_code(nodes, childs[0], result, prefix+'0')
        tree['1'] = assign_code(nodes, childs[1], result, prefix+'1')     
        return tree
    else:
        result[label] = prefix
        return label

def Huffman_code(_vals):    
    vals = _vals.copy()
    nodes = {}
    for n in vals.keys(): # leafs initialization
        nodes[n] = []

    while len(vals) > 1: # binary tree creation
        s_vals = sorted(vals.items(), key=lambda x:x[1]) 
        a1 = s_vals[0][0]
        a2 = s_vals[1][0]
        vals[a1+a2] = vals.pop(a1) + vals.pop(a2)
        nodes[a1+a2] = [a1, a2]        
    code = {}
    root = a1+a2
    tree = {}
    tree = assign_code(nodes, root, code)   # assignment of the code for the given binary tree      
    return code, tree


# In[4]:


vals = {l:v for (v,l) in freq}
code, tree = Huffman_code(vals)

text = 'The bird is the word' # text to encode
encoded = ''.join([code[t] for t in text])
print('Encoded text:',encoded)

decoded = []
i = 0
while i < len(encoded): # decoding using the binary graph
    ch = encoded[i]  
    act = tree[ch]
    while not isinstance(act, str):
        i += 1
        ch = encoded[i]  
        act = act[ch]        
    decoded.append(act)          
    i += 1

print('Decoded text:',''.join(decoded))


# In[7]:


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    #code, tree = Huffman_code(a_great_sentence)
    code, tree = Huffman_code(vals)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(code, base=2))))
    print ("The content of the encoded data is: {}\n".format(code))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


# In[ ]:


#from graphviz import Digraph


# In[ ]:


#dot = Digraph()


# In[7]:


import graphviz


# In[8]:


def draw_tree(tree, prefix = ''):    
    if isinstance(tree, str):            
        descr = 'N%s [label="%s:%s", fontcolor=blue, fontsize=16, width=2, shape=box];\n'%(prefix, tree, prefix)
    else: # Node description
        descr = 'N%s [label="%s"];\n'%(prefix, prefix)
        for child in tree.keys():
            descr += draw_tree(tree[child], prefix = prefix+child)
            descr += 'N%s -> N%s;\n'%(prefix,prefix+child)
    return descr

import subprocess
with open('graph.dot','w') as f:
    f.write('digraph G {\n')
    f.write(draw_tree(tree))
    f.write('}') 
subprocess.call('dot -Tpng graph.dot -o graph.png', shell=True)


# In[ ]:


get_ipython().system('python problem_3_scratchpad.py')

