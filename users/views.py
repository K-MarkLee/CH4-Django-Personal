from django.shortcuts import render

# Create your views here.

# users 페이지의 view 함수
def users(request):
    return render(request, 'users/users.html')