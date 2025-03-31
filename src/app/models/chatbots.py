from typing import List, Optional
from pydantic import BaseModel


class Message(BaseModel):
    role: str = "user"
    message: str

class Conversation(BaseModel):
    conversation_id: Optional[str] | None
    message: List[Message] | str