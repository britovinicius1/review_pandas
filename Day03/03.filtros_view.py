#%%
import pandas as pd

clientes = pd.read_csv("../dados/clientes.csv", sep=";")

clientes.head()
# %%
filtro = clientes['qtdePontos'] == 0

clientes_0 = clientes[filtro].copy()
# %%
clientes['Flag_1'] = 1
# %%
clientes_0
# %%
#quando a gnt faz um filtro em um dataframe ele não retorna uma cópia das linhas filtradas
# ele cria um view ele apota pra mesmas linhas do dataframe porem com o filtro q c quer
#

 

