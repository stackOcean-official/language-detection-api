from fastapi import Depends, FastAPI
from pydantic import BaseModel

from app.api import Input, Output, get_api_key
from app.language_detection import handle_detect_language_request

app = FastAPI(dependencies=[Depends(get_api_key)])

@app.post("/")
async def detect_language(input: Input) -> Output:
    return handle_detect_language_request(input)
