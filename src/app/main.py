from pymongo import MongoClient
from fastapi import FastAPI
import os
from dotenv import dotenv_values

from models.chatbots import Conversation, Message

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

# Load .env from root
config = dotenv_values(os.path.join(BASE_DIR, ".env"))
app = FastAPI()

@app.get("/")
def read_root():
    return "Debate Bot"


@app.post("/conversation/", response_model=Conversation)
async def create_conversation(conversation: Conversation):
    conversation_id = conversation.conversation_id

    # if conversation_id in 

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
