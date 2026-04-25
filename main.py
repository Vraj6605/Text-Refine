from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, change to specific URLs in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
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
def root():
    """Health check endpoint"""
    return {"message": "Text Refine API is running", "status": "healthy"}


@app.post("/refine", response_model=TextResponse)
def refine_text(request: TextRequest):
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

