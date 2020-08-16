# The question comes from the following link, but there is no code provided in that link since it is just purely a math tutorial.
# https://mathinsight.org/ordinary_differential_equation_introduction_examples
# The differential equation is dx/dt = 5x-3

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def function(x, t):
    dxdt = 5*x - 3
    return dxdt
  
#Initial condition is that x(2) = 3

