from fastapi import FastAPI
from database import connect_to_mongo, close_mongo_connection
from routes.conversation import router as conversation_router


app = FastAPI()


@app.on_event("startup")
async def startup():
    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()


# Register routes
app.include_router(conversation_router, prefix="/conversation", tags=["Conversations"])
