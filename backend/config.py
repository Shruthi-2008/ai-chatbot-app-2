import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==================== LLM CONFIG ====================
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

# ==================== OPENAI FALLBACK (Optional) ====================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = "gpt-3.5-turbo"

# ==================== COMMON SETTINGS ====================
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "500"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

# ==================== CORS ====================
ALLOWED_ORIGINS = [
    "http://localhost:8501",
    "http://127.0.0.1:8501"
]

print(f"🤖 Config loaded:")
print(f"   Provider: {LLM_PROVIDER}")
print(f"   Model: {OLLAMA_MODEL}")
print(f"   Ollama URL: {OLLAMA_URL}")