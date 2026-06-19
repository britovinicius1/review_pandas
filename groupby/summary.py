#%%

import pandas as pd

# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
# %%
transacoes.head(5)
# %%
transacoes.groupby(by=["IdCliente"]).count()



# %%
transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()
# %%
summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
                        .agg(
                         {"IdTransacao": ['count'],
                          "QtdePontos": ['sum', 'mean']
                          })
                    
                    )
# %%
summary.columns
# %%
summary.columns = ['idCliente', 'qtdeTransacoes', 'totalPontos', 'avgPontos']
summary
# %%
