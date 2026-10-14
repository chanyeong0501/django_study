from django.db import models # 모델도 view에서 render처럼 이걸 써야 된다고 느낌이 들거임!


# Create your models here.

# 계시글을 저장을 위한 테이블을 설계를 해볼꺼임 그래서 그거위한 클래스를 만들꺼임
# 우리가 데이터 베이스와 상호작용하는 것을 개발하려면 많은 것을 고려해야함
# 예를 들어 보안이라던지 어떻게 소통을 할 껀지, 아니면 여러 기능들(뭐 수정, 삭제 등등..)
# 근데 장고라는 프레임워크를 쓰는 경우 장고가 이런 것들을 구현 해놨음 -> from django.db import models에
# 그래서 우리가 해야 하는 것을 저기에 있는 것들 중에서 장 가져다가 쓰면 된다
# 기본적인 model class에 대한 구현이 완료된 model클래스를 상속 받으면서 시작할꺼임!
# 그래서 기본적인 모델 클레스에 대한 구현이 완료된 Model 클래스를 상속 받으면서 시작할꺼답!
class Article(models.Model):
    #우리는 Model클래스를 상속 받으면서 다른 것을 고민 할 필요 없이 지금 해야 할 것에 대해서만 신경쓰면됨
    # 여기서 우리가 해야하는 것은 테이블의 칼럼을 정의 하고 어려 제약 조건들을 정의 하는 일이다 
    # 아래 세가지를 정의 해봐야 할거같은데 id의 경우는 생략이 가능하다. 
    # id 의 경우는 기본적으로  titile같은 것들에 대해서 위치를 잡아줘야 하는데(어디에 있는지 알기 위해서)그래서 id 컬럼은 알아서 만들어 줌.
    # 그래서 컬럼은 클래스 변수로 정의한다
    # 그리고 타이틀 같은 거는 문자열일 텐데 이런 기본적인 틀 자체도 기본적으로 내장되어 있다  
    title = models.CharField(max_length=10) # max_length= 를 통해서 제약 조건을 만들어줌
    content = models.TextField() # 이렇게 두줄 밖에 쓰지 않았지만 우리는 기능을 다 쓰고 있는 것임
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)