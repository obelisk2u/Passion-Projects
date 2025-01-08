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
                {"type": "text", "text": r"Give me the answers to the first 4 of these problems. Prioritize correctness."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://preview.redd.it/history-paper-2-practice-questions-v0-l2r8kx1d7qw81.jpg?width=1080&crop=smart&auto=webp&s=3afd8de9112825d4aea95b9ef3da9d19bdcbb143",
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