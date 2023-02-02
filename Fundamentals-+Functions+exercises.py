
# coding: utf-8

# In[ ]:

# Excercise 1


# In[10]:

import random


# In[11]:

def cobb_douglas(K, L):

    # Create alpha and z
    z = 1
    alpha = 0.33

    return z * K**alpha * L**(1 - alpha)


# In[2]:

def returns_to_scale(K, L, gamma):
    y1 = cobb_douglas(K, L)
    y2 = cobb_douglas(gamma*K, gamma*L)
    y_ratio = y2 / y1
    return y_ratio / gamma


# In[3]:

cobb_douglas(1.5, 2.0)


# In[4]:

returns_to_scale(1.5, 2.0, 3.0)


# In[ ]:

# Excercise 2


# In[5]:

def mean(numbers):
    total = sum(numbers)
    N = len(numbers)
    answer = total / N
    return answer # or directly return total / N

# uncomment the line below and execute to see the error
# total


# In[17]:

x = random.sample(range(0, 1000), 10)
x


# In[36]:

# Func var

def variance(num):
    var = var1 = var2 = 0
    mean1 = mean(x)
    N = len(x)
    for i in range(0,N):
        var = (x[i] - mean1)**2
        var1 = var + var1
    var2 = var1 / (N-1)
    return var2


# In[37]:

variance(x)


# In[38]:

# Excercise 3


# In[39]:

def cobb_douglas(K, L):
    """
    Computes the production F(K, L) for a Cobb-Douglas production function

    Takes the form F(K, L) = z K^{\alpha} L^{1 - \alpha}

    We restrict z = 1 and alpha = 0.33
    """
    return 1.0 * K**(0.33) * L**(1.0 - 0.33)


# In[40]:

get_ipython().magic('pinfo cobb_douglas')
# the command is tested!


# In[ ]:

# Excercise 4


# In[ ]:

# print(object(s), sep=separator, end=end, file=file, flush=flush)


# In[43]:

print("Hello", "how are you?", sep="---", end='\s')


# In[45]:

print("Hello", "how are you?", sep="--", end='\n')


# In[47]:

print("Hello", "how are you?", sep=", ", end='\n')


# In[48]:

print("Hello", "how are you?", sep=", ", end='?')

