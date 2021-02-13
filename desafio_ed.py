import pymongo
from pymongo import MongoClient
import pandas as pd
import numpy as np
import json
from sqlalchemy import create_engine
import requests
#connect with MongoDB
# client = pymongo.MongoClient("mongodb+srv://estudante_igti:SRwkJTDz2nA28ME9@unicluster.ixhvw.mongodb.net/ibge?retryWrites=true&w=majority")

# db = client.ibge
# records = db.pnadc20203
# df=pd.DataFrame(list(records.find()))
# df.to_csv("/workspace/desadio-ed/data/pnadc20203.csv", index=False, encoding="utf-8,", sep=";")
#df.to_csv("/workspace/desadio-ed/data/pnadc20203.csv")

# res = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/MG/mesorregioes")
# resjson=json.loads(res.text)
# df2=pd.DataFrame(resjson)[["id","nome"]]
# df2.to_csv("/workspace/desadio-ed/data/dimensao_mesorregioes_mg.csv")


#print your collection
#print(list(records.find()))
pnadc=pd.read_csv("/workspace/desadio-ed/data/pnadc20203.csv")
mesomg=pd.read_csv("/workspace/desadio-ed/data/dimensao_mesorregioes_mg.csv")
#print(pnadc.head())
# print(pnadc.uf.value_counts())
# print(dict(pnadc.dtypes))
# print(pnadc.cor.value_counts())
# print(pnadc.loc[pnadc.renda>=0].describe())
# print((pnadc.renda=="nan").value_counts())
# print(pnadc["renda"].sum())
# print(pnadc.renda.isnull().sum())
# print(pnadc.loc[pnadc.renda].count())
# print(pnadc.renda.shape)
# print(pnadc.loc[(pnadc.uf == "Rio de Janeiro")
# ,
# "renda"

# ].describe())
# print(pnadc.loc[(pnadc.uf == "Distrito Federal")&
# (pnadc.renda>=0),
# "renda"

# ].describe())


# print(pnadc.loc[(pnadc.uf == "Rio de Janeiro")&
# (pnadc.renda>=0)
# ,
# "renda"

# ].mean())
# print(pnadc.loc[(pnadc.uf == "São Paulo")&
# (pnadc.renda>=0)
# ,
# "renda"

# ].mean())
# print(pnadc.loc[(pnadc.uf == "Minas Gerais")&
# (pnadc.renda>=0)
# ,
# "renda"

# ].mean())
# print(pnadc.loc[(pnadc.uf == "Espírito Santo")
# ,
# "renda"

# ].mean())


# print(pnadc.loc[(pnadc.uf == "Ceará"),

# "renda"

# ].mean())
# print(pnadc.loc[(pnadc.uf == "Piauí"),

# "renda"

# ].mean())
# print(pnadc.loc[(pnadc.uf == "Maranhão"),

# "renda"

# ].mean())
# print(pnadc.loc[(pnadc.uf == "Alagoas"),

# "renda"

# ].mean())


# print(pnadc.loc[(pnadc.uf == "Distrito Federal"),

# "anosesco"

# ].mean())
# print(pnadc.loc[(pnadc.uf == "São Paulo"),

# "anosesco"

# ].mean())
# print(pnadc.loc[(pnadc.uf == "Rio de Janeiro"),

# "anosesco"

# ].mean())
# print(pnadc.loc[(pnadc.uf == "Paraná"),

# "anosesco"

# ].mean())


# print(pnadc.loc[(pnadc.uf == "Mato Grosso")&(
#     pnadc.sexo=="Homem"
# ),

# "anosesco"

# ].mean())

# print(pnadc.loc[(pnadc.uf == "Paraná")&(
#     pnadc.sexo=="Mulher"
#     )&(pnadc.idade>25)&(pnadc.idade<35),

# "anosesco"

# ].mean())

print(pnadc.loc[(pnadc.uf == "Paraná")&(pnadc.renda>=0)&
   (pnadc.trab == "Pessoas na força de trabalho")
   &(pnadc.idade>=25)&(pnadc.idade<=35),

"renda"

].mean())

print(pnadc.loc[(pnadc.uf == "Santa Catarina")&(pnadc.renda>=0)&
   (pnadc.trab == "Pessoas na força de trabalho")
   &(pnadc.idade>=25)&(pnadc.idade<=35),

"renda"

].mean())

print(pnadc.loc[(pnadc.uf == "Rio Grande do Sul")&(pnadc.renda>=0)&
   (pnadc.trab == "Pessoas na força de trabalho")
   &(pnadc.idade>=25)&(pnadc.idade<=35),

"renda"

].mean())

# print(pnadc.loc[(pnadc.uf == "Minas Gerais")&
# (pnadc.renda>=0),
# "renda"

# ].sum())

# print(mesomg.describe())

# print(pnadc.loc[(pnadc.uf.isin(["Alagoas","Bahia","Ceará","Maranhão","Paraíba","Piauí","Pernambuco","Rio Grande do Norte","Sergipe"]))&(
#     pnadc.sexo=="Mulher"
#     )&(pnadc.idade>25)&(pnadc.idade<35)&(pnadc.graduacao =="Sim")&(pnadc.cor.isin(["Parda"])),

# "renda"

# ].mean())

print(pnadc.loc[(pnadc.uf.isin(["Paraná","Rio Grande do Sul","Santa Catarina"]))&(pnadc.renda>=0)&
   (pnadc.trab == "Pessoas na força de trabalho")
   &(pnadc.idade>=25)&(pnadc.idade<=35),

"renda"

].mean())