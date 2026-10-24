#%%
import pandas as pd


df = pd.read_csv("../data/transacoes.csv", sep=";")
# %%
df.head(5)

# %%

dados = {
    "nome": ["vini", "joao","pedro"],
    "idade": [12,30,24],
    "uf": ["sp", "pr", "mg"]
}


brinquedo = pd.DataFrame(dados)
# %%
brinquedo
# %%
#%%
filtro = brinquedo["idade"] > 15
# %%
brinquedo[filtro]
# %%
df.head(5)
# %%
filtro = df["QtdePontos"] > 50
df_maior_50 = df[filtro]
# %%
df_maior_50
# %%
### esse é o filtro E -> & (*)
filtro = (df["QtdePontos"] > 50) & (df["QtdePontos"] < 120)
df[filtro]
# %%
## esse é o filtro Ou | (+)
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]
# %%
