#!/usr/bin/env python
# coding: utf-8

# Dictonary operations
# 

# In[1]:


dict={"Name":"sakshi ","Age":"21","place":"karad"}
dict


# In[2]:


d={"Name":["sakshi","puja","snehal"],"Age":[55,27,32],"qualification":["BSC","MCA","Ba"]}
d


# In[5]:


import pandas as pd
pd.DataFrame(d)


# In[6]:


d.keys()


# In[7]:


d.values()


# In[8]:


d["bloodgroup"]=("A","O+","AB")
d


# In[10]:


import pandas as pd
pd.DataFrame(d)


# In[12]:


d.pop("Name")


# In[15]:


d1={"roll no":1,"designation":"HR"}
d1


# In[17]:


d1.update({"roll no":56})
d1


# In[18]:


d1.clear()


# In[19]:


d1


# In[ ]:




