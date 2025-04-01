from typing import List, Optional
from pydantic import BaseModel, model_validator


class Message(BaseModel):
    role: str = "user"
    message: str

class ConversationRequest(BaseModel):
    conversation_id: Optional[str] = None
    message: Optional[str] = None  

class ConversationResponse(BaseModel):
    conversation_id: str
    message: List[Message] 