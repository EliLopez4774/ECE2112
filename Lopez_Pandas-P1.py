#!/usr/bin/env python
# coding: utf-8

# # Problem 1
# #### Dataframing cars.csv

# In[33]:


#importing the library
import pandas as pd

#reading the .csv file for the program to use
cars = pd.read_csv('cars.csv')

#why use print? 
#the use of the print operator is essential as when it is just the tail and head operator used simultaneously, only the last operation will appear
print(cars.head(),"\n...\n",cars.tail())


# In[35]:


#as shown at this part, only the cars.tail() gets ran, as it is the last operator
cars.head()
cars.tail()


# In[ ]:




