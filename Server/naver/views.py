from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Translate
from .serializers import TranslateSerializer
from rest_framework import viewsets 

class TranslateViewSet(viewsets.ModelViewSet):
    queryset = Translate.objects.all()
    serializer_class = TranslateSerializer

# 1. 이미지 업로드 순간(나라 코드까지) - OCR로 보내주는 함수
def sending(request):
    return 

# 2. OCR 결과값을 파파고 NMT로 옮겨주는 함수
def transferring(request):
    return

# 3. 번역 결과 값 띄어주는 함수
def checking(request):
    return

# 4. 결과 값 데이터 베이스에 저장함수
def receipt_result(request):
    return