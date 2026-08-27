import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from shared.client import groq_client


def zero_shot(prompt):
    response = groq_client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
        messages=[
            {"role": "user", "content":prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content

# only run the code below if you are executing this file directly (not importing from another file)

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    print("\n--- OUTPUT ---")
    print(zero_shot(prompt))

