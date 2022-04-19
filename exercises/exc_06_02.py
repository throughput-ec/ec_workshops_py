import matplotlib.pyplot as plt
from cartopy import crs as ccrs

#  Suppress warnings issued by Cartopy when downloading data files
import warnings
warnings.filterwarnings('ignore')

fig = plt.figure(figsize=(11, 8.5))
fig.patch.set_facecolor('white') # necessary on Gatsby for some reason; redundant otherwise
ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=-75))
ax.set_title("A Geo-referenced subplot, Plate Carrée projection");
ax.coastlines()