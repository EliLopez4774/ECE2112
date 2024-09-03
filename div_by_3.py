#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
A = np.zeros((10,10))

ctr=1
x=0
y=0

while y < 10:
    while x < 10:
        A[x,y] = ctr*ctr
        ctr+=1
        x+=1
    y+=1
    x=0

x=0
y=0
ctr = 0
div3=np.array([0])

while y < 10:
    while x < 10:
        if (A[x,y]%3) == 0:
            div3[ctr] = A[x,y]
            ctr+=1
            size = 1+ctr
            div3.resize((size))
        x+=1
    y+=1
    x=0
    
print (div3)
np.save('div_by_3', div3)


# In[ ]:




