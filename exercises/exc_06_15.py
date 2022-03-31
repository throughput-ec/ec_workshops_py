import matplotlib.pyplot as plt
import numpy as np
from cartopy import crs as ccrs


lon, lat = np.mgrid[-180:181, -90:91]
data = np.sin(3 * np.deg2rad(lon)) + np.cos(4 * np.deg2rad(lat))

fig = plt.figure(figsize=(11, 8.5))
fig.patch.set_facecolor('white') # necessary on Gatsby for some reason; redundant otherwise

ax = plt.subplot(1, 1, 1, projection=ccrs.Mollweide(central_longitude=0))
ax.coastlines()
dataplot = ax.contourf(lon, lat, data, transform=ccrs.PlateCarree())
plt.colorbar(dataplot, orientation='horizontal');