#%%
import pandas as pd
df = pd.read_csv("../dados/transacao_produto.csv", sep=";")
df
# %%

filtro = (df["IdProduto"]== "5") | (df["IdProduto"] == "11")

df[filtro]
# %%
filtro = df["IdProduto"].isin(["5","11"])
filtro
# %%
df[filtro]

# %%
df = pd.read_csv("../dados/clientes.csv", sep=";")
# %%
df
# %%
###vaziooo -> ele vai ver se é vazio
#not null
filtro = df["DtCriacao"].notna()
# %%
df[filtro]

# %%
###vaziooo
filtro = ~df["DtCriacao"].isna()
filtor = df["DtCriacao"].notna()

# %%
