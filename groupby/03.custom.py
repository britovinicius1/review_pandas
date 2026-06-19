#%%
import pandas as pd
import numpy as np

#%%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
#%%
transacoes.head(5)
# %%
## raiz((amplitude - mean )**2)

def dif_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media) ** 2)


idades = pd.Series([21,33,44,55,12,44,39,10,112,19,5,3])

dif_amp(idades)


#%%
def life_time(x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days


# %%
summary = transacoes.groupby(by=["IdCliente"], as_index=False).agg(
        {
            "IdTransacao" : ["count"],
            "QtdePontos": ["sum", "mean", dif_amp],
            "DtCriacao" : [life_time]
        }
)
# %%
summary.columns
# %%
summary.columns = ["idCliente", "qtdeTransacao", "totalPontos", "mediaPontos", 
                "ampMeanDiff", 'lifeTime']
# %%
summary
# %%
