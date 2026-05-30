#%%
import pandas as pd
import numpy as np
df = pd.read_csv("../dados/clientes.csv", sep=";")
df
# %%
#serie pode contar como um vetor
df['qtdePontos_100'] = df['qtdePontos'] + 100

df
# %%
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]

df.head()

# %%
df['qtdeSocial'] = df['flEmail'] + df['flTwitch'] + df['flYouTube'] + df['flBlueSky'] + df['flInstagram']

# %%
df['qtdePontos'].describe()
# %%
df['log_pontos'] = np.log(df['qtdePontos'] +1)
# %%
df["log_pontos"].describe()
# %%
import matplotlib.pyplot as plt

plt.hist(df["qtdePontos"])
plt.grid(True)
plt.show()
# %%
plt.hist(df["log_pontos"])
plt.grid(True)
plt.show()
# %%
