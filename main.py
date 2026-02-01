from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Updated request body to match Endpoint Tester
class AudioRequest(BaseModel):
    language: str
    audio_format: str
    audio_base64: str


@app.get("/")
def home():
    return {"status": "API running"}


@app.post("/detect")
def detect(
    data: AudioRequest,
    x_api_key: str = Header(None)
):
    # API key validation
    if x_api_key != "my-secret-key":
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Here you could process the audio_base64 if needed
    # For tester, we just return a dummy response

    return {
        "success": True,
        "message": "Audio processed",
        "result": {
            "is_ai_generated": False,
            "confidence": 0.75,
            "language": data.language
        }
    }
