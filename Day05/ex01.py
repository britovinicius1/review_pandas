#%%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
# %%
transacoes
# %%
transacoes.head()
# %%
transacoes = transacoes.sort_values("DtCriacao")
# %%
transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date

#%%
transacoes

# %%
primeira_transacao = transacoes.drop_duplicates(keep="first", subset=["IdCliente","data"]).head(1)
# %%
primeira_transacao
# %%
#%%
transacoes
# %%
first = transacoes.drop_duplicates(keep="first", subset=["IdCliente","data"])
last = transacoes.drop_duplicates(keep="last", subset=["IdCliente","data"])

df_concatenado = pd.concat([last,first])
#%%

df_concatenado
# %%
