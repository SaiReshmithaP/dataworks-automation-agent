import openai
import os

openai.api_key = os.getenv("AIPROXY_TOKEN")

def extract_email(text):
    prompt = f"Extract the sender's email address from this email:\n{text}"
    response = openai.ChatCompletion.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
    return response["choices"][0]["message"]["content"].strip()

def extract_credit_card(image_path):
    prompt = f"Extract the credit card number from this image: {image_path}"
    response = openai.ChatCompletion.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
    return response["choices"][0]["message"]["content"].strip()
