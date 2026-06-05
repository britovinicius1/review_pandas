#%%
import pandas as pd


df = pd.read_csv("../dados/clientes.csv", sep=';')


# %%
df
# %%
df.to_csv("../dados/teste.csv")
# %%
