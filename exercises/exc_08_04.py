import requests
import pandas as pd
import numpy as np
from utilities import check_error_message

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


print("lat", lat)
print("long", lon)