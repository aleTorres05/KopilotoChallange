from fastapi import Security, HTTPException
from starlette import status
from dotenv import load_dotenv
from fastapi.security import api_key
import os
import base64

api_key_header = api_key.APIKeyHeader(name="X-API-KEY")


async def validate_api_key(api_key: str = Security(api_key_header)):
    load_dotenv()

    encode_api_key = base64.b64decode(api_key.encode("ascii"))
    encode_api_key = encode_api_key.decode("ascii")
    if encode_api_key != os.getenv("TEMP_API_KEY"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized - API Key is wrong",
        )
    return None
