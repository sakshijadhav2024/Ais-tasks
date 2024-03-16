#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


dataf1=pd.DataFrame( {'Name': ['sakshi','Anuja','Arpita','Snehal'],
                   'Marks': [78,98,56,25],
                   'Grade': ['B','A','C','D']})
dataf1


# In[8]:


dataf2=pd.DataFrame( {'Name': ['Sharvi','Ovi'],
                   'Marks': [69,99],
                   'Grade': ['c','A']})
dataf2


# In[9]:


dataf3=pd.DataFrame( {'Name': ['purva','Om'],
                   'Marks': [96,33],
                   'Grade': ['A','E'],
                     'Remark':['pass','fail']})
dataf3


# In[10]:


con=pd.concat([dataf1,dataf2],axis=0)
con


# In[12]:


con=pd.concat([dataf1,dataf2],axis=1)
con


# In[13]:


con=pd.concat([dataf1,dataf2,dataf3],axis=0)
con


# In[14]:


con=pd.concat([dataf1,dataf2,dataf3],axis=1)
con


# In[20]:


newdf1= pd.DataFrame({
    'rollno': [101, 102,103, 104],
    'student': ['Amrita', 'Shruti', 'Priya', 'Shrushti']
})
newdf1


# In[21]:


newdf2= pd.DataFrame({
    'rollno': [101, 106,103, 104],
    'student': ['Puja', 'Smita', 'Nidhi', 'Riya']
})
newdf2


# In[23]:


mdf = pd.merge(newdf1, newdf2, on='rollno', how='inner')
mdf


# In[24]:


mdf = pd.merge(newdf1, newdf2, on='rollno', how='outer')
mdf


# In[ ]:




