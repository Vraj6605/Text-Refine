from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from model import model
from prompt import prompt
from parser import parser

app = FastAPI(
    title="Text Refine API",
    description="API for refining and improving text",
    version="1.0.0"
)

# Create the chain
chain = prompt | model | parser


# Request and Response models
class TextRequest(BaseModel):
    text: str


class TextResponse(BaseModel):
    original_text: str
    refined_text: str


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Text Refine API is running", "status": "healthy"}


@app.post("/refine", response_model=TextResponse)
async def refine_text(request: TextRequest):
    """
    Refine and improve the given text
    
    - Improves clarity and readability
    - Fixes grammar and spelling mistakes
    - Makes the tone professional and natural
    - Keeps the message concise
    - Preserves the original intent
    - improve sentence
    """
    result = chain.invoke(input={"text": request.text})
    
    return TextResponse(
        original_text=request.text,
        refined_text=result
    ).model_dump()

