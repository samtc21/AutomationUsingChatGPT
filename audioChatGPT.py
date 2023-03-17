import os
import openai
from uncod_to_ascii_converter import *


openai.organization = "org-7tpQe76EhDCvU1HZNvTWI3vv"
openai.api_key = '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'


audio_file = open("testaudio2.m4a", "rb")

transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(unicode_to_ascii(transcript["text"]))
