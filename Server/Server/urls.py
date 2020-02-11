from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib import admin
from naver import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('naver/', include('naver.urls')),

]



