from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.vigilante_db

def get_db():
    return db

def ping_db():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return True
    except Exception as e:
        print(e)
        return False
