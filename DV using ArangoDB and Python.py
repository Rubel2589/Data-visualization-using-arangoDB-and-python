#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyarango --user


# In[3]:


from pyArango.connection import *
conn = Connection(username="root", password="")


# In[4]:


db = conn["Instacart"]
db


# In[5]:


order = db["order"]


# In[6]:


order


# In[7]:


aql = "FOR x IN order RETURN x"
queryResult = db.AQLQuery(aql, rawResults=True, batchSize=10000)
for key in queryResult:
    print(key)


# In[8]:


data = queryResult[1:10000]


# In[9]:


data


# In[10]:


import json
import matplotlib.pyplot as plt
import pandas as pd


# In[11]:


df = pd.DataFrame(data)


# In[12]:


df


# In[13]:


# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df['order_dow'], df['order_hour_of_day'], c=df['order_number'], cmap='viridis', s=100)
plt.colorbar(label='order_number')
plt.title('Order Hour of Day vs. Order Day of Week')
plt.xlabel('Order Day of Week')
plt.ylabel('Order Hour of Day')
plt.grid(True)
plt.show()


# In[14]:


pip install squarify


# In[15]:


import squarify


# In[16]:


# Group data by order day of week and sum the order numbers
sum_order_by_dow = df.groupby('order_dow')['order_number'].sum().reset_index(name='count')

print(sum_order_by_dow)


# In[17]:


sum_order_by_dow.index


# In[22]:


# Plotting
plt.figure(figsize=(10, 6))
plt.title("Order Day of Week Vs Total no of order")
squarify.plot(sum_order_by_dow["count"], label=sum_order_by_dow.apply(lambda x: f"{x['order_dow']}-{x['count']}", axis=1), alpha=0.8)


# In[ ]:





# In[ ]:




