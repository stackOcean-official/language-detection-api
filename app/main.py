from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    text: str

app = FastAPI()


@app.post("/")
async def detect_language(input: Input):
    print('Incoming request with text "{}"'.format(input.text))
    # Return mock data
    return {"language": "de"}