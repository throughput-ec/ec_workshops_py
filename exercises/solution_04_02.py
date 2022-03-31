import pandas as pd

df = pd.read_csv('https://github.com/ProjectPythia/pythia-datasets/raw/main/data/enso_data.csv',index_col=0)

nino = df["Nino12"]
nino_slice = nino["1982-01-01":"2010-12-31"]
nino_slice.plot()
