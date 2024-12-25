from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.


# 일반 유저 정보 페이지 (다른 로그인 한 유저가 접근 가능)
@login_required
def user(request, pk):
    if request.user.is_authenticated:
        if request.user.pk == pk:
            return redirect('users:user_detail', pk=pk)
        user = get_object_or_404(User, pk=pk)  # 특정 유저 가져오기
        context = {'user': user}
        return render(request, 'users/user.html', context)
    else:
        return redirect('products:index')
    



@login_required
def user_detail(request, pk):
    
    if request.user.pk != pk:
        return redirect('users:user', pk=pk)  # 본인이 아니면 일반 정보 페이지로 리다이렉트
    

    if request.user.is_staff or request.user.is_superuser or request.user.pk == pk:
        user = get_object_or_404(User, pk=pk)
        context = {'user': user}
        return render(request, 'users/user_detail.html', context)