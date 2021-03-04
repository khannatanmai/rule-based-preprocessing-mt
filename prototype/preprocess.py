import googletrans
import sys
import time
import requests
import json
from googletrans import Translator

if(len(sys.argv) < 4):
	print("Not enough arguments.")
	sys.exit()

source_input = sys.argv[1]
replace_source = sys.argv[2]
replace_target = sys.argv[3]

print("*** Pre-processing: " + replace_source + " -> " + replace_target + " ***\n")

# GOOGLE TRANSLATE API

translator = Translator()
source_language = 'en'
destination_language = 'hi'

print("Google Translate\n")

print("Original Input: " + source_input)
result_original = translator.translate(source_input, src=source_language, dest=destination_language)
print("Original Translation: " + result_original.text)

time.sleep(2.5)
preprocessed_input = source_input.replace(replace_source, replace_target)
print("\nPre-processed input: " + preprocessed_input)

time.sleep(2.5)

result_final = translator.translate(preprocessed_input, src=source_language, dest=destination_language)
print("Final Translation: " + result_final.text)

# SWAYAM API
print("\n*****\n\nSwayam Translate\n")

print("Original Input: " + source_input)

headers_token = {
    'Authorization': 'Basic Rkhxazg5MG9Edko2dFFXYWIzbldFOVhwNEE0YTpXSjVmTVloV2JUWjF1RzloVzRrYnA1OEptZllh',
}

data_token = {
  'grant_type': 'client_credentials'
}

response = requests.post('https://apicallhttps.iiithcanvas.com/token', headers=headers_token, data=data_token)

current_token = json.loads(response.text)["access_token"]

headers = {
    'accept': '*/*',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + current_token,
}

data = '{"text":"' + source_input + '","source_language":"eng","target_language":"hin"}'

response = requests.post('https://apicallhttps.iiithcanvas.com/apiMt/v.1.0.0/mt_linker', headers=headers, data=data)
response_text_original = json.loads(response.text)

print("Original Translation: " + response_text_original["data"])

print("\nPre-processed input: " + preprocessed_input)

data = '{"text":"' + preprocessed_input + '","source_language":"eng","target_language":"hin"}'

response = requests.post('https://apicallhttps.iiithcanvas.com/apiMt/v.1.0.0/mt_linker', headers=headers, data=data)
response_text_final = json.loads(response.text)

print("Final Translation: " + response_text_final["data"])
