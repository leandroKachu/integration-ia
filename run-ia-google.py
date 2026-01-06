import os
import time
import sys
import uuid
import markdown2


from dotenv import load_dotenv
from google import genai
from weasyprint import HTML

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet




load_dotenv()
key = os.getenv("KEY_API")
client = genai.Client(api_key=key)

def animated_print(msg, width=60, delay=0.01):
    for i  in range(1, width + 1):
        sys.stdout.write("\r" + "="* i)
        sys.stdout.flush()
        time.sleep(delay)
    
    print()
    print(msg.center(width))
    print("=" * width + "\n")

def animated_input(text,delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

    values = ""


def generate_pdf(markdown_text):
    file_id = uuid.uuid4().hex[:7]

    html = markdown2.markdown(markdown_text)
    HTML(string=html).write_pdf(f"response_{file_id}.pdf")


while True:

    values = ""
    animated_input("Digite sua pergunta: ")
    values = input()
    
    if values == "sair" or values == "exit"or values == "": 
        animated_print( "obrigado até ")
        break

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=values,
    )
    
    values = input("Quer um pdf da resposta ? S/N: ")
    if values.lower() == "s" or values.lower() == "sim":
        generate_pdf(response.text)
    if values.lower() == "n" or values.lower() == "nao" or values.lower() == "não":
        print(response.text)

    animated_print("digite enter para sair")

