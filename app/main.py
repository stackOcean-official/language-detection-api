from fastapi import FastAPI, HTTPException

import fasttext
from fasttext import tokenize
from pydantic import BaseModel
import re
import os

app = FastAPI()

fasttext_language_model = fasttext.load_model(os.path.join("model", "lid.176.ftz"))

white_space_pattern = re.compile(r"\s")


def preprocess_text_for_language_detection(text: str):
    """
    Cleans the text as per fasttext requirements.
    The requirements can be found here: https://pypi.org/project/fasttext/
    
    :text: str: text to clean
    :returns: str: cleaned text
    """
    # fastText assumes UTF-8 encoded text
    text = str(text)
    
    # fastText is not aware of UTF-8 whitespace
    # Replace all white space with space
    text = white_space_pattern.sub(text, " ")
    
    # Tokenize text, per fastext function and rejoin
    tokens = tokenize(text)
    text = " ".join(tokens)
    n = len(tokens)
    
    # Remove white space char as it affects the model accuracy
    text = text.replace("</s>", "")
    
    return text.lower()

class Input(BaseModel):
    text: str

class Output(BaseModel):
    language: str

@app.post("/")
async def detect_language(input: Input) -> Output:

    threshold = 0.0
    no_of_languages = 1
    text = input.text
    if len(text) == 0:
        raise HTTPException(status_code=406, detail="Text field is empty")
    clean_text = preprocess_text_for_language_detection(text)
    if len(clean_text) == 0:
        raise HTTPException(status_code=406, detail="Cleaned text is empty")
    ft_output = fasttext_language_model.predict(clean_text, no_of_languages, threshold=threshold)
    # format output
    result = [(ft_output[0][i][-2:], ft_output[1][i]) for i in range(len(ft_output[0]))]
    # return first language
    return {"language": result[0][0]}
