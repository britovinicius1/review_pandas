#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
# %%
clientes
# %%
clientes.head(5)
# %%
def get_last_id(x):
    return x.split("-")[-1]


#%%
##recebe cada elemento -> percorre a serie
clientes["novo_id"] = clientes["idCliente"].apply(get_last_id)


##aplica transformações linha a linha, elemento a elemento
# %%
clientes
 # %%
