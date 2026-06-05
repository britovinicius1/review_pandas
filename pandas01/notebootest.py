#%%
import pandas as pd
import matplotlib.pyplot as plt
arquivo = "../data/kc_house_data.csv"
df = pd.read_csv(arquivo, sep=",", header=0)


#%%
df
# %%
df["price"].plot()
# %%
