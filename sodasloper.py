#!/usr/bin/env python
# coding: utf-8

# In[17]:



e, f, c= map(int, input().split())
b= e+f
l = []
result= b//c
remainder= b%c
A = result + remainder
l.append(result)
while A >= c:
    B = A//c
    A = B +(A%c)
    l.append(B)
print(sum(l))



    



# In[13]:


e, f, c= map(int, input().split())
empbot= (e+f)//c
result = empbot
while empbot >= c:
    result += empbot//c
    empbot = empbot//c +empbot%c
print (result)

