#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np

cars = pd.read_csv('cars.csv')

arr = np.empty([6])
ctr1 = 0
ctr2 = 0

while ctr1 <= 10:
    if (ctr1%2)==0:
        arr[ctr2] = ctr1
        ctr2+=1
    ctr1+=1
row = np.empty([5])
ctr1=0
while ctr1 < 5:
    row[ctr1]= ctr1
    ctr1+=1

cars.iloc[row,arr]


# In[25]:


cars.loc[(cars['Model']=='Mazda RX4')]


# In[29]:


cars.loc[(cars['Model']=='Camaro Z28'), ['Model','cyl']]


# In[45]:


model = ['Mazda RX4 Wag','Ford Pantera L','Honda Civic']
ctr = 0
while ctr < len(model):
    print(cars.loc[(cars['Model']== model[ctr]), ['Model','cyl','gear']])
    ctr+=1


# In[ ]:




