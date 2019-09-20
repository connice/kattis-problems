#!/usr/bin/env python
# coding: utf-8

# In[13]:


import math
#get user input 
N = int(input())

for i in range (N):
    a, q = list(input().split())
    b = int(a)
    p =float(q)
    

    BPM = 60*b/p
    t = 60/p
    minAbpm = BPM - t
    LarAbpm = BPM + t
    print (minAbpm, "\n",BPM, "\n", LarAbpm, sep= "")

    
    

    
    
    
    


# In[ ]:





# In[ ]:




