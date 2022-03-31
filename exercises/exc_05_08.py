import pandas as pd
import matplotlib.pyplot as plt

# this block loads the data. You will need to reuse it in all exercises going forward. 
url = 'https://raw.githubusercontent.com/LinkedEarth/Pyleoclim_util/master/example_data/wtc_test_data_nino.csv'
df  = pd.read_csv(url,skiprows=0) 
t   = df['t'] # time in fractional years
nino3 = df['nino'] # NINO3 data
air  =  df['air'] # All India Rainfall 

fig = plt.figure(figsize=(10,8))
fig.patch.set_facecolor('white') # necessary on Gatsby for some reason; redundant otherwise
ax = plt.axes(projection = ____ )  # syntax for 3-D projection 
p = ax.scatter(___, ___ , ___, c=_, cmap='viridis');
fig.colorbar(p,label='Year', ax=ax) # include colorbar
ax.set_xlabel('NINO3 (K)'); ax.set_ylabel('Year'); ax.set_zlabel('AIR (mm/month)');
ax.set_title('3D representation', fontweight = 'bold')

plt.show() #note: this last command is unnecessary in Jupyter notebooks, where the "inline plot" option is on by default.
