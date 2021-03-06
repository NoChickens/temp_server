# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# import json
# import urllib.request
# from .models import Temp
# from .serializers import TempSerializer
# # from decouple import config


# # 1. 이미지 업로드 순간(나라 코드까지) - OCR로 보내주는 함수
# def sending(request):

#     # OCR로 요청 보낼 건데, Json 형식으로 보내야 됨 (Body 내용 미리 작성해놓음)

#     # base64_result = request.data    지수형이 보내 줄 거 
#     with open('./OCR.json', 'r', encoding='utf-8') as f:
#         temps = json.load(f)
#         # temps["images"][0]["data"] = base64_result    - OCR.json에 data(key) 에 value 값 저장
#         transmit = json.dumps(temps)
#     data = transmit
#     # url = "Invoke OCR URL"
#     request = urllib.request.Request(url)
#     request.add_header("X-OCR-SECRET","secret_key")
#     request.add_header("Content-Type", "application/json")
#     response = urllib.request.urlopen(request, data=data.encode("utf-8"))
#     rescode = response.getcode()
#     if(rescode==200):
#         response_body = response.read()
#         fix = response_body.decode('utf-8')
#         fix = json.loads(fix)
#         empty = ''
#         for key, val in fix.items():
#             if key == "images":
#                 for k in val[0]["fields"]:
#                     empty+=k['inferText']+' '

#         print(empty)  # 여기에 inferText에 모든 것이 나옴.
        
#     else:
#         print("Error Code:" + rescode)

#     return empty

# # 2. OCR 결과값을 파파고 NMT로 옮겨주는 // 번역 결과 값을 쏴주는 함수
# def transferring(request, empty):

#     # 파파고 요청 코드

#     client_id = "" # 개발자센터에서 발급받은 Client ID 값
#     client_secret = "" # 개발자센터에서 발급받은 Client Secret 값
#     encText = urllib.parse.quote(empty)
#     data = "source={원래언어}&target=ko&text=" + encText  
#     url = "https://openapi.naver.com/v1/papago/n2mt"
#     request = urllib.request.Request(url)
#     request.add_header("X-Naver-Client-Id",client_id)
#     request.add_header("X-Naver-Client-Secret",client_secret)
#     response = urllib.request.urlopen(request, data=data.encode("utf-8"))
#     rescode = response.getcode()
#     if(rescode==200):
#         response_body = response.read()
#         fix2 = response_body.decode('utf-8')
#         fix2 = json.loads(fix2)
#         translated = fix2["message"]["result"]["translatedText"]
#     else:
#         print("Error Code:" + rescode)

#     # TempSerializer 코드

#     serializer = TempSerializer(data=translated) # 번역 결과 값을 보여주기 위한 serializer
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)

#     return Response(status=400, data=serializer.errors)

# # 3. 번역 결과 값 선택 시 DB에 저장 / 선택 안 할 시 재촬영 함수
# def checking(request):
#     return