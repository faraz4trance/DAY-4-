#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1
import pandas as pd
print(pd.__version__)


# In[9]:


#Q2
import numpy as np
x = np.array([1,2,3,45])
print(x)
print(type(x))


# In[12]:


import seaborn as sns
print(sns.__version__)


# In[23]:


#Q4
mpg = sns.load_dataset('mpg')
mpg.head()


# In[27]:


#Q5
mpg['origin'].unique()


# In[37]:


#Q6
mpg['origin'].describe()

