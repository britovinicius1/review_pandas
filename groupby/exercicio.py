#%%
import pandas as pd

##quem teve mais transacoes de streak?

# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")

produtos = pd.read_csv("../data/produtos.csv", sep=";")

#%%
produtos.head(5)
#%%
transacoes.head(5)
#%%
transacoes_produto.head(5)
# %%

# %%
cliente_transacao_produto = transacoes.merge(transacoes_produto,
                 on='IdTransacao',
                 how='left')[['IdTransacao', 'IdCliente', 'IdProduto']]
# %%
cliente_transacao_produto
# %%
df_full = cliente_transacao_produto.merge(
        produtos,
        on = ['IdProduto']
)[['IdTransacao', 'IdCliente','IdProduto', 'DescNomeProduto']]
# %%
df_full
# %%
filtro = df_full['DescNomeProduto'] == "Presença Streak"
df_full[filtro]
# %%

(df_full.groupby(by=["IdCliente"])["IdTransacao"]
                .count()).sort_values(ascending=False).head(1)
# %%

produtos_filtrado = produtos[produtos["DescNomeProduto"]=="Presença Streak"]
produtos_filtrado.rename({'DescNomeProduto':'descProduto'}, inplace=True)
produtos_filtrado_finalizado = produtos_filtrado[['IdProduto', 'DescNomeProduto']]

# %%
produtos_filtrado_finalizado
# %%
produtos.rename(columns={"IdProduto": "idProduto"}, inplace=True)
#%%
produtos_filtrado_finalizado.rename(columns={"IdProduto": "idProduto"}, inplace=True)

#%%
transacoes_produto.rename(columns={"IdProduto": "idProduto", 'idTransacaoProduto': 'IdTransacao'}, inplace=True)


#%%
transacoes_produto

#%%
(transacoes.merge(
    transacoes_produto,
    on=["IdTransacao"],
    how='left'
).merge(
    produtos_filtrado_finalizado,
    on=["idProduto"],
    how="right"
).groupby(by='idCliente')["idTransacao"].count()
)




# %%
#### teste 2#####

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")
produtos = pd.read_csv("../data/produtos.csv", sep=";")


