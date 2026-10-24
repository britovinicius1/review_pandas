#%%
import pandas as pd

df = pd.read_excel("data/Online_Retail.xlsx")
# %%
df.head(5)
# %%

df.index
# %%
df.columns
# %%
colunas = [
    "Description",
    "Quantity",
    "UnitPrice"
]

df_copia = df[colunas]

df_copia
# %%
df_copia = df_copia.rename(columns={
    "Description": "description",
    "Quantity": "quantity",
    "UnitPrice": "unitprice"
})

# %%
df_copia.head(5)
# %%
df_copia["Vendas"] = df_copia["quantity"] * df_copia["quantity"]
# %%
df_copia
# %%
filtro = df_copia["Vendas"] > 2500000000
df_copia[filtro]
#%%
df_copia
# %%
df_copia[df_copia["quantity"] > 0]
# %%
