import matplotlib.pyplot as plt
from cartopy import crs as ccrs, feature as cfeature

fig = plt.figure(figsize=(11, 8.5))
ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=-75))
ax.set_title("A Geo-referenced subplot, Plate Carrée projection");