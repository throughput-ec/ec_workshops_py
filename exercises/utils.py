def import_all():
    import requests
    import numpy as np
    import pandas as pd
    from datetime import datetime, timedelta, date

    #import xarray as xr
    import os
    import time

    #data visualization
    %matplotlib inline
    import matplotlib.pylab as plt
    from matplotlib import ticker
    %matplotlib inline

    #used for map projections
    import cartopy.crs as ccrs
    import cartopy.feature as cft
    from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

    import warnings
    warnings.filterwarnings('ignore')

def check_error_message(ans,writeFlag=False):
    # ans: response JSON from an API query
    # writeFlag: bool, true == print verbose errors, if found
    # returns error code if found, or NaN if not.
    if isinstance(ans,dict) and 'message' in ans.keys() and 'code' in ans.keys():
        if writeFlag:
            print(str(ans['code']) + ': ' + ans['message'])
        ##### NOTE: we should include here below all the codes that do not return data as the user expects
        if ans['code'] >= 400 and ans['code'] != 404:
            print('Data were not returned')
            print(ans)
            raise Exception('No data')
        return ans['code']        
    elif ans:
        return np.nan