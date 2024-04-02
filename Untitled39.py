#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[19]:


df=pd.read_csv("C:/Users/dhanu/Downloads/supermarket_sales.csv")
df


# In[20]:


print(df.shape)
df['Gender'].value_counts()


# In[21]:


sns.countplot(x='Gender', data=df)


# In[33]:


#Plotting Customers per city
place = pd.DataFrame(df['City'].value_counts())
place


# In[37]:


sns.barplot(x=place.index  , y=place['count'])


# In[35]:


payment = df.groupby('Payment').size().reset_index(name='Count')
payment


# In[36]:


sns.barplot(x=payment['Payment'] , y=payment['Count'])


# In[38]:


plt.figure(figsize= (12,6))
sns.barplot(x = df['Product line'], y = df['gross income'])


# In[39]:


xdata = [0,1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize = (12,6))
sns.barplot(y = df['Product line'], x = df['Rating'])
plt.xticks(xdata)


# In[40]:


plt.figure(figsize = (12,6))
sns.barplot(x = df['Total'] , y = df['Product line'])


# In[41]:


xdata = [1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize = (12,6))
sns.distplot(df['Quantity'])
plt.xticks(xdata)


# In[42]:


quantity = pd.DataFrame(df['Quantity'].value_counts())
quantity


# In[47]:


plt.figure(figsize=(12,6))
sns.barplot(x = df['index'], y = df['count'])


# In[ ]:




