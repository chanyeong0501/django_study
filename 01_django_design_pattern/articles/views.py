from django.shortcuts import render # 여기 import render 가 탬플릿을 가져오는게 됨

# Create your views here.
# 여기서 메인페이지를 응답하는 함수를 만들 꺼임
# view의 약속이 있는데 그건 반드시 첫번째 인자로 요청 객체가 들어온다는 것임
# 이때 매개변수 이름이 굳이 request안써도 되는데 공통으로 쓰니깐 그냥 쓰자 
# 일단 request가 뭐가 들어오는지 모르지만 (지금은) 써야함
def index(request):
    # 메인 페이지 (탬플릿)을 응답데이터로 생성
    # 탬플릿을 취합해서 최종적으로 만들어 주는 함수가 필요함

    return render(request, 'articles/index.html') # 랜더 함수는 탬플릿을 만들어 주는 함수이고 여기서 request가 먼저 있어야 함