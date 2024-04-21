import os
import google.generativeai as genai
from dotenv import load_dotenv
import os

genAI = genai.configure(api_key=os.getenv("api_key"))

def configure():
  load_dotenv()

def run():
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("5 times 5")
    if response.parts:
      text = response.parts[0].text
      print(text)
    else:
      print("Response was blocked or no content was returned.")
run() 
