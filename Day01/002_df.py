#%%
import pandas as pd
nomes = [
    "Lucas", "Mariana", "Felipe", "Juliana", "Rafael",
    "Amanda", "Bruno", "Fernanda", "Gustavo", "Larissa"
]

idades = [23, 17, 34, 28, 45, 19, 52, 31, 26, 40]

serie_idades = pd.Series(idades)
serie_nome = pd.Series(nomes)


for i in range(len(idades)):
    print(nomes[i], idades[i])

for nome,idade in zip(nomes,idades):
    print(nome,idade)

# %%
#dataframe varal onde coloca as series
df = pd.DataFrame()
# %%
df['idades'] = serie_idades
df['Nomes'] = serie_nome
df
# %%
#retornando a linha
df.iloc[3]

# %%
