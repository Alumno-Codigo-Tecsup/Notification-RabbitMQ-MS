from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    messageType: str

@app.post("/sendmessage")
async def send_message(message: Message):
    return {"status": "success", "messageType": message.messageType} 