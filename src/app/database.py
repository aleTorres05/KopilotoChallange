import os
from dotenv import load_dotenv
from pymongo import MongoClient


class Database:
    client: MongoClient
    db = None


load_dotenv()
db = Database()


async def connect_to_mongo():
    db.client = MongoClient(os.getenv("MONGODB_CONNECTION_URI"))
    db.db = db.client[os.getenv("DB_NAME")]
    print("✅ Connected to MongoDB")


async def close_mongo_connection():
    db.client.close()
    print("❌ MongoDB connection closed")
