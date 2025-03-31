import os
from dotenv import dotenv_values
from pymongo import MongoClient


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

config = dotenv_values(os.path.join(BASE_DIR, ".env"))


class Database:
    client: MongoClient
    db = None


db = Database()


async def connect_to_mongo():
    db.client = MongoClient(os.environ.get("MONGODB_CONNECTION_URI"))
    db.db = db.client[os.environ.get("DB_NAME")]
    print("✅ Connected to MongoDB")


async def close_mongo_connection():
    db.client.close()
    print("❌ MongoDB connection closed")
