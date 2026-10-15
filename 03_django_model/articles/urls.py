from django.urls import path

from . import views

app_name = 'articles'# 이런식으로 불러와서 쓰면 "" 사이에 먼저예를 들어 "길동" 이라 되어있으면 앞에 홍이라는 것을 
    # 붙여 주기 위해서 이렇게 한거임
urlpatterns = [
    path('', views.index)
    path('/dinner', views.dinner) # 여기도 보면 /dinner앞에 articles를 붙이고 한다는 말임.
]
