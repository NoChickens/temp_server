from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Schedule, Expenditure, ExchangeRates, Receipt
from .serializers import UserSerializer, ScheduleSerializer, ExchangeRatesSerializer, ExpenditureSerializer, ReceiptSerializer


# 1. 회원가입 - 회원가입 함수
def signup(request):
    return 

# 2. 로그인 - 로그인 함수
def login(request):
    return 

# 3. 유저 디테일 - 회원의 지출 기록 페이지로 연결해주는  함수
@api_view(['GET'])
def user_detail(request):
    # user = get_object_or_404(User, id=user_id)
    # serializer = ScheduleSerializer(user)
    # return Response(serializer.data)
    return

# 4. 로그아웃 - 로그아웃 함수
def logout(request):
    return 


# 5. 스케줄 명을 설정해야 DB를 가계부 차트에 보여준다!
def set_folder(request):
    return