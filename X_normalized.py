#!/usr/bin/env python
# coding: utf-8

# In[28]:


#import the NumPy Library
import numpy as np

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


# In[ ]:




