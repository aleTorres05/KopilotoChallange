from fastapi import APIRouter, HTTPException
from models.chatbots import Conversation
from services.conversation_service import get_conversation, save_conversation

router = APIRouter()

@router.post("/", response_model=Conversation)
async def create_conversation(conversation: Conversation):
    saved_conversation = await save_conversation(conversation)
    return saved_conversation

@router.get("/{conversation_id}", response_model=Conversation)
async def read_conversation(conversation_id: str):
    conversation = await get_conversation(conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation
