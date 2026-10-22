from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from services.chatbot import get_ai_response
from services.speech_to_text import transcribe_audio
from services.browser_tts import generate_speech

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="AI Voice Assistant API",
    description="Backend API for the AI Voice Chatbot",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def home():
    return {
        "message": "AI Voice Assistant API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = get_ai_response(
        request.message
    )

    return {
        "response": response
    }
    
@app.post("/api/transcribe")
async def transcribe(file: UploadFile = File(...)):

    audio_bytes = await file.read()

    text = transcribe_audio(
        audio_bytes
    )

    return {
        "text": text
    }
    
class VoiceRequest(BaseModel):
    text: str


@app.post("/api/voice")
def voice(request: VoiceRequest):
    audio = generate_speech(request.text)

    return StreamingResponse(
        audio,
        media_type="audio/mpeg"
    )
    