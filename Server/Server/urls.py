from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url,include 
from django.contrib import admin 
from rest_framework import routers 
from naver.views import TranslateViewSet
from rest_framework import routers
from naver import views

router = routers.DefaultRouter()
# router.register(r'translate', views.TranslateViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    # path('naver/', include('naver.urls')),

    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/naver/', include('naver.urls')),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



