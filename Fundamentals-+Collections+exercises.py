
# coding: utf-8

# In[ ]:

#Excercise 1


# In[7]:

y = ["a", "b", "c"]
z = [1, 2, 3]
y.append(z)
print(y)


# In[6]:

clear(y,z)


# In[4]:

y = ["a", "b", "c"]
z = [1, 2, 3]
y.extend(z)
print(y)


# In[ ]:

# Append adds 'z' at the end of 'y' as it is. It adds 'z' as a list at the end of 'y'
# Extend, extends the list 'y'. It adds the elements of the list 'z' at the end of 'y' 


# In[ ]:

#Excercise 2


# In[8]:

list(range(0, 5))


# In[9]:

list(range(0, 15, 2))


# In[ ]:

#Excercise 3


# In[2]:

t = (1, "hello", 3.0)


# In[4]:

t(0) = 100


# In[3]:

t.append(200)
#t(len(t)+1)=200
t


# In[5]:

t1 = t.sort()


# In[ ]:

#Reversing a tuple is not feasible because tuples are immutable i.e., the elements and thier order remains the same 
#and can't be changed. 


# In[6]:

t.reverse()


# In[ ]:

#However, a tuple can be mutated to a list. Operations such as sort and reverse can then be performaed on the list


# In[7]:

t_list = list(t)
t_list


# In[ ]:

#Excercise 4


# In[8]:

foo = ("good", "luck!")


# In[10]:

# Expected result
enum_foo = list(enumerate(foo))
enum_foo


# In[ ]:

# Combination of zip, range, and len


# In[11]:

l = len(foo)
l


# In[29]:

index_foo = []
for i in range(0,len(foo)):
    index_foo.append(i)

index_foo


# In[31]:

zipped_foo = list(zip(index_foo,foo))
zipped_foo


# In[32]:

enum_foo == zipped_foo


# In[33]:

#Excercise 5


# In[35]:

companies = {"AAPL": {"price": 175.96},
             "GE": {"price": 1047.43},
             "TVIX": {"price": 8.38}}
print(companies)


# In[ ]:

#Excercise 6


# In[4]:

Australia_data = {"country": "Australia", "Area": 7741220, "Agricultural Land %" : 46.65, "Major Lakes": ['Eyre','Torrens','Gairdner'],
                 'Coordinates': {'Lat': '27 00 S', 'Long' : '133 00 E'}}
Australia_data


# In[ ]:

#Excercise 7


# In[8]:

China_data = {'country': 'China',
 'year': 2015,
 'GDP': 11.06,
 'population': 1.371,
 'unemployment': 4.051,
 'irrigated_land': 690070,
 'top_religions': {'buddhist': 18.2, 'christian': 5.1, 'muslim': 1.8}}


# In[9]:

New_china_data = China_data.pop('irrigated_land')


# In[11]:

China_data


# In[ ]:

#Excercise 8


# In[20]:

#1 Calling pop once
China_data = {'country': 'China',
 'year': 2015,
 'GDP': 11.06,
 'population': 1.371,
 'unemployment': 4.051,
 'irrigated_land': 690070,
 'top_religions': {'buddhist': 18.2, 'christian': 5.1, 'muslim': 1.8}}
New_china_data = China_data.pop('irrigated_land')
China_data


# In[22]:

#2 Calling pop twice
New_china_data = China_data.pop('irrigated_land','no_key')
New_china_data


# In[ ]:

# As the key is already removed from the dict, in the second pop command, the function couldn't find the key 'irrigated land'. 
# So, it returned the default value mentioned in the function i.e., 'no_key'
# If the default value is not mentione,d it would have returned an error statement.


# In[ ]:

#Excercise 9


# In[23]:

Set1 = {1, 2, 1, 2, 1, 2}


# In[24]:

Set1


# In[ ]:

# A set with repeated elements removed the repetitions and ket the unique elements 
# this is because, duplicates are not permitted in the set data structure


# In[ ]:

#Excercise 10


# In[25]:

s = {1, "hello", 3.0}
s2 = {"hello", "world"}


# In[26]:

# Operation 1 - Union
s3 = s.union(s2)
s3


# In[27]:

# Operation 1 - Intersection
s4 = s.intersection(s2)
s4


# In[ ]:



