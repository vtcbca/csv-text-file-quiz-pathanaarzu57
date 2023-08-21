#!/usr/bin/env python
# coding: utf-8

# #write a program to create "intro.txt"file.print only even number of row.

# In[1]:


import csv


# In[2]:


f=open('intro.txt','w',newline='')
print(f)


# In[3]:


w=csv.writer(f)


# In[4]:


header=["id","name","no"]


# In[5]:


w.writerow(header)


# In[6]:


row=[[1,"om",21],[2,"sai",22],[3,"ram",23]]


# In[7]:


w.writerows(row)


# In[8]:


f.close()


# In[11]:


#print even number of row
with open('intro.txt','r',newline='')as f:
    data=f.readlines()[0::2]
    print(data)
    obj=csv.reader(f)
    for i in obj:
        print(i)


# In[ ]:




