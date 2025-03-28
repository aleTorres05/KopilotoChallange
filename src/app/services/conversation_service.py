from database import db
from models.chatbots import Conversation
from typing import Optional
from uuid import uuid4


collection = "conversations"

async def get_conversation(conversation_id: str) -> Optional[dict]:
    if conversation_id:
        return db.db[collection].find_one({"conversation_id": conversation_id})

async def save_conversation(conversation: Conversation):
    existing = await get_conversation(conversation.conversation_id)
    
    if existing:
        new_messages = existing["message"] + conversation.message
        db.db[collection].update_one(
            {"conversation_id": conversation.conversation_id},
            {"$set": {"message": new_messages}}
        )
    else:
         conversation.conversation_id = str(uuid4())
         db.db[collection].insert_one(conversation.model_dump()) 


    return await get_conversation(conversation.conversation_id)
 