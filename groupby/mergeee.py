#%%

import pandas as pd
# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
# %%
#transacoes é a da esquerda e puxa a da direita(clientes)  tipo um proc da transacoes na clientes
#left join
# o default é inner join -> só pega linhas que encontra em ambas as tabelas
#o on é por qual coluna ele vai fazer o join

#colunas repetidas - mesmo nome vai ficar com X e Y sacou?


#%%
clientes.columns

#%%
transacoes.columns
#%%
transacoes.rename(columns={'IdCliente': 'idCliente', 'QtdePontos': 'qtdePontos' },inplace=True)
#%%


### transacoes base da verdade -> busca (right) na clientes, como -> left join, inner.

transacoes.merge(right=clientes, 
                 how='left', 
                 on=['idCliente'], 
                 suffixes=["_Transacao", '_Clientes'])

# %%
df_1 = pd.DataFrame({
    "transacao": [1, 2, 3, 4, 5],
    "nome": ['t1','t2','t3','t4','t5'],
    "idCliente": [1, 2, 3, 2, 2],
    "valor": [10, 45, 32, 17, 87],
})

df_2 = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "nome": ["teo", "nah", "mah", "jose"],
})
# %%
df_1.merge(df_2,
          left_on=["idCliente"],
          right_on=["id"],
          how="left",
          suffixes=["_transacao", "_clientes"]
          )
# %%
