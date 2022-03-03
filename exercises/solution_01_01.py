import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/LinkedEarth/Pyleoclim_util/master/example_data/soi_data.csv',skiprows=0, header=1)
df.head()