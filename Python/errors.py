
# coding: utf-8

# In[35]:

import pyperclip
from sympy import *
init_printing()
def errors(fx, *parameters):
    eq = 0
    for parameter, error in parameters:
        eq += diff(fx, parameter) **2 * error**2
    pyperclip.copy(latex(sqrt(eq)))
    return sqrt(eq)
def delta(name):
    return var("\Delta\ %s"%(name,))
d = delta
def set_global_vars(txt):
    variables = txt.split()
    for v in variables:
        if v.startswith('\\'):
            globals()[v[1:]] = var(v)
            globals()['d'+v[1:]] = d(v)
        else:
            globals()[v] = var(v)
            globals()['d'+v] = d(v)


# In[26]:

#Example 1
C = 0.000000001
dC = 0.00000000005
R  = 1470
dR = 0.5
Omega = 1.185e5
dOmega = .0005e5


# In[73]:

fx = c*r*omega; fx


# In[74]:

errs = errors(fx, (omega, domega), (r,dr), (c,dc)); errs


# In[32]:

#Calculate Value
fx.subs({omega : Omega,  r : R, c:C })


# In[33]:

#Calculate Error
errs.subs({omega : Omega, domega : dOmega, r : R, c:C, dr : dR, dc : dC})


# In[60]:

#Example 2
set_global_vars('a1 a2')
A1 = 1.754  
dA1 = (1.751- 1.757)/3.92
A2 = 10.41
dA2 = (10.4-10.41)/3.92


# In[70]:

fx2 = a1/a2; fx2


# In[71]:

err2= errors(fx2,(a1, da1),(a2,da2)); err2


# In[62]:

#Calculate Value
fx2.subs({a1 : A1, da1 : dA1, a2 : A2, da2 : dA2})


# In[72]:

#Calculate Error
err2.subs({a1 : A1, da1 : dA1, a2 : A2, da2 : dA2, })


# In[ ]:



