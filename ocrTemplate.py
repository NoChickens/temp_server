import os, sys, json
import urllib.request
from IPython import embed


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

PATH = 'OCR/2test' # PATH는 base64 이미지 파일

with open('{}.txt'.format(PATH), 'r', encoding='utf-8') as base64_of_image:
    TEMPLATE["images"][0]["data"] = base64_of_image.read()
    TEMPLATE_json = json.dumps(TEMPLATE)


client_secret = 'Tmh3QUNPS3l5dlpza2hhWUxtU3pUVkJMdE1TWG9kelA='
url = "https://4ezihkm520.apigw.ntruss.com/custom/v1/862/7db01c9f008b09a1db8fc55fee81945d8cfa5454b13df99c36ff8ee555d5c926/infer"

request = urllib.request.Request(url)
request.add_header("X-OCR-SECRET",client_secret)
request.add_header("Content-Type", "application/json")
response = urllib.request.urlopen(request, data=TEMPLATE_json.encode("utf-8"))

if(response.getcode() == 200):
    response_body = json.loads(response.read().decode('utf-8'))
    embed()
    images = response_body.get('images')[0]
    matchedTemplate = images.get('matchedTemplate')
    title = images.get('title')
    fields = images.get('fields')
    result = {
        'matchedTemplate' : matchedTemplate,
        'title' : title.get('inferText'),
        'fields' : fields
    }
    # embed()
#     images = response_body.get('images')[0].get('fields')
#     result = []
#     for word in images:
#         result.append(word['inferText'])
#     data = {
#         'data': result
#     }
    with open('{}_2.json'.format(PATH), 'w', encoding='utf-8') as file:
        file.write(json.dumps(result))
#     print(data)
# else:
#     print("Error Code:" + rescode)