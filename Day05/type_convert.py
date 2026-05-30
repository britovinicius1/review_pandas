#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
# %%
#
clientes
# %%
#serie do tipo int
clientes["qtdePontos"]
# %%
#Convertendo para outro tipo
clientes["qtdePontos"].astype(str).astype(int)

# %%
clientes
#%%

clientes["DtCriacao"][5471]
# %%
#parecido com o case when, da pra por mais chaves
#isso nao altera a serie -> 
replace = {"0000-00-00 00:00:00.000":"2024-02-01 09:00:00.000"}
clientes["DtCriacao"] = pd.to_datetime(clientes["DtCriacao"].replace(replace))

# %%
ano = clientes["DtCriacao"].dt.year
data_clientes = clientes["DtCriacao"].dt.date
dia_clientes = clientes["DtCriacao"].dt.day
mes_clientes = clientes["DtCriacao"].dt.month
data_clientes
dia_clientes
mes_clientes
# %%
