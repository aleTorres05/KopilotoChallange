from typing import List, Optional, Union
from pydantic import BaseModel


class Message(BaseModel):
    role: str = "user"
    message: str

class Conversation(BaseModel):
    conversation_id: Optional[str] = None
    message: Optional[Union[List[Message], str]] = None
