import os
from groq import Groq
from dotenv import load_dotenv

from services.conversation_service import get_conversation

# context: id='
async def answer_ai(message, conv_id):
    load_dotenv()
    
    message_dict = {"content": message, "role": "user"}
    if conv_id:
        conversation = await get_conversation(conv_id)
        new_conversation = [
            {"role": msg["role"], "content": msg["message"]}
            for msg in conversation["message"]
        ]
        new_conversation.append(message_dict)
        message_dict = new_conversation
        ai_answer = call_ai(message_dict, message, conv_id)
        return ai_answer
        

    else:
        message_dict["content"] = os.getenv("PROMPT") + message
        message_dict = [message_dict]
        ai_answer = call_ai(message_dict, message, conv_id)
        return ai_answer

def call_ai(message_dict, message, conv_id):
    client = Groq(api_key=os.getenv("API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=message_dict,
        model="llama-3.3-70b-versatile",
    )

    messages = [
        {"role": "user", "message": message},
        {
            "role": chat_completion.choices[0].message.role,
            "message": chat_completion.choices[0].message.content,
        },
    ]

    return {"conversation_id": conv_id, "message": messages}