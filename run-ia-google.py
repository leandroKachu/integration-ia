from dotenv import load_dotenv
from google import genai

import os

load_dotenv()
key = os.getenv("KEY_API")

client = genai.Client(api_key=key)
while True:
    values = input("Digite algo (enter vazio para sair): ")
    
    if values == "sair" or values == "exit": 
        print( "obrigado até ")
        break

    if values == "":
        break

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=values,
    )
    print(response.text)




