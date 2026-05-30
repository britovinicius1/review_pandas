#%%
import pandas as pd
import sqlalchemy
from urllib.parse import quote_plus
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os
#%%
load_dotenv()
senha = quote_plus(os.getenv("DB_SENHA"))
engine = sqlalchemy.create_engine(f"mysql+pymysql://root:{senha}@localhost:3306/olist")
#%%
clientes = pd.read_sql("SELECT * FROM olist_customers LIMIT 10", engine)


# %%
clientes
# %%
clientes.head()
# %%
clientes.shape
# %%
clientes.info()
# %%
clientes.describe()
# %%
#
estados = clientes[['customer_state']].sort_values(by='customer_state')
# %%
#%%
estados
#%%

estados.loc[3]

# %%
