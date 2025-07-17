from openai import OpenAI
from pprint import pprint
import os

# 깃허브 업로드 시 가려야 함
api_key = ""
# api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

model = "gpt-4o-mini"

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What are the youth support projects in Busan?"},
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
).model_dump()
pprint(response)