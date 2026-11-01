#%%
import pandas as pd
import sqlalchemy
from urllib.parse import quote_plus
from sqlalchemy import inspect
from sklearn import cluster
from sqlalchemy import text

with open("order_items.sql") as open_file:
    query = open_file.read()

print(query)
# %%

senha = quote_plus("like1019@")
engine = sqlalchemy.create_engine(
    f"postgresql+psycopg2://postgres:{senha}@localhost:5432/olist"
)

df = pd.read_sql_query(
    query,
    con=engine
)
#%%
df.head(2)
# %%
kmean = cluster.KMeans(n_clusters=4)
# %%
kmean.fit(df[["price"]])
# %%
df["cluster"] = kmean.labels_
df
# %%
### salvando tabela no postegres
df.to_sql("items_cluster_temp", con=engine, 
          if_exists="replace", index=False)

# %%
