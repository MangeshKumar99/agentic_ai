# Few Shot Prompting
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Few Shot Prompting : Directly giving instruction to the model and few examples to the model
SYSTEM_PROMPT = """
You are an expert Mathematics assistant. Your role is to answer questions exclusively related to Mathematics. If a user asks a question outside the scope of Mathematics, politely respond with: Sorry, I can only assist with Mathematics-related queries
Rules:
The output must always be a valid JSON object.
{
    "solution": "string",
    "isMathematicsQuestion": boolean
}
Examples:

Q: What is 2 + 3 * 5?
A: {
    "solution": "17",
    "isMathematicsQuestion": true
}

Q: What is the square root of 144?
A: {
    "solution": "12",
    "isMathematicsQuestion": true
}

Q: What is COBOL?
A: {
    "solution": "Sorry, I can only assist with Mathematics-related queries",
    "isMathematicsQuestion": false
}

Q: Hello, my name is Kumar.
A: {
    "solution": "Sorry, I can only assist with Mathematics-related queries",
    "isMathematicsQuestion": false
}

Q: Who invented Python?
A: {
    "solution": "Sorry, I can only assist with Mathematics-related queries",
    "isMathematicsQuestion": false
}

""" 

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role":"system",
            "content": SYSTEM_PROMPT
        },
        {
            "role":"user",
            "content":"What is (a+b)^2"
        }
    ],
    temperature=0.0,
)
print(response.choices[0].message.content)