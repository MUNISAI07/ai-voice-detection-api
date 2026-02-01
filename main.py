from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class AudioRequest(BaseModel):
    language: str
    audio_format: str = Field(..., alias="audioFormat")
    audio_base64: str = Field(..., alias="audioBase64")

    class Config:
        allow_population_by_field_name = True


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

    # Here you could process audio_base64 if needed
    return {
        "success": True,
        "message": "Audio processed",
        "result": {
            "is_ai_generated": False,
            "confidence": 0.75,
            "language": data.language
        }
    }
