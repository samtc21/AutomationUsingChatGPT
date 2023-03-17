import requests
import os
import openai


openai.organization = "org-7tpQe76EhDCvU1HZNvTWI3vv"
openai.api_key = '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'

pic_result = openai.Image.create_edit(
  image=open("image_edit_mask.png", "rb"),
  prompt="kid with captain america closes driving a huge moto",
  n=2,
  size="1024x1024"
)

print(pic_result["data"][0]["url"])
print(pic_result["data"][1]["url"])
"""""
api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"
# api_key = os.getenv("OPENAI_API_KEY")
"""
""""
openai.Image.create_edit(
    image=open("shiloh_original.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A cute baby sea otter wearing a beret",
    n=2,
    size="1024x1024"
)
"""
