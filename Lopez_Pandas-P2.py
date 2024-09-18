#!/usr/bin/env python
# coding: utf-8

# In[23]:

#Library dependencies
import pandas as pd
import numpy as np

#recalling the .csv file into the same variable as dataframe
cars = pd.read_csv('cars.csv')

#making an empty array for counting
arr = np.empty([6])
ctr1 = 0
ctr2 = 0

#Generates the array containing of odd numbers for the columns required
while ctr1 <= 10:
    if (ctr1%2)==0:
        arr[ctr2] = ctr1
        ctr2+=1
    ctr1+=1
#Generates the array containing the first five numbers for the rows required
row = np.empty([5])
ctr1=0
while ctr1 < 5:
    row[ctr1]= ctr1
    ctr1+=1

#using the arrays as the parameters for the .iloc or index based locator for the dataframe, cars
cars.iloc[row,arr]


# In[25]:

#the problem asks for the row of values for a certain model, that model being Mazda RX4
cars.loc[(cars['Model']=='Mazda RX4')]


# In[29]:

#The problem then asks for the table displaying the Model name and the cylinders only of a certain model, that model being Camaro Z28
cars.loc[(cars['Model']=='Camaro Z28'), ['Model','cyl']]


# In[45]:

# The last part of the problem asks for a table of values that will display the model names, amount of cylinders, and gears of three certain models, that being the models listed in the list, model
model = ['Mazda RX4 Wag','Ford Pantera L','Honda Civic']
ctr = 0

#using a while loop to loop the values in the list and print the tables with corresponding values
while ctr < len(model):
    print(cars.loc[(cars['Model']== model[ctr]), ['Model','cyl','gear']])
    ctr+=1


# In[ ]:




