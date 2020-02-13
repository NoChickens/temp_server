import os, sys, json
import urllib.request
from IPython import embed
from decouple import config


TEMPLATE = {
    "images": [
        {
            "format": "jpg",
            "name": "medium",
            "data": ""
        }
    ],
    "requestId": "string",
    "resultType": "string",
    "timestamp": "1",
    "version": "V1"
}

PATH = '2test' # PATH는 base64 이미지 파일

with open('{}.txt'.format(PATH), 'r', encoding='utf-8') as base64_of_image:
    TEMPLATE["images"][0]["data"] = base64_of_image.read()
    TEMPLATE_json = json.dumps(TEMPLATE)


client_secret = config('KEY')
url = "https://4ezihkm520.apigw.ntruss.com/custom/v1/883/728a92f505e638bb89981222993c97d90c01ae012875a8a78af253cf003a56e4/general"

request = urllib.request.Request(url)
request.add_header("X-OCR-SECRET", client_secret)
request.add_header("Content-Type", "application/json")
response = urllib.request.urlopen(request, data=TEMPLATE_json.encode("utf-8"))

if(response.getcode() == 200):
    response_body = json.loads(response.read().decode('utf-8'))
    # embed()
    images = response_body.get('images')[0].get('fields')
    result = []
    for word in images:
        result.append(word['inferText'])
    data = {
        'data': result
    }
    with open('{}.json'.format(PATH), 'w', encoding='utf-8') as file:
        file.write(json.dumps(data))
    print(data)
else:
    print("Error Code:" + rescode)

print(data)