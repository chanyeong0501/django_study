"""
URL configuration for firstpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views # 모듈이기 때문에 우리가 이렇게 받아와야 함

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index), # articles로 요청이 들오왔을 때 일할 view함수를 작성함
] # 결국 아티클스라는 주소로 요정이 오면 index 뷰 함수를 호출 하겠다는 의미
# 근데 여기서 index()이렇게 괄호로 안 쓴 이유는 view함수에 호출은 왼쪽 인자 주소로 요정이 왔을때만 호출이 
# 되어야 해서 함수 주소만 기록해둔 것 이기 때문이다.
