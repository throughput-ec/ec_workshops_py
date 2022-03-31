import pandas as pd
import matplotlib.pyplot as plt

# this block loads the data. You will need to reuse it in all exercises going forward. 
url = 'https://raw.githubusercontent.com/LinkedEarth/Pyleoclim_util/master/example_data/wtc_test_data_nino.csv'
df = pd.read_csv(url,skiprows=0) 
t = df['t'] # time in fractional years
nino3 = df['nino'] # NINO3 data
air  =  df['air'] # All India Rainfall 

with plt.style.context(_____):
    fig = plt.figure(figsize=(12,8))
    fig.patch.set_facecolor('white') # necessary on Gatsby for some reason; redundant otherwise
    plt._____(nino3, air, c=t, _____ = _____ , ___ =___)
    plt.xlabel('NINO3 SST (K)')
    plt.ylabel('AIR (mm/month)')
    plt.colorbar(label='year')
    
plt.show() #note: this last command is unnecessary in Jupyter notebooks, where the "inline plot" option is on by default.
