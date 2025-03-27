from typing import List, Optional
from pydantic import BaseModel


class Message(BaseModel):
    role: str 
    message: str

class Conversation(BaseModel):
    conversation_id: Optional[str]
    message: List[Message] 