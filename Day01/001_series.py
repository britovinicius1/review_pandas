#%%
## Comentarios ->> a serie converte tudo para o mesmo tipo.
## As series tem alguns metodos


import pandas as pd

pd.Series()

# %%
idades = [
    30,
    31,
    32,
    25,
    40,
    55
]

media = sum(idades)/len(idades)
print(media)

# %%
series_idades = pd.Series(idades)
series_idades

# %%
media_idades = series_idades.mean()
variancia_idades = series_idades.var()

summar_idades = series_idades.describe()

print(summar_idades)

# %%
### Importe os indices de uma serie funciona da mesma forma que chaves de um dicionário, nao existe a chave -1
#o indice fica vinculado aquela linha e elemento da série
#pode ter dois indices iguais apontando por numeros diferetnes

#agora olha pra indice como posição e não chave
series_idades.iloc[-1]
# %%

series_idades.iloc[4:]

# %%
index = ["Vini", "josefino", "pertu", "doido", "cremoso", "tt"]
serie_nova = pd.Series(idades,index=index)

##loc é default pra series -> navega nos indices e iloc navega nas linhas
# %%
serie_nova.loc["Vini"]
# %%
