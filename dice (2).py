#!/usr/bin/env python
# coding: utf-8

# In[17]:


import sys
#get user input 
N, M = map(int, input().split())

# check the constriant 
if N < 4 or N > 20:
      sys.exit()
if M < 4 or M > 20:
      sys.exit()
else:
    smallnum =(min(N, M))+1
    largenum =(max(N, M ))+1
for item in range (smallnum, largenum):
    print (item)



        


# In[ ]:


import sys 
#get user input 
n = int(input())
x=1
if n>= 1 and n<= 100:
    while(x <= n):
        print (str(x) + " Abracadabra")
        x =+ 1
        
        



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[22]:


import sys 
#get user input 
n = int(input())
x=1
if n>= 1 and n<= 100:
    while(x <= n):
        print (str(x) + " Abracadabra")
        x += 1
        


# In[30]:



import sys
#get user input 
N, M = map(int, input().split())

# check the constriant 

for item in range (4, 20):
    print (min((N, M)+1))
    (N, M )=+ 1


    


# In[24]:



import sys
#get user input 
N, M = map(int, input().split())

# check the constriant 

for item in range (4, 20):
    num =(min(N, M))+1
    print (num)
    num +=1


# In[22]:


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
    
    
    


# In[ ]:





# In[ ]:




