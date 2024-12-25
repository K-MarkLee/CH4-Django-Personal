from django.shortcuts import render
from accounts.forms import CustomUserCreateForm  # sign up 폼 가져오기
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

# index 페이지의 view 함수
def index(request):
    
    # 로그인한 유저는 main 페이지로 이동
    if request.user.is_authenticated:
        return render(request, 'products/main.html')

    # sign up 폼을 form 변수에 저장
    form = AuthenticationForm()
    context = {"form" : form}
    return render(request, 'products/index.html', context)


def main(request):
    return render(request, 'products/main.html')