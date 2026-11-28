import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data=np.loadtxt("tipping.py", delimiter=",", dtype=str)

x= data[1:,0].astype(np.float32)
print("x=", x)
y= data[1:, 1].astype(np.float32)
print("y=", y)

params, params_cov=scipy.optimize.curve_fit(linear,x, y)
slope=params[0]
intercept=params[1]

print(data)
print("tips=", y)
print("bill=", x)

y_units= "dollars"
x_units= "dollars"

slope_units= slope_units(x_units, y_units)

print(print_equation(slope, intercept, x_units, y_units)) 

fig = plt.figure()
plt.scatter(t, y, label='Data')
plt.plot(t, linear(t, slope, intercept),label='Linear Fit') 
plt.legend(loc='best')
plt.xlabel("dollars ($)") 
plt.ylabel("dollars ($)")
plt.show()

fig.savefig('dataplot.png')

