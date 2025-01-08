from openai import OpenAI
import re

client = OpenAI()

image_path = "./docs/algebra.jpg"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": r"Give me the answers to each one of these problems. Prioritize correctness."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://i.imgur.com/rVnkqtD.jpeg",
                    },
                },
            ],
        }
    ],
    
)

response=(response.choices[0].message.content)
file_path = 'out.md'

with open(file_path, 'w') as file:
    file.write(response)