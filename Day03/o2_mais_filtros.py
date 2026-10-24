#%%

import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv", sep=";")

# %%
filtro = (df["IdProduto"] == "5") | (df["IdProduto"] == "11")

#%%
df.dtypes
# %%
df[filtro]
# %%
df["IdProduto"].isin([5,11])
# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes
# %%
clientes["DtCriacao"].notna()
# %%
### negação da condição não não é nao

~clientes["DtCriacao"].notna()

