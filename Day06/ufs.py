
#%%
import pandas as pd
import requests
from io import StringIO

headers = {"User-Agent": "Mozilla/5.0 (compatible; meu-script/1.0)"}

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

response = requests.get(url, headers=headers)
dfs = pd.read_html(StringIO(response.text))

# %%
uf = dfs[1]
# %%
uf.dtypes
# %%
def str_to_float(x):
    x = float(x.replace(" ", "")
              .replace(",",".")
              .replace("\xa0", ""))
    return x



# %%
#aplica linha a linha o tratamento
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)

#%%
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
# %%
uf.dtypes
# %%
uf
# %%
def exp_to_anos(exp):
    return float(exp.replace(",", ".").replace(" anos",""))

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)
# %%
def uf_to_regiao(uf):
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return "Norte"
    elif uf in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"

# %%
uf["Regiao"] = uf["Unidade federativa"].apply(uf_to_regiao)

# %%
uf
# %%
uf.columns
#%%
uf.dtypes
# %%
def mortalidade_to_float(x):
    x = float(x.replace("‰","").replace(",","."))
    return x

uf["Mortalidade infantil (2016)/1000"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)

# %%
uf
# %%
uf.iloc[0]
#%%
uf.dtypes


# %%
def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and linha["Mortalidade infantil (2016)/1000"] < 15 and linha["IDH (2010)"]>700)


#%%
uf["IDH (2010)"] = uf["IDH (2010)"].astype(float)
#%%
#assim ele aplica nas linhas
#recebe linha a linha
#a onde a linha vem em formato de series e os indices da linhas são as colunas

uf.apply(classifica_bom, axis=1)

# %%
uf.dtypes
# %%
