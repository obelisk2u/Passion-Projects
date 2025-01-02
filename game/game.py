import requests

API_KEY = ""

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Hello, OpenAI!"}
    ],
    "max_tokens": 10
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    answer = response.json()["choices"][0]["message"]["content"]
    print(answer)
else:
    print("Error:", response.status_code, response.text)
