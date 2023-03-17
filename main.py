import os
import openai

#THIS CODE USING OPENAI MODULE INSTEAD OF REQUESTS ( NOT WORKING - ERROR WITH API KEY )
openai.api_key = os.getenv("OPENAI_API_KEY")
print(os.getenv("OPENAI_API_KEY"))

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)

print(response.json())
