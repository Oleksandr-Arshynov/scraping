import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://oleksandr:dnkUq22IrgB7cDyq@cluster0.tgvrxhn.mongodb.net/my_db?retryWrites=true&w=majority&appName=Cluster0")

db = client.my_db

collection_a = db.authors_scrapy
collection_q = db.quotes_scrapy

# Відкриття файлу JSON та завантаження даних у базу даних
with open("authors.json") as f:
    data_a = json.load(f)
    collection_a.insert_many(data_a)

with open("quotes.json") as f:
    data_q = json.load(f)
    collection_q.insert_many(data_q)
