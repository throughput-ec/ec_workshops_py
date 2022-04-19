import matplotlib.pyplot as plt
from cartopy import crs as ccrs, feature as cfeature
#  Suppress warnings issued by Cartopy when downloading data files
import warnings
warnings.filterwarnings('ignore')

latN = 54; latS = 43
lonW = 23; lonE = 41
cLat = (latN + latS) / 2
cLon = (lonW + lonE) / 2
projLccUk = ccrs.LambertConformal(central_longitude=cLon, central_latitude=cLat)
projPC = ccrs.PlateCarree() # we keep this for transforms

fig = plt.figure(figsize=(11, 8.5))
fig.patch.set_facecolor('white') # necessary on Gatsby for some reason; redundant otherwise
ax = plt.subplot(1, 1, 1, projection=projLccUk)
ax.set_extent([lonW, lonE, latS, latN], crs=projPC)
ax.set_facecolor(cfeature.COLORS['water'])
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle='--')
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)
ax.set_title('Ukraine and neighbors');