from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = input()

response = client.models.generate_content(model="gemini-3-flash-preview",contents=prompt)

print(response.text)