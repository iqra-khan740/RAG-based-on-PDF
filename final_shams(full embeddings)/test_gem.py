from dotenv import load_dotenv, find_dotenv
import os

# Load .env file (explicit path)
load_dotenv(find_dotenv())

# Check key
api_key = os.getenv("GOOGLE_API_KEY")
print("Loaded key:", api_key)

import google.generativeai as genai

# Configure Gemini with your key
genai.configure(api_key=api_key)


model = genai.GenerativeModel(model_name="gemini-1.5-flash")


response = model.generate_content("Hello Gemini! Are you working?")
print(response.text)
