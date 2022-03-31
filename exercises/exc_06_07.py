import matplotlib.pyplot as plt
from cartopy import crs as ccrs, feature as cfeature
#  Suppress warnings issued by Cartopy when downloading data files
import warnings
warnings.filterwarnings('ignore')

fig = plt.figure(figsize=(11, 8.5))
fig.patch.set_facecolor('white') # necessary on Gatsby for some reason; redundant otherwise
proj = ccrs.__________
ax = plt.subplot(1, 1, 1, projection=proj)
ax.coastlines()
ax.stock_img()
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='blue');
ax.tissot(facecolor='orange', alpha=0.8)
ax.set_title("____________ Projection with Tissot's indicatrix");