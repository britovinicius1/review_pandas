#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
# %%
clientes.head(5)
# %%
filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro] ## 
clientes_0["flag_1"] = 1
# %%
clientes_0.head(5)
# %%
## quando filtra ele não faza uma cópia, ele faz uma view
## ele só aponta pra a base e olha as linhas que ta filtrada;
a = [1,2,3]
b = a

# %%
print(f"A: {a}")
print(f"B: {b}")
# %%
b.append("fodase")
# %%
print(f"A: {a}")
print(f"B: {b}")
# %%
#pra resolver cria uma cópia;
#dessa forma isola, pq cria outra lista igual só que os objetos são diferentes
A = [1,2]
B = A.copy()
# %%
filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro].copy() ### aqui ele vai desassociar
clientes_0["flag_1"]