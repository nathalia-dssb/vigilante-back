import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nathdsbb:u5zX3PSEqDjd60kt@vigilante.eoponc3.mongodb.net/?retryWrites=true&w=majority&appName=vigilante"


client = MongoClient(uri, server_api=ServerApi('1'))
database = client.vigilante_db
collection = database.alerts

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

except Exception as e:
    print(e)

async def get_one_alert(id):
    alert = await collection.find_one({"_id": id})
    return alert
