#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import numpy as np
np.zeros(10)


# In[3]:


import numpy as np
np.ones(10)


# In[4]:


import numpy as np
np.arange(5,50,5)


# In[5]:


import numpy as np
np.arange(10,51,1)


# In[6]:


import numpy as np
np.arange(10,51,2)


# In[7]:


import numpy as np
np.array([[[0,1,2],[3,4,5],[6,7,8]]])


# In[8]:


import numpy as np
np.array([[[1,0,0,],[0,1,0],[0,0,1]]])


# In[9]:


import numpy as np
s=np.random.normal(0,1)
print(s)


# In[13]:


import numpy as np
a=np.random.randn(25)
a


# In[15]:


import numpy as np
a=np.arange(0,1.2,0.0101000)
a


# In[16]:


import numpy as np
np.linspace(0,1,20)


# In[17]:


import numpy as np
a=np.arange(1,26,1)
b=a.reshape(5,5)
b


# In[18]:


import numpy as np
a= np.arange(1, 26).reshape(5, 5)
b=a[1:, 1:]
print(b)


# In[19]:


import numpy as np
a= np.arange(1, 26).reshape(5, 5)
b=a[1:, 1:]
print(b)


# In[20]:


import numpy as np
a=np.array([[[2],[7],[12]]])
a


# In[21]:


import numpy as np
s=np.array([21,22,23,24,25])
s


# In[22]:


import numpy as np
a=np.array([[16,17,18,19,20],[21,22,23,24,25]])


# In[24]:


import numpy as np
a=([55,60,65,70,75])
np.std(a)


# In[25]:


import numpy as np
a=([55,60,65,70,75])
np.sum(a)


# In[ ]:




