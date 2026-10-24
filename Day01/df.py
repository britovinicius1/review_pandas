#%%
################################ TEORIA #############################
# O dataframe é um conjunto de séries
# séries -> coluna do excel
# dataframe(mesma coisa que uma planilha do excel) - Planilha é o dataframe e cada coluna é uma serie
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

nomes = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

# %%
series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
#%%
df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
# %%
type(df)
# %%
df["nomes"]

# %%
df["idades"]
# %%
### acessando linha de um df -> quando passa iloc para um dataframe iloc -> vc pega a linha e os indices é as colunas vira uma série
# indices vira a coluna
print(df.iloc[-1]["idades"])
# %%
 