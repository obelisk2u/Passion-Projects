from openai import OpenAI
client = OpenAI()

image_path = "./docs/algebra.jpg"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": r"Give me the answers to each one of these problems"},
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

print(response.choices[0].message.content)