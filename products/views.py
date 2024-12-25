from django.shortcuts import render

# Create your views here.

# index 페이지의 view 함수
def index(request):
    return render(request, 'products/index.html')