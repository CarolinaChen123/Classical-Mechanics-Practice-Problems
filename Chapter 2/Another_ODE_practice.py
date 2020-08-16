# The source of the code comes from here. :)
# http://www.fizika.unios.hr/rf/wp-content/uploads/sites/67/2011/02/CPwP.pdf

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from pylab import *
import math

N = 1000

y = zeros([4])

L_o = 1.0
L = 1.0
v_o = 0.0
theta_o = 0.3
omega_o = 0.3

y[0] = L
y[1] = v_o
y[2] = theta_o
y[3] = omega_o

time = np.linspace(0, 25, N)

k = 3.5
m = 0.2
gravity = 9.81

def Spring_pendulum(y, time):
    g0 = y[1]
    g1 = (L_o + y[0]) * y[3] * y[3] -k/m * y[0] + gravity * cos(y[2]) 
    g2 = y[3]
    g3 = -(gravity*sin(y[2]) + 2.0*y[1]*y[3])/(L_o + y[0])
    return array([g0, g1, g2, g3])

answer = odeint(Spring_pendulum, y, time)

xdata = (L_o + answer[:, 0]) * sin(answer[:, 2])
ydata = -(L_o + answer[:, 0]) * cos(answer[:, 2])

plot(xdata, ydata, 'r-')
xlabel("Horizontal position")
ylabel("Vertical position")
show()
