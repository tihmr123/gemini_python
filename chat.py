import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1.1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="Your role is to speak like a fifth grade math teacher",
)

chat_session = model.start_chat(
    history=[]
)

print("Bot: Hello, how can I help you?")
print()

while True:
  user_input=input("You: ")
  
  response = chat_session.send_message(user_input)

  model_response = response.text
  print("Bot:",model_response)
  print()

  chat_session.history.append ({"role":"user","parts":[user_input]})
  chat_session.history.append({"role":"model","parts":[model_response]})