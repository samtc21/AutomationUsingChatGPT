import requests
import os
import openai
import argparse

"""
parser = argparse.ArgumentParser()
parser.add_argument('prompt', help="the prompt to send to the OpenAI API")
parser.add_argument('file_name', help="the prompt to send to the OpenAI API")
args = parser.parse_args()
print(args.prompt)
print(args.file_name)
"""
print(os.getenv("OPENAI_API_KEY"))
args = input("Enter question to ChatGPT")

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"
#api_key = os.getenv("OPENAI_API_KEY")
request_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}
request_data = {
    "model": "text-davinci-003",
    "prompt": f" {args}",
    "max_tokens": 500,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)
if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(args,"w") as file:
        file.write(response_text)
    print(response.json()["choices"][0]["text"])
else:
    print(f"Request failed with status code: {str(response.status_code)}\n")
