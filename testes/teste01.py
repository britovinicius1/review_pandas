#%%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
# %%

df.shape
# %%
df.columns
# %%
df[['idCliente','qtdePontos']].sort_values(by='qtdePontos', ascending=False)
# %%

renamed_columns = {
    'idCliente': 'IDCLIENTE',
     'qtdePontos': 'QtdePontos'
}

df.rename(columns=renamed_columns, inplace=True)

# %%
df
# %%
df.columns
# %%
colunas = df.columns.to_list()
# %%
df.columns
# %%
colunas = df.columns.to_list()
# %%
colunas.sort()
# %%
colunas
# %%
df = df[colunas]
# %%
df
# %%
df.columns = df.columns.str.upper()
# %%
df
# %%
filtro = df['QTDEPONTOS'] >= 1000
# %%
df[filtro]
# %%
df
# %%

top_5 = df.sort_values(by='QTDEPONTOS', ascending=False).head(5)
# %%
top_5['IDCLIENTE']
# %%
