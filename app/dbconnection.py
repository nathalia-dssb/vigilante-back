import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


client = MongoClient(os.environ.get("MONGO_DB"), server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)