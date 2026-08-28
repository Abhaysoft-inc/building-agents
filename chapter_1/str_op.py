import os
import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from shared.client import groq_client


# forcing model to produce fixed str format

def str_ans(question):
    prompt = f"""Answer the following question and respond ONLY with valid JSON in this exact shape, no other text before or after:
    
    {{"answer": "<your answer>", "confidence": "<high|medium|low>", "reasoning": "<one short sentence>"}}

    Question: {question}

    """

    response = groq_client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
            messages=[
                {"role": "system", "content": "You are a chatty assistant who loves adding friendly commentary."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )
    raw_text = response.choices[0].message.content
    try:
        parsed = json.loads(raw_text)
        return parsed
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON", "raw_response": raw_text}

if __name__ == "__main__":
    question = input("Enter a question: ")
    result = str_ans(question)
    print(json.dumps(result, indent=2))


