# The question comes from the following link, but there is no code provided in that link since it is just purely a math tutorial.
# https://mathinsight.org/ordinary_differential_equation_introduction_examples
# The differential equation is dx/dt = 5x-3

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

def function(x, t):
    dxdt = 5*x - 3
    return dxdt
  
#Initial condition is that x(2) = 3
x0 = 1
t = np.linspace(2, 12, 100)
x = odeint(function, x0, t)
y = (2/5)*np.exp(5*(t-2)) + (3/5)

plt.plot(t,x,'r-')
plt.plot(t,y,'b--')
plt.show()

# This is an important comment that I want everyone who is seeing this file to pay attention to.
# If the initial condition is given not at t = 0, then what should us do?
# Here is a really good comment from the website.
# https://stackoverflow.com/questions/59758833/issue-with-odeint-from-scipy-integrate-when-i-start-the-range-not-at-0
'''
# The "initial condition" does not mean the value at t=0. 
# The initial condition given to odeint is the value at the first t value. 
# In your case, you have start = -1, so your U0 specifies the value at t=-1. 
# That's what is shown in your first plot.
'''
# Also one important thing I learn is that math.exp is really different from np.exp.
# I spend so many fxxking time in find the error when I accidentally used math.exp but I should use np.exp.
# I feel I am stupid. :)
