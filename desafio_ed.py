import pymongo
from pymongo import MongoClient
import pandas as pd
import numpy as np

#connect with MongoDB
client = pymongo.MongoClient("mongodb+srv://estudante_igti:SRwkJTDz2nA28ME9@unicluster.ixhvw.mongodb.net/ibge?retryWrites=true&w=majority")

db = client.ibge
records = db.pnadc20203
df=pd.DataFrame(list(records.find()))
df.to_csv("/workspace/desadio-ed/data/pnadc20203.csv", index=False, encoding="utf-8,", sep=";")

#print your collection
#print(list(records.find()))
# pnadc=pd.read_csv("/workspace/desadio-ed/data/pnadc20203.csv", sep=";")
#print(pnadc.head())
#print(pnadc.uf)
# print(dict(pnadc.dtypes))
# print(pnadc.loc[pnadc.renda>0 ].renda.describe())
# print(pnadc.renda)
# print(pnadc.renda.count())
# print(pnadc.loc[pnadc.renda>0].shape)
# print(pnadc.renda.sum())
# print(pnadc.loc[(pnadc.uf == "Distrito Federal"),

# "renda"

# ].mean())
# print(pnadc.loc[(pnadc.uf == "Distrito Federal"),

# "renda"

# ].count())