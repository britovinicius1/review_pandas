#%%

import pandas as pd

df_clientes = pd.read_csv("../dados/clientes.csv", sep=";")

#### AMOSTRAS ####
# %% ## tipo o limit do sql
df_clientes.head(5)
df_clientes.tail(2)
# %% amostra aleatória
df_clientes.sample(15)
# %%#atributo do datafrme
i,j = df_clientes.shape


# %% ##atributo
df_clientes.columns
# %%
df_clientes.index
# %%
df_clientes.info(memory_usage="deep")
# %%
##object é um tipo generico mas na maioria das vezes é string, é o tipo mais generico. Tipo pode ser uma coluna de listas;
df_clientes.dtypes
# %%
