#%%
import pandas as pd



df_clientes = pd.read_csv("../data/clientes.csv", sep=";")



# %%
df_clientes.head(10) ### igual ao limit
# %%
df_clientes.tail(2) ##ler o final da tabela
# %%
#cico valores alieatóriso
df_clientes.sample(5)    #pega registros aleatórios
# %%
i,j = df_clientes.shape
print(i)             #pega as linhas e colunas
# %%
df_clientes.columns      #pega as colunas
# %%
df_clientes.index   ###pega os indices
# %%
#object -> tipo generico, que na maioria das vezes é string, em geral é string
df_clientes.info(memory_usage="deep")
# %%
df_clientes.dtypes      ## traz como uma série

# %%
df_clientes.dtypes["idCliente"]
# %%
