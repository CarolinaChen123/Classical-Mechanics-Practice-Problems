# There is another initial value problem which I picked from a calculus textbook
# y''+y'-6y=0, y(0)=1, y'(0)=0
# This equation could be written into y''=-y'+6y

# So now let me assume that y'=z. Then the equation becomes z'+z-6y=0 or z'=-z+6y
# The initial condition becomes that y(0)=1 and z(0)=0.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

#initializing the array for y-
def function(Set, t, b=1, c=1):
    return [Set[1], -Set[1]+6*Set[0]]

Set = [1, 0]

t = np.linspace(0, 20, 10)

New = odeint(function, Set, t)

Solution = New[:, 0]

Check =  0.6*np.exp(2*t) + 0.4*np.exp(-3*t)

plt.xlabel("t")
plt.ylabel("y")
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 50.0)
plt.plot(t, Solution);
plt.plot(t, Check, 'r--')
