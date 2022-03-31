import ______ as np
from ______ import default_rng

rng = default_rng(______) #seed to obtain same value for the distribution


time = np.arange(_,_,__)
time_ens=np.reshape(np.repeat(time,1000),[__,___])
noise = rng.normal(___,___, size=___)

time_ens = ______

time_mean = ______

print(np.shape(time))
print(np.shape(time_ens))
print(np.shape(time_mean))
