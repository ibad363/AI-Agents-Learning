import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()
openrouter_api_key = os.getenv("OPEN_ROUTER_API_KEY")

BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "qwen/qwen3-30b-a3b:free"

response = requests.post(
    url=f"{BASE_URL}/chat/completions",
    headers={
        "Authorization": f"Bearer {openrouter_api_key}"
    },
    data=json.dumps({
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": "What is the meaning of life in context of Islamic teaching?"
            }
        ]
    })
)
data = response.json()
print(data["choices"][0]["message"]["content"])