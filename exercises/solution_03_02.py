import numpy as np
from numpy.random import default_rng

rng = default_rng(10) #seed to obtain same value for the distribution


time = np.arange(1,2001,1)
value = np.sin(2*np.pi*1/20*time)

white_noise = rng.normal(0, np.sqrt(np.var(value)/2), size=np.size(value))

value2 = value+white_noise

print(time)
print(value2)
