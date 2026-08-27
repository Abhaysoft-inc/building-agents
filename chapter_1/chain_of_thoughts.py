import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.client import groq_client
import os


def direct_answer(question):
    response = groq_client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
            messages=[
                {"role": "system", "content": "Answer with just the final answer, no explanation."},
                {"role": "user", "content": question}
            ],
            temperature=0.3,
        )
    return response.choices[0].message.content

def chain_of_thought(question):
    response = groq_client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
            messages=[
            {
                "role": "system",
                "content": "Think step by step. Show your reasoning, then on a new line write 'Final Answer: <answer>'."
            },
            {"role": "user", "content": question}
        ],
            temperature=0.3,
        )
    return response.choices[0].message.content

if __name__ == "__main__":
    review = input("Question: ")
    print("\n--- DIRECT ANSWER OUTPUT ---")
    print(direct_answer(review))
    print("\n--- CoT ANSWER OUTPUT ---")
    print(chain_of_thought(review))
