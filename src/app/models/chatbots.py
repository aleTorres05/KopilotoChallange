from typing import List
from pydantic import BaseModel, Field


class Message(BaseModel):
    role: str 
    message: str

class Conversation(BaseModel):
    conversation_id: str
    message: List[Message] 