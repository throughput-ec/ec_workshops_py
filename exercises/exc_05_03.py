import pandas as pd
import matplotlib.pyplot as plt

# this block loads the data. You will need to reuse it in all exercises going forward. 
url = 'https://raw.githubusercontent.com/LinkedEarth/Pyleoclim_util/master/example_data/wtc_test_data_nino.csv'
df = pd.read_csv(url,skiprows=0) 
t = df['t'] # time in fractional years
nino3 = df['nino'] # NINO3 data
air  =  df['air'] # All India Rainfall 

# plot
fig, ax = plt.subplots(2,1,figsize=(10, 6),sharex = True)
fig.patch.set_facecolor('white') # necessary on Gatsby for some reason; redundant otherwise
csfont = {'fontname':_______}
ax[0].plot(t,nino3)
ax[0].set_ylabel('NINO3 SST (K)',**csfont)
ax[0].set_title('NINO3 and All India Rainfall',fontdict={____:__, ___ :___ })
ax[1].plot(t,air)
ax[1].set_ylabel('AIR (mm/month)',**csfont)
ax[1].set_xlabel(______)

plt.show() #note: this last command is unnecessary in Jupyter notebooks, where the "inline plot" option is on by default.
