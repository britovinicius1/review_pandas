#%%
import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

# %%
#calcular a amplitude e a distancia da amplitude da média e elevar ao quadrado e tirar a raiz
## sqrtr((amplitude - mean) ** 2)

#%%

def diff_amp(x: pd.Series):
    amplitude = x.max() - x.mean()
    media = x.mean()
    return np.sqrt((amplitude - media)**2)


def life_time(x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days




# %%
idades = pd.Series([23,44,55,12,34,56,10])
diff_amp(idades)

#%%
transacoes.head(5)

# %%
analises = (
transacoes.groupby(by=["IdCliente"], as_index=False).agg({
    "IdTransacao": ["count"],
    "QtdePontos": ["sum", "mean", diff_amp],
    "DtCriacao": [life_time]
})

)
# %%
analises.columns = ["idCliente", "qtdeTransacao", "totalpontos", "mediapontos", "ampMeanDiff", "lifetime"]
# %%
analises
# %%
