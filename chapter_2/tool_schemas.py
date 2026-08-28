# the model has never seen your Python code
# It doesn't know what calculator() actually does internally — it only knows what you told it via the description field.

# description is the goat here

# Rule of thumb: a good tool description answers two questions — what does this do, and when should you reach for it — not just the first one.

# each param has its own desc, 

# "expression": {
#     "type": "string",
#     "description": "A math expression to evaluate, e.g. '25 * 4 + 10'"
# }

# "required": ["expression"]

# tells model to which param to absolutely fill in before calling the tool


from imports import *
import json

def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

vague_tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "does math",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string"}
                },
                "required": ["expression"]
            }
        }
    }
]

precise_tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluates arithmetic expressions with numbers. Use this whenever the user's question requires computing a numeric result, including percentages, totals, differences, or any calculation — even if phrased as a word problem.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A valid Python math expression using digits and operators only, e.g. '150 * 0.15' or '(340 - 100) / 4'. Convert any word-based numbers to digits first."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

def test_question(question, tools, label):
    messages = [{"role": "user", "content": question}]
    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools,
    )
    msg = response.choices[0].message

    print(f"\n[{label}] Question: {question}")
    if msg.tool_calls:
        args = json.loads(msg.tool_calls[0].function.arguments)
        print(f"  → Called calculator with: {args.get('expression')}")
    else:
        print(f"  → Did NOT call the tool. Answered directly: {msg.content}")

if __name__ == "__main__":
    tricky_questions = [
        "If a shirt costs eighty dollars and there's a fifteen percent discount, what do I pay?",
        "What's 340 divided by 4?",
        "How many minutes are there in three and a half hours?",
    ]

    for q in tricky_questions:
        test_question(q, vague_tools, "VAGUE")
        test_question(q, precise_tools, "PRECISE")

