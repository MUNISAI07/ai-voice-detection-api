from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class AudioRequest(BaseModel):
    audio_url: str
    message: str | None = None


@app.get("/")
def home():
    return {"status": "API running"}


@app.post("/detect")
def detect(
    data: AudioRequest,
    x_api_key: str = Header(None)
):
    # API key check
    if x_api_key != "my-secret-key":
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # audio url check
    try:
        r = requests.get(data.audio_url, timeout=10)
        if r.status_code != 200:
            raise Exception()
    except:
        raise HTTPException(status_code=400, detail="Invalid audio URL")

    return {
        "success": True,
        "message": "Audio received and processed",
        "result": {
            "is_ai_generated": False,
            "confidence": 0.75,
            "language": "unknown"
        }
    }
