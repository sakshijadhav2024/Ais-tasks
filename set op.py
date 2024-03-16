#!/usr/bin/env python
# coding: utf-8

# In[1]:


s={1,"sakshi",2,"vedant",3,4,"manisha",}


# In[2]:


s


# In[3]:


s.add("Pramod")


# In[4]:


s


# In[5]:


s1={44,55,66,22,11}


# In[6]:


s


# In[7]:


s1


# In[9]:


d=s.difference(s1)


# In[10]:


d


# In[11]:


d1=s1.difference_update(s)
print(d1)


# In[13]:


s1.discard(44)


# In[14]:


s1


# In[17]:


p=s.intersection(d)
p


# In[21]:


a=s.isdisjoint(s1)


# In[22]:


a


# In[25]:


p.union(d)


# In[ ]:




