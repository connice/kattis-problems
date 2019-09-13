#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
#get user input 
N, M = map(int, input().split())

# check the constriant 
if N < 4 or N > 20:
      sys.exit()
elif M < 4 or M > 20:
      sys.exit()
else:
    smallnum =(min(N, M))+1
    largenum =(max(N, M))+ 1
   # print (smallnum, "\n",largenum, sep= "")

    result= smallnum
while result <= largenum:
    print(result)
    result+= 1
    

