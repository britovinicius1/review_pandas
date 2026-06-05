#%%
import pandas as pd

data = {
    'Classe': ['Júnior', 'Júnior', 'Pleno', 'Pleno', 'Sênior', 'Sênior'],
    'Nome':   ['Jorge', 'Carlos', 'Roberta', 'Patrícia', 'Bruno', 'Vera'],
    'Venda':  [200, 120, 340, 124, 243, 350]
}

df = pd.DataFrame(data)
df
# %%

df.groupby("Classe").max()


# %%
df2 = df.copy()

# %%
df2
# %%
df2["Venda"] = [150,432,190,230,410,155]
# %%
df2
# %%
df3 = pd.concat([df, df2])
# %%
df3
# %%
df3.groupby("Classe")[["Venda"]].sum()
# %%
