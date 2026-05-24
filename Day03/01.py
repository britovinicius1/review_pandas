#%%
import pandas as pd

df = pd.read_csv("../dados/transacoes.csv", sep=";")

df

# %%

filtro = df["QtdePontos"]>=50

df[filtro]

# %%

filtro2 = (df['QtdePontos'] >= 50) & (df['QtdePontos'] < 100) 

df[filtro2]
# %%
filtro2 = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100) 

df[filtro2]
# %%
