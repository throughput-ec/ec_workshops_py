import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(11, 8.5))
fig.patch.set_facecolor('white') # necessary on Gatsby for some reason; redundant otherwise
lon, lat = np.mgrid[-180:181, -90:91]
data = np.sin(3 * np.deg2rad(lon)) + np.cos(4 * np.deg2rad(lat))
plt.contourf(lon, lat, data)
plt.colorbar();

