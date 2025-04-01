from database import db
from models.chatbots import ConversationResponse
from typing import Optional
from uuid import uuid4


collection = "conversations"

async def get_conversation(conversation_id: str) -> Optional[dict]:
    if conversation_id:
        return db.db[collection].find_one({"conversation_id": conversation_id})
    
    

async def save_conversation(conversation):
    conversation_id = conversation["conversation_id"]
    print("antes:",conversation)
    if conversation_id:    
        existing = await get_conversation(conversation_id)
        
        if existing:
            new_messages = existing["message"] + conversation["message"]
            db.db[collection].update_one(
                {"conversation_id": conversation_id},
                {"$set": {"message": new_messages}}
            )
        else:
            return "This conversation does not exist"
    else:
        conversation = ConversationResponse(**conversation)
        print("despues",conversation)
        conversation_id = str(uuid4())
        conversation.conversation_id = conversation_id
        db.db[collection].insert_one(conversation.model_dump()) 

    return await get_conversation(conversation_id)
 