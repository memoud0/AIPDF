from openai import OpenAI
import openai
import os
from dotenv import load_dotenv


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key is None:
    raise ValueError("OpenAI API key not found")

client = OpenAI(api_key=openai_api_key)

def get_ai_response(text):
    try:
        response = openai.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an assistant that helps with PDF content."},
                {"role": "user", "content": text}
            ],
            model="gpt-3.5-turbo",
        )
        response_message = response.choices[0].message.content
        print(response_message)
    except Exception as e:
        print(f"Error: {e}")
        return "There was an error processing your request with the AI."

def converse_with_ai(messages):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150
        )
        response_message = response.choices[0].message.content
        print(response_message)
    except Exception as e:
        print(f"Error: {e}")
        return "There was an error processing your request with the AI."
