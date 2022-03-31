import pandas as pd
import matplotlib.pyplot as plt

# this block loads the data. You will need to reuse it in all exercises going forward. 
url = 'https://raw.githubusercontent.com/LinkedEarth/Pyleoclim_util/master/example_data/wtc_test_data_nino.csv'
df = pd.read_csv(url,skiprows=0) 
t = df['t'] # time in fractional years
nino3 = df['nino'] # NINO3 data
air  =  df['air'] # All India Rainfall 

def nino3_air_plot(plot_title):
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('white')
    ax.plot(t,nino3,label='NINO3',color='C0')
    ax.set_ylabel('NINO3 SST (K)')
    ax.set_title(plot_title)
    ax.legend()
    # twin object for two different y-axis on the sample plot
    ax2=ax.twinx()
    ax2.plot(t,air,label='AIR',color='C1')
    ax2.set_xlabel('Year AD')
    ax2.legend()

available = ['default'] + plt.style.available
for i, style in enumerate(available):
    with plt.style.context(style):
        nino3_air_plot(plot_title=style)
    
plt.show() #note: this last command is unnecessary in Jupyter notebooks, where the "inline plot" option is on by default.
