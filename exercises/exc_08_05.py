import requests
import pandas as pd
import numpy as np
from utilities import check_error_message

#data visualization
import matplotlib.pylab as plt
from matplotlib import ticker

#used for map projections
import cartopy.crs as ccrs
import cartopy.feature as cft
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


# prefix to use with all API queries
URL_PREFIX = 'https://argovis-api.colorado.edu'
# users that have an API key would use it in their code (no need to do so here)
API_KEY   = ''

startDate = '2018-05-29T00:00:00Z'
endDate   = '2018-05-31T00:00:00Z'

polygon = '[[61.096076,25.106205],[51.933279,10.054482],[60.37706,9.236052],[68.777189,8.221804],[77.130969,7.034482],[71.404221,19.816425],[61.096076,25.106205]]'

# define url for the API query of profile locations in a region (polygon) and time range of interest
url = URL_PREFIX + '/profiles?' + \
      '&startDate=' + startDate + \
      '&endDate=' + endDate + \
      '&polygon=' + polygon + \
      '&source=argo_core'

# make the request
d   = requests.get(url,headers={"x-argokey": API_KEY}).json()
# check what the API request returned
ans = check_error_message(ans=d,writeFlag=True)
# if there are data, create a panda dataframe from the returned list of dictionaries

if np.isnan(ans):
    df = pd.DataFrame(d)

# Printing column names as the Data Frame is too wide
# let's store longitude and latitude for the profiles in the dataframe
lon = [x['coordinates'][0] for x in df['geolocation']]
lat = [x['coordinates'][1] for x in df['geolocation']]

# Plot Code
# if there are data, plot profile locations on a map
if np.isnan(ans):
    #### set up the map first
    # this declares a recentered projection for Pacific areas
    usemap_proj = ccrs.PlateCarree(central_longitude=50)
    usemap_proj._threshold /= 20.  # to make greatcircle smooth

    ax = plt.axes(projection=usemap_proj)
    # set appropriate extents: (lon_min, lon_max, lat_min, lat_max)
    ax.set_extent([min(lon)-10,max(lon)+10,min(lat)-5,max(lat)+5], crs=ccrs.PlateCarree())

    gl = ax.gridlines(draw_labels=True,color='black')
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlocator = ticker.FixedLocator(np.arange(-180,180,5))
    gl.ylocator = ticker.FixedLocator(np.arange(-90,90,5))

    gl.xlabel_style = {'size': 16}
    gl.ylabel_style = {'size': 16}

    ax.coastlines()
    ax.add_feature(cft.LAND)#, color='lightgray'
    ax.add_feature(cft.OCEAN)
    ax.add_feature(cft.COASTLINE)
    ax.add_feature(cft.BORDERS, linestyle=':')

    geodetic = ccrs.Geodetic()
    #### plot the profile locations
    plt.plot(lon,lat,marker='o',markersize=10,color='k',linestyle='none',transform=ccrs.PlateCarree())