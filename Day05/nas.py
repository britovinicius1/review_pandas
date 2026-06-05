#%%
import pandas as pd
clientes = pd.read_csv("..//data/clientes.csv", sep=';')
clientes
# %%
#ele vai remover as linhas que tem ao menos um na
#cria uma view

clientes = clientes.dropna()
# %%
#regra pra excluir NA
# %%
#pq o criterio pra dropa na agora tem que ser a linha inteira
#padrao é any se encontra pelo menos uma ele dropa
clientes.dropna(how="all")

# %%
df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453, 4324, None, 5423],
    }
)
df
# %%
#remove só aonde a idade esta sendo NA
df.dropna(how="all", subset=['idade'])
# %%
df
# %%
# %%
#ao menos uma
df.dropna(how="any", subset=['nome', 'idade'])
# %%
#fill na
df['idade'] = df['idade'].fillna(0)
# %%
df
# %%
df.fillna(0)
# %%
df.fillna({'nome': 'alguem', 'idade':0})
# %%
medias = df[['idade', 'salario']].mean()

#%%

medias

#%%
df = df.fillna({'nome': 'alguem'})
# %%
df = df.fillna(medias)
# %%
df
# %%
df['nome'] = df['nome'].fillna('Alguem')

# %%
df
# %%
