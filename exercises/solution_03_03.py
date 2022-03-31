import numpy as np


time = np.arange(1,2001,1)
value = np.sin(2*np.pi*1/20*time)

idx_min = np.where(time==200)[0][0]
idx_max = np.where(time==400)[0][0]

value2 = value[idx_min:idx_max+1]

print(value2)
