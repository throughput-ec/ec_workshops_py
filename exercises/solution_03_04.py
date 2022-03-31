import numpy as np
from numpy.random import default_rng

rng = default_rng(30) #seed to obtain same value for the distribution


time = np.arange(0,10001,100)
time_ens=np.reshape(np.repeat(time,1000),[np.shape(time)[0],1000])
noise = rng.normal(0, 200, size=np.shape(time_ens))

time_ens = time_ens+noise

time_mean = np.mean(time_ens,axis=1)

print(np.shape(time))
print(np.shape(time_ens))
print(np.shape(time_mean))
