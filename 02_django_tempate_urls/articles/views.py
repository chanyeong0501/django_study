from django.shortcuts import render
# Create your views here.

# 메인 페이지를 응답하는 함수

# view함수의 약속
    # 모든 view 함수는 반드시 첫번째 인자로 요청 객체(urls.py로 부터 받은)가 들어온다.
    # 매개변수 이름이 request일 필요는 없음. 하지만 다른 이름을 사용하지 않는다.
def index(request):
    # 메인 페이지 (템플릿)을 응답 데이터로 생성
    # 템플릿을 취합해서 최종적으로 만들어주는 함수
    #여기서도 딕셔너리의 이름이 반드시 컨택스트 일 필요는 없으나 근데 그냥 다른 사람과 같이 쓰니깐 이렇게 쓰자
    context = {
        "name" : "jane"

    }
    return render(request, 'articles/index.html', context)
import random

def dinner(request):
    foods = ["국밥", "국수", "카레", "탕수육", "빵",]
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')
# 클아이언트에 데이터를 입력할  form이 담긴 페이지를 응답하는 함수
def throw(request):
    return render(request, 'articles/throw.html')

# 사용자 입력 데이터를 바아서 그걸 추추러해서 어떤 데이터를 보냈는지 다시 알려주는 함수
def catch(request):
    # 사용자가 입력한 데이터를 찾아야 함
        # 그럼 사용자가 입력한 데이터는 어디에 있음?? -> request
        # 사실 클라이언트가 보낸 모든 정보는 첫번째 인자이누 request에 들어가 있음
    # 그리고 찾은 거를 변수에 담아서
    # 탬플릿과 함께 응답을 해야함
    data = request.GET.get('query')
    context = {
        'data' : data,
    }
    return render(request, 'articles/catch.html', context)
# 여기서 varible라우팅에 서 선언했던 변수명과 같은 이름으로 매개변수를 써야 함
def detail(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)
