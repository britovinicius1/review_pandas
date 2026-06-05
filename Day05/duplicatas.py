#%%
import pandas as pd
df = pd.DataFrame({
    "nome": ["teo", "lara", "nah", "bia", "mah", "lara", "mah", "mah"],
    "sobrenome": ["calvo", "calvo", "ataide", "ataide", "silva", "silva", "silva", "silva"],
    "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134]
})


#%%
df
#%%
#ele mantem a primeira
df.drop_duplicates(subset=["nome", "sobrenome"], keep="last")
# %%
df = df.sort_values("salario", ascending=False)
#%%
df

# %%
df.drop_duplicates(subset=["nome","sobrenome"], keep="last")
# %%
df = (df.sort_values(by="salario", ascending=False)
      .drop_duplicates(keep="last",subset=["nome","sobrenome"]))
# %%
df
# %%
