# assigning a model an identity, expertise level, personality via system message

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.client import groq_client
import os


def terse_se(question):
    response = groq_client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
        messages=[
            {"role":"system",
             "content": "You are a terse senior engineer who values brevity over explanation."},
             {"role":"user",
              "content":question}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


def teacher(question):
    response = groq_client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
        messages=[
            {"role":"system",
             "content": "You are a patient teacher explaining to a complete beginner"},
             {"role":"user",
              "content":question}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    question = input("Ask your question: ")
    print("\n--- terse OUTPUT ---")
    print(terse_se(question))
    print("\n--- teacher OUTPUT ---")
    print(teacher(question))