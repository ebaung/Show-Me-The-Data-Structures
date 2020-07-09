#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


# In[2]:


#Write a function that provides an efficient look up of whether the user is in a group.
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()
    if user in users:
        return True
    else:
        #now recurse through the group's groups
        group_hierarchy = group.get_groups()
        for item in group_hierarchy:
            return is_user_in_group(user, item)
    return False


# In[3]:


#default Udacity test case
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


# In[4]:


# TEST CASE 1: default Udacity test case
#expect True
is_user_in_group("sub_child_user", parent)


# In[5]:


#default Udacity test case
#expect True
is_user_in_group("sub_child_user", child)


# In[6]:


#default Udacity test case
#expect True
is_user_in_group("sub_child_user", sub_child)


# In[7]:


# TEST CASE 2: testing user that doesn't exist
#expect False
is_user_in_group("Weird_Al_Yankovich", sub_child)


# In[8]:


#expect False
is_user_in_group("Weird_Al_Yankovich", child)


# In[9]:


#expect False
is_user_in_group("Weird_Al_Yankovich", parent)


# In[10]:


# TEST CASE 3: Users in different groups in the hierarchy
# expect 
# usr1: True, False, False
# usr2: True, True, False
# usr3: True, True, True
Administrators = Group("Administrators")
Server_Administrators = Group("Server Administrators")
Backup_Administrators = Group("Backup Administrators")

Administrators.add_group(Server_Administrators)
Server_Administrators.add_group(Backup_Administrators)

usr1 = "Charlie Chaplin"
usr2 = "Ernest Hemingway"
usr3 = "Donald Trump"

Administrators.add_user(usr1)
Server_Administrators.add_user(usr2)
Backup_Administrators.add_user(usr3)


# In[27]:


# usr1: True, False, False
print(is_user_in_group("Charlie Chaplin", Administrators))
print(is_user_in_group("Charlie Chaplin", Server_Administrators))
print(is_user_in_group("Charlie Chaplin", Backup_Administrators))


# In[28]:


# usr2: True, True, False
print(is_user_in_group("Ernest Hemingway", Administrators))
print(is_user_in_group("Ernest Hemingway", Server_Administrators))
print(is_user_in_group("Ernest Hemingway", Backup_Administrators))


# In[29]:


# usr3: True, True, True
print(is_user_in_group("Donald Trump", Administrators))
print(is_user_in_group("Donald Trump", Server_Administrators))
print(is_user_in_group("Donald Trump", Backup_Administrators))

