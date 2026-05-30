
#%%
# #ordernar
import pandas as pd
clientes = pd.read_csv("../dados/clientes.csv", sep=";")
# %%
clientes
# %%
clientes["qtdePontos"]
# %%
#o indice ordena junto com o valor
clientes["qtdePontos"].sort_values()
# %%
max_pontos = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_pontos
clientes[filtro]
# %%
#isso aqui nao altera ro proprio dataframe
#sorte_values retorna um df novo
top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
            .head(5)["idCliente"])

# %%
top_5
# %%
type(top_5)
# %%
#dataframe para teste
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario": [2345, 4533, 3245, 4533],
    }
)
#%%
brinquedo.sort_values(by=["salario", "idade"], ascending=[False,True])

# %%
