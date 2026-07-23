import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen3:4b",
    "prompt": "Say hello in one sentence.",
    "stream": False
}

print("Sending request...")

response = requests.post(url, json=payload, timeout=120)

print("Status:", response.status_code)
print(response.json())