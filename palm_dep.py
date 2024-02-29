import json
import requests

# Replace with your actual API key and headers
api_key = "AIzaSyBmjhopUEEOHLgBwvn0r36e3tsHUqOnEfA"
headers = {"myHeaders": "your_header_value"}

# Replace with the prompt you want to send

with open("buggy_code1.py", "r") as file:
    code_contents = file.read()

prompt = {
    "text": code_contents+'''eval(input()) Give a recommendation for making this code more secure:\n
             Give me the most important 3 points to secure this code.\n
             Answer in three sentences only, and be specific.'''
}

# Create JSON request body
raw = json.dumps({"prompt": prompt})

# Send POST request
url = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText"
params = {"key": "AIzaSyBmjhopUEEOHLgBwvn0r36e3tsHUqOnEfA"}
response = requests.post(url, params=params, data=raw)

# Check for successful response
if response.status_code == 200:
    # Process the response (e.g., extract the generated text)
    data = response.json()
    print(data['candidates'][0]['output'])
else:
    print(f"Error: {response.status_code}")
