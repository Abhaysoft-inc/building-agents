# calling simple messages to the llm

import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

llm_url = os.getenv("LLM_URL")
openrouter_key = os.getenv("OPENROUTERKEY")

resp = requests.post(
    url=llm_url,
    headers={
       "Authorization": f"Bearer {openrouter_key}",
    },
    data=json.dumps({
        "model": "openai/gpt-oss-20b:free",
        "messages": [
      {
        "role": "user",
        "content": "Who are you"
      }
    ]
    })
)

print(resp.json())