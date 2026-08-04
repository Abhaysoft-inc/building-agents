# calling simple messages to the llm

import os
import requests
from dotenv import load_dotenv

load_dotenv()

llm_url = os.getenv("LLM_URL")
openrouter_key = os.getenv("OPENROUTERKEY")

def get_response(prompt:str):
    resp = requests.post(
        url=llm_url,
        headers={
            "Authorization": f"Bearer {openrouter_key}",
        },
        json={
            "model": "nvidia/nemotron-3-ultra-550b-a55b:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            "temperature": 1,
        },
    )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]