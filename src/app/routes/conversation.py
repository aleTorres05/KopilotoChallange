from fastapi import APIRouter, HTTPException, Depends
from models.chatbots import Conversation
from services.conversation_service import get_conversation, save_conversation
from api.aiChatbot import call_ai
import middleware.middleware as auth


router = APIRouter(dependencies=[Depends(auth.validate_api_key)])


@router.post("/", response_model=Conversation)
async def create_conversation(conversation: Conversation):

    conversation_model = conversation.model_dump()
    message_to_ai = conversation_model["message"]
    conversation_id = (
        conversation_model["conversation_id"]
        if conversation_model["conversation_id"]
        else ""
    )
    ai_answer = await call_ai(message_to_ai, conversation_id)
    saved_conversation = await save_conversation(ai_answer)

    return saved_conversation


@router.get("/{conversation_id}", response_model=Conversation)
async def read_conversation(conversation_id: str):
    conversation = await get_conversation(conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation
