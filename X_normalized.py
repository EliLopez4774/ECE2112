#!/usr/bin/env python
# coding: utf-8

# In[28]:


#import the NumPy Library
import numpy as np

#Problem Number 1

#making the random array and assigning it to X
X = np.random.random((5,5))
print("Random Array X: \n",X,"\n")

avg = np.mean(X)
sd = np.std(X)

#making a room for the normalized array
Z = np.zeros((5,5))
x = 0
y = 0

#Nested loop to change the Zero Array with the Normalized Values using the Z formula
while y < 5:
    while x < 5:
        Z[x,y] = (avg-(X[x,y]))/sd
        x+=1
    y+=1
    #Reset x
    x=0

print("Normalized Array Z: \n",Z)
np.save('X_normalized',Z)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Problem Number 2
#Making a container for the square values
A = np.zeros((10,10))

#counters
ctr=1
x=0
y=0

#Filling the initial array with square values of the first 100 numbers
while y < 10:
    while x < 10:
        A[x,y] = ctr*ctr
        ctr+=1
        x+=1
    y+=1
    x=0

#restart counters and make the divisible by three array
x=0
y=0
ctr = 0
div3=np.array([0])

#Nested loop
while y < 10:
    while x < 10:
        #Checks if the number in the array is divisible by three, if it is, the number is stored into the div3 array
        if (A[x,y]%3) == 0:
            div3[ctr] = A[x,y]
            ctr+=1
            size = 1+ctr
            div3.resize((size))
        x+=1
    y+=1
    x=0
    
#print and save
print (div3)
np.save('div_by_3', div3)



# In[ ]:




