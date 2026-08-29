from imports import *
import json

# creating a tool

def calculator(expression):
    try:
        result = eval(expression) #vulnerable
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# describing a tool (tool schema)

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluates a basic math expression and returns the result. Use this for any arithmetic calculation.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A math expression to evaluate, e.g. '25 * 4 + 10'"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


# telling the model that tools exists

messages = [
    {"role": "user", "content": "What's 15% of 200, and separately, what's 340 divided by 4?"}
]

response = groq_client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
    tools=tools,
)
response_message = response.choices[0].message

if response_message.tool_calls:
    tool_call = response_message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    result = calculator(args["expression"]) ## executing the function

    messages.append(response_message)
    messages.append({
    "role":"tool",
    "tool_call_id": tool_call.id,
    "content":result
    })

    final_response = groq_client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
    tools=tools)

    print(final_response.choices[0].message.content)
else:
    print(response_message.content)
