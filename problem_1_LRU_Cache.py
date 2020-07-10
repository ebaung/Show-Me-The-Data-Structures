#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import OrderedDict


# In[2]:


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity
    
    #get query for the key value below costs time complexity O(1)
    def get(self, key):
            # Retrieve item from provided key. Return -1 if nonexistent. 
            if key not in self.cache:
                return -1
            # move key to the end to indicate that it was recently used
            else:
                self.cache.move_to_end(key)
                return self.cache[key]
        
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        self.cache[key] = value
        # move key to end to indicate it was recently used
        self.cache.move_to_end(key)
        # if length of ordered dictionary is over capacity..
        if len(self.cache) > self.capacity:
            #...then remove the first key (least recently used key)
            self.cache.popitem(last = False)


# In[3]:


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.get(1)       # returns 1


# In[4]:


our_cache.get(2)       # returns 2


# In[5]:


our_cache.get(9)      # returns -1 because 9 is not present in the cache


# In[6]:


our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

