# Zero Shot Prompting
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Zero Shot Prompting : Directly giving instruction to the model
SYSTEM_PROMPT = "You are an expert Mathematics assistant. Your role is to answer questions exclusively related to Mathematics. If a user asks a question outside the scope of Mathematics, politely respond with: Sorry, I can only assist with Mathematics-related queries"

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
            "content":"What is an Operating System (OS) in Computer Science?"
        }
    ],
    temperature=0.0,
)
print(response.choices[0].message.content)