import requests
import os
import openai


openai.organization = "org-7tpQe76EhDCvU1HZNvTWI3vv"
openai.api_key = "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"

""""
pic_result = openai.Image.create_edit(
  image=open("image_edit_mask.png", "rb"),
  prompt="kid with captain america closes driving a huge moto",
  n=2,
  size="1024x1024"
)
"""
pic_result = openai.Image.create(
  prompt="a chinese warrior panda doing some karate on the great western wall",
  n=2,
  size="1024x1024"
)

print(pic_result["data"][0]["url"])
print(pic_result["data"][1]["url"])

