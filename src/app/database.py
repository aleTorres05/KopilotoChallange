import os
from dotenv import dotenv_values
from pymongo import MongoClient


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

config = dotenv_values(os.path.join(BASE_DIR, ".env"))


class Database:
    client: MongoClient = None  
    db = None

db = Database()

async def connect_to_mongo():
    db.client = MongoClient(config["MONGODB_CONNECTION_URI"])
    db.db = db.client[config["DB_NAME"]]
    print("✅ Connected to MongoDB")

async def close_mongo_connection():
    db.client.close()
    print("❌ MongoDB connection closed")
