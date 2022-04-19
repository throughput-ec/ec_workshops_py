import pandas as pd
import matplotlib.pyplot as plt

# this block loads the data. You will need to reuse it in all exercises going forward. 
url = 'https://raw.githubusercontent.com/LinkedEarth/Pyleoclim_util/master/example_data/wtc_test_data_nino.csv'
df = pd.read_csv(url,skiprows=0) 
t = df['t'] # time in fractional years
nino3 = df['nino'] # NINO3 data
 
# plot
fig, ax = plt.subplots()
ax.____(___,___)
ax.___('NINO3 SST')
ax.___('NINO3 (K)')
ax.___('Year AD')
# remove upper and top spines
ax.spines[['top', 'right']].___(___)

plt.show() # note: this last command is unnecessary in Jupyter notebooks, 
           # where the "inline plot" option is on by default.
