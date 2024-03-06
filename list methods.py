#!/usr/bin/env python
# coding: utf-8

# # List Methods

# In[45]:


l=['sakshi','karad',22,45.2,'pune']
l


# #append

# In[46]:


l.append('satara')
l


# #count()

# In[47]:


print(l.count('karad'))


# #extend

# In[48]:


l1=['book',89,'pen']
l1


# In[49]:


print(l)


# In[50]:


l.extend(l1)


# In[51]:


print(l)


# #index

# In[52]:


print(l.index('pune'))


# #insert

# In[56]:


l.insert(3,99)
l


# #pop

# In[57]:


l.pop(2)
l


# #remove

# In[58]:


l.remove('sakshi')
l


# #reverse

# In[59]:


l.reverse()
l


# #sort

# In[60]:


l2=[2,88,65,34]
l2.sort()
l2


# In[63]:


l2.sort(reverse=True)
l2


# #clear()

# In[4]:


l.clear()
l


# #copy()

# In[8]:


l1=l.copy()
l1


# In[ ]:




