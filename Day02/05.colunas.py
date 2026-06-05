#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
#%%
df.shape
# %%
df.dtypes
# %%
## renomear coluna ###
## esse tipo de rename precisa atribuir ao df;

renamed_columns = {
        "QtdePontos" : "qtPontos",
        "DescSistemaOrigem": "SistemaOrigem"
    }
#df = df.rename(columns=renamed_columns)
df.rename(columns=renamed_columns, inplace=True) #-> Altera sem precisar reatribuir

# %%
df
# %%
## Pegar colunas ##
# So pode passar um unico objeto pra dentro do dataframe, então passa uma lista que é um unico objeto carrega varios elementos

df[["IdCliente",'qtPontos']]
# %%
df[["IdCliente",'qtPontos']].head(5)
# %%
colunas = df.columns.to_list()
colunas.sort()
colunas
# %%
df = df[colunas]
df
# %%
