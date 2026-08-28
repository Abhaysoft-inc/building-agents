import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.client import groq_client
import os

def bad_prompt(task):
    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role":"system", "content":"give the output strictly in JSON format and not any other"},
            {"role": "user", "content": task}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    task = "Extract the important info from this: 'John Smith ordered 3 units of product SKU-4471 on March 12th, paid $89.97, shipping to 221 Baker Street.'"
    print(bad_prompt(task))