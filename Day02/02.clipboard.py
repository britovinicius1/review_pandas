#%%

import pandas as pd
import requests 
df = pd.read_clipboard()
# %
df
# %%

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

df2 = pd.read_html(response.text)
df2
# %%
df2
# %%
