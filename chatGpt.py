import requests
import os

def classify(question, categories):
    if type(question) != str:
        return print("the question need to be a string only")

    for element in categories:
        if type(element) != str:
            return print("categories need to be a list of strings only")

def pic_modifier( image, instructions):
    api_endpoint = "https://api.openai.com/v1/completions"
    api_key = "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"
    # api_key = os.getenv("OPENAI_API_KEY")


    openai.Image.create_edit(
        image=open("otter.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A cute baby sea otter wearing a beret",
        n=2,
        size="1024x1024"
    )

def generate_pythonCode(question):
    api_endpoint = "https://api.openai.com/v1/completions"
    api_key = "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"
    # api_key = os.getenv("OPENAI_API_KEY")
    request_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }
    request_data = {
        "model": "text-davinci-003",
        "prompt": f" {question}",
        "max_tokens": 500,
        "temperature": 0.5
    }

    response = requests.post(api_endpoint, headers=request_headers, json=request_data)
    if response.status_code == 200:
        response_text = response.json()["choices"][0]["text"]
        with open(args, "w") as file:
            file.write(response_text)
        print(response.json()["choices"][0]["text"])
    else:
        print(f"Request failed with status code: {str(response.status_code)}\n")
