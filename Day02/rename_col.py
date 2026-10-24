#%%

import pandas as pd


df_transac = pd.read_csv("../data/transacoes.csv", sep=";")
# %%
df_transac.shape
#
df_transac.columns
# %%
df_transac.head(2)
# %%
#ele cria um dataframe novo q precisa ser armazenado
df_transac = df_transac.rename(columns=
                  {
                      "IdTransacao": "idtransacao",
                      "QtdePontos": "qtpontos",
                      "DescSistemaOrigem": "SistemaOrigem",
                      "IdCliente": "idCliente"
                  })

#se você passar inplace = True, voce alteara sem precisar reatribuir a um df novo.
# %%
df_transac.head(5)
# %%
#se fizer assim ele retorna uma série
# 
df_transac["idCliente"]
# %%

# só pode passar um únic objeto, dai passa uma lista que carrega outros objetos

#retorna um dataframe

df_transac[["idCliente","qtpontos"]]
# %%

# SELECT * FROM df
df_transac

# SELECT idCliente FROM df
df_transac[["idCliente"]]
# %%
# SELECT idCliente, qtPontos FROM df LIMIT 5
df_transac[["idCliente", "qtpontos"]].head(5)
# %%
## SELECT idClientem idTransacao, qtPontos FROM df LIMIT 5
#isso aqui ele retorna um dataframe novo
df_2 = df_transac[["idCliente", "idtransacao", "qtpontos"]].head(5)
# %%
df_2
# %%
colunas = df_transac.columns.to_list()
colunas
# %%
colunas.sort()
colunas
# %%
df_transac[colunas]
# %%
