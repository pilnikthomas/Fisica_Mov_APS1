
# coding: utf-8

# In[1]:

import math
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

def EqDif(Sol, t):
    theta=Sol[0]
    W=Sol[1]
    dThetadt=W
    dWdt=-9.8*math.cos(theta)/r
    return [dThetadt, dWdt]

def EqDifArrassto(Sol, t):
    theta=Sol[0]
    W=Sol[1]
    dThetadt=W
    dWdt=-9.8*math.cos(theta)/r
    return [dThetadt, dWdt]


# In[7]:

lista_t=np.arange(0,30,0.1)
r=1.65
sol=odeint(EqDif, [math.radians(50), 0], lista_t)


# In[8]:

X=[]
Y=[]
T=[]
m=0.37

for i in range(0,len(sol[:,0])):
    Theta=(sol[:,0])[i]
    W=(sol[:,1])[i]
    X.append(r*math.cos(Theta))
    Y.append(r*math.sin(Theta))
    T.append((m*(W**2)*r)-(m*9.8*math.cos(Theta)))


# In[9]:

plt.plot(X,Y, 'b')
plt.grid(True)
plt.show()

plt.plot(lista_t, X)
plt.grid(True)
plt.show()


# In[ ]:




# In[ ]:



