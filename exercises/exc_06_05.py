import matplotlib.pyplot as plt
from cartopy import crs as ccrs
#  Suppress warnings issued by Cartopy when downloading data files
import warnings
warnings.filterwarnings('ignore')

fig = plt.figure(figsize=(10, 5))
fig.patch.set_facecolor('white') # necessary on Gatsby for some reason; redundant otherwise
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.stock_img()
ax.coastlines()
ax.tissot(facecolor='orange', alpha=0.8)
ax.set_title("Plate Carrée projection with Tissot's indicatrix");