#%%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
# %%
df.head(5)
# %%
df["qtd_100"] = df["qtdePontos"] + 100
# %%
df.head(5)
# %%
df["flEmail"]