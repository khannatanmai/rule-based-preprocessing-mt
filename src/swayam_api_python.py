import requests
import json

headers = {
    'accept': '*/*',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_access_token_here',
}

data = '{"text":"This is example text","source_language":"eng","target_language":"hin"}'

response = requests.post('https://apicallhttps.iiithcanvas.com/apiMt/v.1.0.0/mt_linker', headers=headers, data=data)

response_text = json.loads(response.text)

print(response_text["data"])

