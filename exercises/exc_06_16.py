import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cartopy.crs as ccrs
from cartopy.io import shapereader
import geopandas
plt.style.use('seaborn-whitegrid')
#  Suppress warnings issued by Cartopy when downloading data files
import warnings
warnings.filterwarnings('ignore')

# import data 
url = 'https://raw.githubusercontent.com/LinkedEarth/Pyleoclim_util/master/example_data/wtc_test_data_nino.csv'
df = pd.read_csv(url,skiprows=0)
t = df['t'] # time in fractional years
nino3 = df['nino'] # NINO3 data
air  =  df['air'] # All India Rainfall

fig = plt.figure(figsize = (12,12))
fig.patch.set_facecolor('white') # necessary on Gatsby for some reason; redundant otherwise
# first plot the timeseries as in Module 5
a1 = plt.subplot(2, 1, 1)
a1.plot(t,nino3,label='NINO3',color='red')
a1.set_ylabel('SST (K)')
a1.set_title('Temporal evolution',fontweight='bold')
a1.legend()
# twin object for two different y-axis on the sample plot
a1b=a1.twinx()
a1b.plot(t,air,label='AIR',color='blue')
a1b.set_ylabel('Rainfall (mm/month)')
a1b.set_xlabel('Year AD') 
a1b.legend()
# then add the map:
proj = ccrs.Robinson(central_longitude=180, globe=None)
a0 = plt.subplot(2, 1, 2, projection=proj)
a0.set_extent([60, 280, -10, 40], crs=ccrs.PlateCarree())
a0.coastlines()
a0.stock_img()
gl = a0.gridlines(
    draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--'
)
# add a box for NINO3
a0.add_patch(mpatches.Rectangle(xy=[210, -5], width=60, height=10,
                                    facecolor='C0', transform=ccrs.PlateCarree()))
a0.text(230,0,"NINO3",transform=ccrs.PlateCarree(),fontweight='bold')

# highlight India the same color as the line on the plot (2nd color in the default cycler)

# extract country shape from the NaturalEarth database using geopandas
resolution = '10m'; category = 'cultural'; name = 'admin_0_countries'
shpfilename = shapereader.natural_earth(resolution, category, name)
df = geopandas.read_file(shpfilename)
# put into polygon:
poly = df.loc[df['ADMIN'] == 'India']['geometry'].values[0]
a0.add_geometries(poly, crs=ccrs.PlateCarree(), facecolor='C1')
a0.text(75,22,"India",transform=ccrs.PlateCarree(),fontweight='bold')
a0.set_title('Spatial relationships',fontweight='bold')




