import pandas as pd
import matplotlib.pyplot as plt

# this block loads the data. You will need to reuse it in all exercises going forward. 
url = 'https://raw.githubusercontent.com/LinkedEarth/Pyleoclim_util/master/example_data/wtc_test_data_nino.csv'
df = pd.read_csv(url,skiprows=0) 
t = df['t'] # time in fractional years
nino3 = df['nino'] # NINO3 data
air  =  df['air'] # All India Rainfall 

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('white') # gatsby adjustment
ax.plot(t,nino3,label='NINO3',color='tab:red')
ax.set_ylabel('NINO3 SST (K)')
ax.set_title('NINO3 and All India Rainfall',fontweight='bold')
ax.legend()
# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
ax2.plot(t,air,label='AIR',color='tab:green',alpha=0.6)
ax2.set_xlabel('Year AD') 
ax2.legend()

plt.show() #note: this last command is unnecessary in Jupyter notebooks, where the "inline plot" option is on by default.
