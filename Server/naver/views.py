from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import urllib.request


# 1. 이미지 업로드 순간(나라 코드까지) - OCR로 보내주는 함수

def sending(request):
    # base64_result = request.data    지수형이 보내 줄 거 
    with open('./OCR.json', 'r', encoding='utf-8') as f:
        temps = json.load(f)
        # temps["images"][0]["data"] = base64_result
        transmit = json.dumps(temps)
    data = transmit
    # url = ""
    request = urllib.request.Request(url)
    request.add_header("X-OCR-SECRET","secret_key")
    request.add_header("Content-Type", "application/json")
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

        # return Response(temp)    결과 값 inferText 파파고로 보내보셈 알아서 


# 2. OCR 결과값을 파파고 NMT로 옮겨주는 함수
def transferring(request):
    return

# 3. 번역 결과 값 띄어주는 함수
def checking(request):
    return

# 4. 결과 값 데이터 베이스에 저장함수
def receipt_result(request):
    return