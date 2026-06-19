#%%


import pandas as pd

idades = [32,44,12,54,77,90,33,12,14,45,20,11]

idades = pd.Series(idades)


# %%

#agregação

idades.sum()
# %%
idades.min()
# %%
idades.mean()
# %%
idades.describe()
# %%
cliente = pd.read_csv("..//data/clientes.csv", sep=";")
# %%
pessoas_que_possuem_twitch = cliente["flTwitch"].sum()
proporção = cliente["flTwitch"].mean()
# %%
proporção

#%%
cliente.columns
# %%
redes_sociais = ['flEmail', 'flTwitch', 'flYouTube', 'flBlueSky',
       'flInstagram']

cliente[redes_sociais]
# %%
##se aplicar uma média em uma série, ele retorna a agregação daquela série se aplica num dataframe ele vai retornar
##a média em cada uma das colunas do dataframe

cliente[redes_sociais].mean()
# %%
cliente[redes_sociais].sum()
# %%
filtro_cliente = cliente.dtypes == "str"

filtro_2 = cliente.dtypes[~(cliente.dtypes == "str")].index.tolist()
# %%
cliente[filtro_2].mean()
# %%
cliente[filtro_2].describe()
# %%
