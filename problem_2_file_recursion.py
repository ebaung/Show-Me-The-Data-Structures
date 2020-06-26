#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


#dirname = 'C:\\Users\\DeepThought\\Sync\\Udacity\\School of AI\\01 Data structures and algorithms\\02 Data Structures\\Project 2 Show Me the Data Structures\\testdir'
root_dir = os.getcwd()
dirname = os.path.join(root_dir,"testdir")


# In[3]:


def find_files(suffix = '.c', path = dirname):
    for name in os.listdir(path):
        path2 = os.path.join(path, name)
        if os.path.isdir(path2):
            for file in os.listdir(path2):
                if file.endswith(suffix):
                    print(os.path.join(path2, file))
                
            find_files(suffix, path2)
        


# In[4]:


find_files()
# expect output to use default values and give full paths to files:
# subdir1\a.c, subcdir3\subsubdir1\b.c, and subdir5\a.c


# In[5]:


find_files('.c', dirname)
# expect output to give full paths to files subdir1\a.c, subcdir3\subsubdir1\b.c, and subdir5\a.c


# In[8]:


find_files(None, None)
#expect an error stating wrong value type

