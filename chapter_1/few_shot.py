# we show some example to the llm to understand better

# its not enough for reasoning tasks, rag, 

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.client import groq_client
import os

def few_shot(review):
    examples_prompt = f"""Classify the sentiment of each review as Positive, Negative, or Neutral.

Review: "This product changed my life, absolutely love it!"
Sentiment: Positive

Review: "It broke after two days. Waste of money."
Sentiment: Negative

Review: "It's fine, does what it says."
Sentiment: Neutral

Review: "{review}"
Sentiment:"""

    response = groq_client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
        messages=[
            {"role": "system", "content": "You classify sentiment. Respond with only one word."},
            {"role": "user", "content": examples_prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    review = input("Enter a review to classify: ")
    print("\n--- FEW-SHOT OUTPUT ---")
    print(few_shot(review))