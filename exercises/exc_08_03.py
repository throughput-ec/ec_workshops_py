from utilities import import_all
from utilities import check_error_message

# prefix to use with all API queries
URL_PREFIX = 'https://argovis-api.colorado.edu'
# users that have an API key would use it in their code (no need to do so here)
API_KEY   = ''

startDate = '2018-05-29T00:00:00Z'
endDate   = '2018-05-31T00:00:00Z'
# To see what this polygon looks like, scroll over east of Africa at 
# https://argovis.colorado.edu/ng/home?mapProj=WM&presRange=%5B0,2000%5D&selectionStartDate=2018-04-27&selectionEndDate=2018-04-28&threeDayEndDate=2022-04-05T03:45:47&shapes=%5B%5B%5B25.106205,61.096076%5D,%5B10.054482,51.933279%5D,%5B9.236052,60.37706%5D,%5B8.221804,68.777189%5D,%5B7.034482,77.130969%5D,%5B19.816425,71.404221%5D,%5B25.106205,61.096076%5D%5D%5D&includeRealtime=true&onlyBGC=false&onlyDeep=false&threeDayToggle=false
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

df.head()