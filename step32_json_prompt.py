import openai
import base64
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("receipt.png","rb") as f:
    image_data = f.read()

image_base64 = base64.b64encode(image_data).decode("utf-8")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_base64}"
                    }
                },
                {
                    "type": "text",
                    "text": "Read the receipt and return the result in JSON format only. Use this structure: {\"date\": \"YYYY-MM-DD\", \"store\": \"store name\", \"items\": [{\"name\": \"item name\", \"price\": 000}]}. Return JSON only, no explanation."
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)
