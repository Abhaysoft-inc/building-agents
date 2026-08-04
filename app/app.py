from pathlib import Path
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ConfigDict

from utils import get_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    message: str = Field(alias="prompt")

@app.post("/generate")
async def generate_response(prompt:Prompt):
    return {"response": get_response(prompt.message)}


