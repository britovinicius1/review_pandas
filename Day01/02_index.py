#%%
#serie tem dtype



import pandas as pd

lista = [2,3,4]
indice = ["a","b","c"]

serie_teste = pd.Series(lista, index=indice)


idades = [
    30,
    22,
    44,
    45,
    30,
    20,
    12,
    33,
    14,
    15
]
series_idades = pd.Series(idades)
# %%
series_idades
# %%
# indice e valor (series)
# os indices da series funciona da mesma maneira que as chaves do dicionario
# os indices são associados ao valor - ele é vinculado ao elemento da série [tipo um id]

# iloc -> quando coloca iloc agora usa indice em posição/olha na ordem das linhas (igual lista) o padrão é CHAVE
## loc é o default pra series
# loc -> usa como chave
series_idades.iloc[-1] ### IGNORA AS CHAVES E OLHA POR POS
# %%
series_idades.iloc[::-1]
series_idades.loc[0]

# %%

