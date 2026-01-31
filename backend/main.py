from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from config import *

app = FastAPI(title="🦙 Ollama Chatbot API")

# ==================== CORS ====================
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    temperature: float = 0.7

@app.get("/")
async def root():
    return {"message": "🦙 Ollama Chatbot Backend Running!", "model": OLLAMA_MODEL}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Ollama Chat Request
        payload = {
            "model": OLLAMA_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": request.message
                }
            ],
            "stream": False,
            "options": {
                "temperature": request.temperature,
                "num_predict": MAX_TOKENS
            }
        }
        
        print(f"🤖 Sending to Ollama: {request.message[:50]}...")
        
        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            ai_message = result["message"]["content"]
            return {"response": ai_message}
        else:
            raise HTTPException(
                status_code=500,
                detail=f"Ollama Error: {response.status_code} - {response.text}"
            )
            
    except requests.exceptions.ConnectionError:
        raise HTTPException(
            status_code=503,
            detail="❌ Ollama not running! Run: ollama serve"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
