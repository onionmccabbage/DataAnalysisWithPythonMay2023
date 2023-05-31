#!/usr/bin/env python
# coding: utf-8

# ## Beautiful Charts

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[20]:


x = np.arange(5)
np.random.seed(0)
y = np.random.rand(5)+3
y


# In[22]:


plt.bar(x, y)
plt.title('Vertical Bar Chart')


# In[52]:


# we can combine charts into a figure
plt.subplots(2,2) # a grid of two rows and two columns
# .. and the bottom right
plt.subplot(2,1,1)
plt.pie([6,5,4,3])
# target bottom left
plt.subplot(2,1,2)
plt.barh(x,y)
plt.subplot(2,2,1) # target the top left space in the figure (2,2,1)
plt.bar(x,y)
plt.subplot(2,2,2)
plt.plot(x,y) # this plots a line in top-right (2,2,2)


# In[ ]:




