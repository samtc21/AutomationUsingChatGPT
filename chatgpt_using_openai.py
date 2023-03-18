import openai

# THIS CODE USING OPENAI MODULE INSTEAD OF REQUESTS

openai.organization = "org-7tpQe76EhDCvU1HZNvTWI3vv"
openai.api_key = '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'

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)

print(response["choices"][0]["text"])
