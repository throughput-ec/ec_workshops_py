from cartopy.io import shapereader
import geopandas
import matplotlib.pyplot as plt
from cartopy import crs as ccrs, feature as cfeature
#  Suppress warnings issued by Cartopy when downloading data files
import warnings
warnings.filterwarnings('ignore')

def map_ukraine(highlight_color='orange'):
    '''
        This function plots a regional map of Ukraine with administrative boundaries
        
        Inputs:
        -------
        highlight_color: the color in which the territory is highlighted
        
        Outputs:
        -------
        - fig: the resuling Matplotlib Figure object
        - ax: the resuling Matplotlib Axes object
    '''
    
    latN = 54; latS = 43
    lonW = 23; lonE = 41
    cLat = (latN + latS) / 2
    cLon = (lonW + lonE) / 2

    projLccUk = ccrs.LambertConformal(central_longitude=cLon, central_latitude=cLat)
    projPC = ccrs.PlateCarree() # we keep this for transforms

    # get country borders
    resolution = '10m'
    category = 'cultural'
    name = 'admin_0_countries'
    shpfilename = shapereader.natural_earth(resolution, category, name)
    # read the shapefile using geopandas
    df = geopandas.read_file(shpfilename)

    # put into polygon:
    poly = df.loc[df['ADMIN'] == 'Ukraine']['geometry'].values[0]
    # plot: 
    fig = plt.figure(figsize=(11.5, 8))
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
    ax.add_geometries(poly, crs=projPC, facecolor=highlight_color, edgecolor='0.5')
    return fig, ax

fig, ax = map_ukraine()
latK, lonK = 50.45, 30.523333 # coordinates obtained from https://geohack.toolforge.org/geohack.php?pagename=Kyiv&params=50_27_00_N_30_31_24_E_region:UA_type:city
# add a dot and a label for the city of Kyiv
ax.plot(lonK,latK,color="k", marker="o", markersize= 10,transform=ccrs.PlateCarree())
ax.text(lonK+0.5,latK+0.5,"Kyiv", transform=ccrs.PlateCarree(),
        va='top', ha='right', fontweight='bold')
# same for Mariupol
lonM = 37.549444; latM = 47.095833
ax.plot(lonM,latM,color="k", marker="o", markersize= 10,transform=ccrs.PlateCarree())
ax.text(lonM+0.5,latM+0.5,"Mariupol", transform=ccrs.PlateCarree(),
        va='top', ha='right', fontweight='bold')
plt.show()