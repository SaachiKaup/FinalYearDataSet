import requests
import os
import json

API_KEY = "AIzaSyBmjhopUEEOHLgBwvn0r36e3tsHUqOnEfA"
API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key=AIzaSyBmjhopUEEOHLgBwvn0r36e3tsHUqOnEfA"
headers = {"Authorization": f"Bearer {API_KEY}"}

file_path = "buggy_code1.py"  # Replace with the actual path to your file
with open(file_path, "r") as f:
    buggy_code = f.read()

prompt = {
    "prompt": "Give a recommendation for making this code more secure: Give me the most important 3 points to secure this code. Answer in three sentences only, and be specific.",
    #"code": buggy_code,
    #"language": "python",  # Specify the programming language
}

response = requests.post(API_ENDPOINT, data = json.dumps(prompt))

if response.status_code == 200:
    response_data = response.json()
    recommendations = response_data["recommendations"]  
    print(recommendations) 
else:
    print("Error:", response.text)
