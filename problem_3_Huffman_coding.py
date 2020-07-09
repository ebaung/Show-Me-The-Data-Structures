#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sys
import queue
from collections import Counter

a_great_sentence = "The bird is the word"
    
ridiculous_text =  """Well everybody's heard about the bird !
        Bird bird bird, the bird is the word !
        [repeat]

        Everybody's heard about the bird !
        Bird bird bird, the bird is the word !
        [repeat]

        Don't you know about the bird?
        Well everybody's heard about the bird 
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Yeah !
        Well everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        Everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        Everybody's heard, about the bird !
        Everybody's heard, about the bird !
        Don't you know about the bird?
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Yeah!
        SURFIN' BIRD!!!!
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word !
        Well everybody's heard, about the bird !
        Yeah everybody's heard, about the bird !
        Everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        Don't you know about the bird?
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Go!!
        (Claps)Everybody's heard, about the bird !
        [Repeat 8 times]
        Yeah!!!Everybody's heard about the bird !
        Everybody's heard about ... bird !""" ; 

null_string = ""
non_string = 128
symbols = "~!@#$%^&*()_+{}|"
    
test_str = a_great_sentence
    
if type(test_str) != str:
    #type(test_str) != str
    print("Please enter a string (characters and symbols within quotes " ")")
    sys.exit()
elif len(test_str) < 1:
    print("You entered a blank. Please type at least one character.") 
    sys.exit()
else:
    print(test_str)

if __name__ == "__main__":
    codes = {}

#     a_great_sentence = "The bird is the word"
    
#     ridiculous_text =  """Well everybody's heard about the bird !
#     Bird bird bird, the bird is the word !
#     [repeat]

#     Everybody's heard about the bird !
#     Bird bird bird, the bird is the word !
#     [repeat]

#     Don't you know about the bird?
#     Well everybody's heard about the bird 
#     Bird bird bird, the bird is the word !
#     Bird bird bird, the bird is the word ! Yeah !
#     Well everybody's heard, about the bird !
#     Na-na-na-na-na-na-na-na-na
#     Na-na-na-na-na-na-na-na-na

#     Everybody's heard, about the bird !
#     Na-na-na-na-na-na-na-na-na
#     Na-na-na-na-na-na-na-na-na

#     Everybody's heard, about the bird !
#     Everybody's heard, about the bird !
#     Don't you know about the bird?
#     Well everybody's heard, about the bird !
#     Bird bird bird, the bird is the word !
#     Bird bird bird, the bird is the word ! Yeah!
#     SURFIN' BIRD!!!!
#     Well everybody's heard, about the bird !
#     Bird bird bird, the bird is the word !
#     Bird bird bird, the bird is the word !
#     Well everybody's heard, about the bird !
#     Yeah everybody's heard, about the bird !
#     Everybody's heard, about the bird !
#     Na-na-na-na-na-na-na-na-na
#     Na-na-na-na-na-na-na-na-na
#     Na-na-na-na-na-na-na-na-na

#     Don't you know about the bird?
#     Well everybody's heard, about the bird !
#     Bird bird bird, the bird is the word !
#     Bird bird bird, the bird is the word ! Go!!
#     (Claps)Everybody's heard, about the bird !
#     [Repeat 8 times]
#     Yeah!!!Everybody's heard about the bird !
#     Everybody's heard about ... bird !""" ; 

#     null_string = ""
#     non_string = 128
#     symbols = "~!@#$%^&*()_+{}|"
    
#     test_str = ridiculous_text
    
#     if test_str == " ":
#         print("You entered a blank. Please type at least one character.")
#         return
#     elif type(test_str) != str:
#     #type(test_str) != str
#         print("Please enter a string (characters and symbols within quotes " ")")
#         return
#     else:
#         print(test_str)

    def get_frequencies(test_str):
        # using dict and collections.Counter() to get  
        # count of each element in string as a dictionary
        #frequencies = dict(Counter(test_str.replace(" ","")))
        frequencies = dict(Counter(test_str))

        #convert dictionary frequencies pairs to tuples
        freq = [(v, k) for k, v in frequencies.items()]
        return frequencies, freq
        
    frequencies, freq = get_frequencies(test_str)
    #print(freq)

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_str)))
    print ("The content of the data is: {}\n".format(test_str))

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
    # print(node)

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
    
    #enable line below to print out letters, codes and frequencies
    for i in sorted(freq, reverse=True):
        print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])
        #print(i[1], '{}'.format(i[0]), code[i[1]])
    
    def assign_code(nodes, label, result, prefix = ''):    
        children = nodes[label]     
        tree = {}
        if len(children) == 2:
            tree['0'] = assign_code(nodes, children[0], result, prefix+'0')
            tree['1'] = assign_code(nodes, children[1], result, prefix+'1')     
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
        return code,tree
    
    vals = {l:v for (v,l) in freq}
    code, tree = Huffman_code(vals)

    text = test_str # text to encode
    encoded = ''.join([code[t] for t in text])
    #print('Encoded text:',encoded)

    def decode(encoded):
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

        #print('Decoded text:',''.join(decoded))
        decoded_text = ''.join(decoded)
        return decoded_text
    
    
    #code, tree = Huffman_code(a_great_sentence)
    code, tree = Huffman_code(vals)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded))

    decoded_text = decode(encoded)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_text)))
    print ("The content of the encoded[decoded] data is: {}\n".format(decoded_text))


# In[ ]:


#original test case
The bird is the word
The size of the data is: 69

The content of the data is: The bird is the word

    4.00 10
r   2.00 011
i   2.00 001
h   2.00 010
e   2.00 1101
d   2.00 1100
w   1.00 11101
t   1.00 11100
s   1.00 11111
o   1.00 11110
b   1.00 0001
T   1.00 0000
The size of the encoded data is: 36

The content of the encoded data is: 0110111011111100111000001010110000100011010011110111111010101011001010

The size of the decoded data is: 69

The content of the encoded[decoded] data is: The bird is the word


# In[ ]:


#Ludicrous test case (the whole Surfin Bird lyrics!)
Well everybody's heard about the bird !
        Bird bird bird, the bird is the word !
        [repeat]

        Everybody's heard about the bird !
        Bird bird bird, the bird is the word !
        [repeat]

        get_ipython().set_next_input("        Don't you know about the bird");get_ipython().run_line_magic('pinfo', 'bird')
        Well everybody's heard about the bird 
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Yeah !
        Well everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        Everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        Everybody's heard, about the bird !
        Everybody's heard, about the bird !
        get_ipython().set_next_input("        Don't you know about the bird");get_ipython().run_line_magic('pinfo', 'bird')
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Yeah!
        SURFIN' BIRD!!!!
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word !
        Well everybody's heard, about the bird !
        Yeah everybody's heard, about the bird !
        Everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        get_ipython().set_next_input("        Don't you know about the bird");get_ipython().run_line_magic('pinfo', 'bird')
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Go!!
        (Claps)Everybody's heard, about the bird !
        [Repeat 8 times]
        Yeah!!!Everybody's heard about the bird !
        Everybody's heard about ... bird !
The size of the data is: 1731

The content of the data is: Well everybody's heard about the bird !
        Bird bird bird, the bird is the word !
        [repeat]

        Everybody's heard about the bird !
        Bird bird bird, the bird is the word !
        [repeat]

        get_ipython().set_next_input("        Don't you know about the bird");get_ipython().run_line_magic('pinfo', 'bird')
        Well everybody's heard about the bird 
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Yeah !
        Well everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        Everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        Everybody's heard, about the bird !
        Everybody's heard, about the bird !
        get_ipython().set_next_input("        Don't you know about the bird");get_ipython().run_line_magic('pinfo', 'bird')
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Yeah!
        SURFIN' BIRD!!!!
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word !
        Well everybody's heard, about the bird !
        Yeah everybody's heard, about the bird !
        Everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        get_ipython().set_next_input("        Don't you know about the bird");get_ipython().run_line_magic('pinfo', 'bird')
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Go!!
        (Claps)Everybody's heard, about the bird !
        [Repeat 8 times]
        Yeah!!!Everybody's heard about the bird !
        Everybody's heard about ... bird !

  502.00 11
a 106.00 1000
r 103.00 0111
d 101.00 0101
e  96.00 0100
b  84.00 0010
i  70.00 0000
t  64.00 10110
n  62.00 10101
h  58.00 10100
-  56.00 10011
o  55.00 01101

  44.00 00111
get_ipython().system('  36.00 00011')
y  35.00 101111
s  28.00 100100
u  22.00 011000
21.00("001101")
'  20.00 001100
v  16.00 1011101
l  15.00 1011100
w  13.00 1001010
B  11.00 0001011
N   8.00 0001000
E   8.00 10010111
W   7.00 10010110
p   4.00 00010100
Y   4.00 00010010
D   4.00 011001111
k   3.00 011001011
]   3.00 011001010
[   3.00 011001001
R   3.00 011001110
?   3.00 011001101
.   3.00 011001000
I   2.00 000100111
m   1.00 0110011000
U   1.00 0001001101
S   1.00 0001001100
G   1.00 0001010111
F   1.00 0001010110
C   1.00 0001010101
8   1.00 0001010100
)   1.00 01100110011
(   1.00 01100110010
The size of the encoded data is: 932

The content of the encoded data is: 1001110101001001111100111111010010111010100011110111100100110101011011110011001001101110100010010000111010111100000100110101100010110111011010100010011001000000111010111000110011111111111111111110001011000001110101110010000001110101110010000001110101001101111011010100010011001000000111010111000010011011101101010001001101100110110101110101110001100111111111111111111101100100001110100101110001010010001011001100100100111001111111111111111111101110011011101010001111011110010011010101101111001100100110111010001001000011101011110000010011010110001011011101101010001001100100000011101011100011001111111111111111111000101100000111010111001000000111010111001000000111010100110111101101010001001100100000011101011100001001101110110101000100110110011011010111010111000110011111111111111111110110010000111010010111000101001000101100110010010011100111111111111111111100010010011011010100110010110111011110110101100011011001010101010110101100111110000010011010110001011011101101010001001100100000011101010110010110011111111111111111111001110101001001111100111111010010111010100011110111100100110101011011110011001001101110100010010000111010111100000100110101100010110111011010100010011001000000111010111001111111111111111111000101100000111010111001000000111010111001000000111010100110111101101010001001100100000011101011100001001101110110101000100110110011011010111010111000110011111111111111111110001011000001110101110010000001110101110010000001110101001101111011010100010011001000000111010111000010011011101101010001001101100110110101110101110001111000100110100100010100110001100111111111111111111110011101010010011111001111110100101110101000111101111001001101010110111100110010011011101000100100001110101001101111000001001101011000101101110110101000100110010000001110101110001100111111111111111111100010001000100101010110001001010101100010010101011000100101010110001001010101100010010101011000100101010110001001010101100000111111111111111111100010001000100101010110001001010101100010010101011000100101010110001001010101100010010101011000100101010110001001010101100000111001111111111111111111101110011011101010001111011110010011010101101111001100100110111010001001000011101010011011110000010011010110001011011101101010001001100100000011101011100011001111111111111111111000100010001001010101100010010101011000100101010110001001010101100010010101011000100101010110001001010101100010010101011000001111111111111111111000100010001001010101100010010101011000100101010110001001010101100010010101011000100101010110001001010101100010010101011000001110011111111111111111111011100110111010100011110111100100110101011011110011001001101110100010010000111010100110111100000100110101100010110111011010100010011001000000111010111000110011111111111111111111011100110111010100011110111100100110101011011110011001001101110100010010000111010100110111100000100110101100010110111011010100010011001000000111010111000110011111111111111111110001001001101101010011001011011101111011010110001101100101010101011010110011111000001001101011000101101110110101000100110010000001110101011001011001111111111111111111100111010100100111110011111101001011101010001111011110010011010101101111001100100110111010001001000011101010011011110000010011010110001011011101101010001001100100000011101011100011001111111111111111111000101100000111010111001000000111010111001000000111010100110111101101010001001100100000011101011100001001101110110101000100110110011011010111010111000110011111111111111111110001011000001110101110010000001110101110010000001110101001101111011010100010011001000000111010111000010011011101101010001001101100110110101110101110001111000100110100100010100000110011111111111111111110001010000000101000110011100000010100101011100001000100000110011000101110111000011001110000001001000011000110001100011001111111111111111111100111010100100111110011111101001011101010001111011110010011010101101111001100100110111010001001000011101010011011110000010011010110001011011101101010001001100100000011101011100011001111111111111111111000101100000111010111001000000111010111001000000111010100110111101101010001001100100000011101011100001001101110110101000100110110011011010111010111000110011111111111111111110001011000001110101110010000001110101110010000001110101001101111011010100010011001000000111010111000010011011101101010001001101100110110101110101110001100111111111111111111110011101010010011111001111110100101110101000111101111001001101010110111100110010011011101000100100001110101001101111000001001101011000101101110110101000100110010000001110101110001100111111111111111111100010011010010001010011010010111010100011110111100100110101011011110011001001101110100010010000111010100110111100000100110101100010110111011010100010011001000000111010111000110011111111111111111111011100110111010100011110111100100110101011011110011001001101110100010010000111010100110111100000100110101100010110111011010100010011001000000111010111000110011111111111111111110001000100010010101011000100101010110001001010101100010010101011000100101010110001001010101100010010101011000100101010110000011111111111111111110001000100010010101011000100101010110001001010101100010010101011000100101010110001001010101100010010101011000100101010110000011111111111111111110001000100010010101011000100101010110001001010101100010010101011000100101010110001001010101100010010101011000100101010110000011100111111111111111111100010010011011010100110010110111011110110101100011011001010101010110101100111110000010011010110001011011101101010001001100100000011101010110010110011111111111111111111001110101001001111100111111010010111010100011110111100100110101011011110011001001101110100010010000111010100110111100000100110101100010110111011010100010011001000000111010111000110011111111111111111110001011000001110101110010000001110101110010000001110101001101111011010100010011001000000111010111000010011011101101010001001101100110110101110101110001100111111111111111111100010110000011101011100100000011101011100100000011101010011011110110101000100110010000001110101110000100110111011010100010011011001101101011101011100011110001010011011010001100011001111111111111111111000101010000010101011001111100010111000110011000010101101011100110111010100011110111100100110101011011110011001001101110100010010000111010100110111100000100110101100010110111011010100010011001000000111010111000110011111111111111111110110010001001110000100101110001010010001011011000101011111101100000101110000001001001100110010010011111111111111111110001001101001000101000001100011000111011100110111010100011110111100100110101011011110011001001101110100010010000111010111100000100110101100010110111011010100010011001000000111010111000110011111111111111111111011100110111010100011110111100100110101011011110011001001101110100010010000111010111100000100110101100010110111001110011001110011001110011100100000011101011100011

The size of the decoded data is: 1731

The content of the encoded[decoded] data is: Well everybody's heard about the bird !
        Bird bird bird, the bird is the word !
        [repeat]

        Everybody's heard about the bird !
        Bird bird bird, the bird is the word !
        [repeat]

        get_ipython().set_next_input("        Don't you know about the bird");get_ipython().run_line_magic('pinfo', 'bird')
        Well everybody's heard about the bird 
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Yeah !
        Well everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        Everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        Everybody's heard, about the bird !
        Everybody's heard, about the bird !
        get_ipython().set_next_input("        Don't you know about the bird");get_ipython().run_line_magic('pinfo', 'bird')
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Yeah!
        SURFIN' BIRD!!!!
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word !
        Well everybody's heard, about the bird !
        Yeah everybody's heard, about the bird !
        Everybody's heard, about the bird !
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na
        Na-na-na-na-na-na-na-na-na

        get_ipython().set_next_input("        Don't you know about the bird");get_ipython().run_line_magic('pinfo', 'bird')
        Well everybody's heard, about the bird !
        Bird bird bird, the bird is the word !
        Bird bird bird, the bird is the word ! Go!!
        (Claps)Everybody's heard, about the bird !
        [Repeat 8 times]
        Yeah!!!Everybody's heard about the bird !
        Everybody's heard about ... bird !


# In[ ]:


#string = "" (Null string)
You entered a blank. Please type at least one character.


# In[ ]:


#integer (not string)
Please enter a string (characters and symbols within quotes )

