from imports import *
import json

# was only handlinng tool_calls[0] - the first one, and silently dropping any other

def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def get_gold_price(unit="ounce"):
    return "Current gold price: $2,678 per ounce"

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluates arithmetic expressions with numbers. Use this whenever a numeric calculation is needed.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A valid math expression using digits and operators, e.g. '150 * 0.15'"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_gold_price",
            "description": "Returns the current live price of gold. Use this whenever the question needs up-to-date gold pricing, which you cannot know from memory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "unit": {
                        "type": "string",
                        "description": "Unit to price gold in, e.g. 'ounce' or 'gram'"
                    }
                },
                "required": []
            }
        }
    }
]

# dispatch table

available_functions = {
    "calculator": calculator,
    "get_gold_price": get_gold_price,
}

