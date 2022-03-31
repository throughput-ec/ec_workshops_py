import pandas as pd
import matplotlib.pyplot as plt

# this block loads the data. You will need to reuse it in all exercises going forward. 
url = 'https://raw.githubusercontent.com/LinkedEarth/Pyleoclim_util/master/example_data/wtc_test_data_nino.csv'
df = pd.read_csv(url,skiprows=0) 
t = df['t'] # time in fractional years
nino3 = df['nino'] # NINO3 data
air  =  df['air'] # All India Rainfall 

with plt.style.context('ggplot'):
    fig, ax = plt.subplots(figsize=(8,6))
    fig.patch.set_facecolor('white') # Gatsby shenanigan
    ax.______(nino3,air,_____=____)
    ax.set_xlabel('NINO3 SST (K)')
    ax.set_ylabel('AIR (mm/month)')
    ax.set_title('NINO3 vs All India Rainfall, monthly data',fontweight = 'bold')

plt.show() #note: this last command is unnecessary in Jupyter notebooks, where the "inline plot" option is on by default.
