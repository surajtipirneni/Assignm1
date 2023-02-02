
# coding: utf-8

# In[ ]:

#Excercise 1


# In[ ]:

import math


# In[3]:

FV = 100
t = 10
i = 0.05
PV = FV/pow(1+i,t)
PV


# In[2]:

#Exercise 2


# In[4]:

# var1
x = 1

if x > 0:
    print("1")
    print("2")
print("3")


# In[5]:

# var2
x = 1

if x > 0:
    print("1")
print("2") # changed the indentation
print("3")


# In[9]:

# Modifying x to print 3
x = 0

if x > 0:
    print("1")
    print("2")
print("3")


# In[10]:

# Modifying x to print 2,3
x = 0

if x > 0:
    print("1")
print("2") # changed the indentation
print("3")


# In[ ]:

#Exercise 3


# In[11]:

import datetime
current_time = datetime.datetime.now()


# In[17]:

if current_time.time() > datetime.time(12,0,0,0):
    print("Good afternoon")


# In[16]:

#Exercise 4


# In[22]:

import numpy as np
x = np.random.random()
print(f"x = {x}")


# In[23]:

if x > 0.5:
    print('x > 0.5')
elif x < 0.5:
    print('x < 0.5')


# In[ ]:

#Exercise 5


# In[27]:

# Discount rate
r = 0.05

# High school wage
w_hs = 40000
time_working_a_hs = 40

# College wage and cost of college
c_college = 5000
w_college = 50000
t_co = 4
time_working_a_co = time_working_a_hs - t_co


# In[ ]:

import numpy as np

# Compute npv of being a hs worker
Cashflow = list(w_hs)*time_working_a_hs
NPV_a_hs = np.npv(w_hs

# Compute npv of attending college

# Compute npv of being a college worker

# Is npv_collegeworker - npv_collegecost > npv_hsworker


# In[39]:

Cashflow_hs =[]
Cashflow_hs += time_working_a_hs * [w_hs]

Cashflow_co = []
Cashflow_co += t_co * [-c_college]
Cashflow_co += time_working_a_co * [w_college]


# In[43]:

# begin work immediately after high school
PV_a_hs = np.npv(r, Cashflow_hs)
PV_a_hs


# In[44]:

# begin work after college
PV_a_co = np.npv(r, Cashflow_co)
PV_a_co


# In[ ]:




# In[46]:

PV_a_co<PV_a_hs


# In[ ]:

#At discount rate = 0.05, the student should not enroll for post-secondary school as NPV_college < NPV_highschool


# In[ ]:

#Exercise 6


# In[51]:

cities = ["Phoenix", "Austin", "San Diego", "New York"]
states = ["Arizona", "Texas", "California", "New York"]


# In[60]:

zipped = list(zip(cities, states))
len(zipped)
zipped


# In[62]:

for i in range(0,len(zipped)):
    print(zipped[i][0] + ' is in ' + zipped[i][1])


# In[ ]:

#Exercise 7


# In[75]:

# Define cost of teaching python
cost = 25_000
r = 0.01

#assuming discount rate is per year
r_monthly = r/12


# Per month value
added_value = 2500

n_months = 0
total_npv = 0.0


# In[77]:

n_months = 0
added_value_cum = 0
while added_value_cum <= cost: 
    if n_months == 0:
        added_value_cum = 0
    else:
        added_value_cum = added_value_cum + added_value/pow(1+r_monthly,n_months)
    n_months = n_months + 1 



# In[83]:

print('number of months the company requires the employees to work to make training profitable is:', n_months)


# In[84]:

#Exercise 8


# In[87]:

x = list(np.random.rand(10_000))
x


# In[ ]:




# In[89]:

for i in range(0,len(x)):
    if x[i] > 0.999:
        print('index is', i)
        break


# In[ ]:

#Exercise 9


# In[90]:

x = np.random.rand(10_000)


# In[91]:

sum_x = 0
for i in range(0,len(x)):
    if x[i] > 0.5:
        sum_x = sum_x +x[i]
    else:
        continue


# In[92]:

sum_x


# In[ ]:

#Exercise 10


# In[94]:

# utilizing variables defined in excercise 6 above

for i in range(0,len(zipped)):
    for j in range(0,len(zipped)):
        print(zipped[i][0] + ' is in ' + zipped[j][1])


# In[ ]:




# In[ ]:



