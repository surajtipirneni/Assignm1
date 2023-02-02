
# coding: utf-8

# In[ ]:

"Suraj"


# In[1]:

x = "Hello World"
x


# In[ ]:

#Excercise 1


# In[1]:

z = 3
z = z + 4
print("z is", z)


# In[ ]:

#Excercise 2


# In[2]:

len(x)


# In[ ]:

#Excercise 3


# In[3]:

import time


# In[5]:

time.localtime()


# In[6]:

#Excercise 4

import time as t
# In[8]:

import time as t


# In[9]:

t.localtime()


# In[ ]:

#Excercise 5


# In[13]:

D = float(10000)
r = float(0.025)
T = int(30)


# In[14]:

#Excercise 6


# In[22]:

PDV = D/pow(1+r,T)
PDV


# In[ ]:

#Excercise 7


# In[24]:

import math


# In[23]:

x = 1.05
y = 1.02


# In[26]:

z = math.log(x) - math.log(y)
z


# In[29]:

z1 = (x-y)/x
z1


# In[28]:

#Excercise 8


# In[31]:

x = "What's wrong with this string"
x


# In[ ]:

#Excercise 9


# In[32]:

x = "Hello"
y = "World"
print(x+" "+y)


# In[ ]:

#Excercise 10


# In[35]:

test = "abc"
test = test.replace('c','d')
test


# In[ ]:

#Excercise 11


# In[48]:

price = "$6.50"
price = price.replace('$','')
clean_price = float(price)
clean_price


# In[ ]:

#Excercise 12


# In[51]:

string1 = "Growth rate of USA's GDP is {}% over the last {} years"
print(string1.format(5.9,2))


# In[ ]:

#Excercise 13


# In[53]:

Country = "United States"
GDP = 5.9
Year = 2021


# In[54]:

string2 = f"Growth rate of {Country}'s GDP is {GDP}% since {Year}"
print(string2)


# In[ ]:

#Excercise 14


# In[55]:

rev = [100,95,110,130]


# In[62]:

for i in range(1,5):
    print(f"The {i}st quarter revenue was {rev[i-1]}M")


# In[ ]:

#Excercie 15


# In[63]:

x = 2
y = 2
z = 4


# In[64]:

# Statement 1
x > z


# In[65]:

# Statement 2
x == y


# In[66]:

# Statement 3
(x < y) and (x > y)


# In[67]:

# Statement 4
(x < y) or (x > y)


# In[68]:

# Statement 5
(x <= y) and (x >= y)


# In[69]:

# Statement 6
True and ((x < z) or (x < y))


# In[ ]:

#Excercie 16


# In[70]:

all([True, True, True])


# In[71]:

all([False, True, False])


# In[72]:

all([False, False, False])


# In[73]:

any([True, True, True])


# In[74]:

any([False, True, False])


# In[75]:

any([False, False, False])


# In[ ]:



