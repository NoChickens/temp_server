from django.conf.urls import url, include 
from django.urls import path


# 이 앱은 회원 정보를 관리한다.
# 회원은 자신의 폴더를 관리할 수 있다. 
# 사전에 작성한 모델들을 이 앱에 작성한다.

app_name = 'accounts'

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
