from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.


# 일반 유저 정보 페이지 (다른 로그인 한 유저가 접근 가능)
@login_required
def user(request, pk):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=pk)  # 특정 유저 가져오기
        is_following = user.followers.filter(pk=request.user.pk).exists()  # 팔로우 여부 확인
        context = {
            'user': user,
            'is_following': is_following,
            'followers_count': user.followers.count(),
            'followings_count': user.followings.count(),
            }
        return render(request, 'users/user.html', context)
    else:
        return redirect('products:index')
    



@login_required
def detail(request, pk):

    if request.user.is_staff or request.user.is_superuser or request.user.pk == pk:
        user = get_object_or_404(User, pk=pk)
        context = {'user': user}
        return render(request, 'users/user_detail.html', context)
    

   
@login_required
def follow(request, pk):
    target_user = get_object_or_404(User, pk=pk)
    if request.user != target_user:  # 자신을 팔로우할 수 없음
        if request.user.followings.filter(pk=target_user.pk).exists():
            request.user.followings.remove(target_user)  # 언팔로우
        else:
            request.user.followings.add(target_user)  # 팔로우
    return redirect('users:user', pk=pk)


