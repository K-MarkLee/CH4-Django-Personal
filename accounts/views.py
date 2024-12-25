from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import CustomUserUpdateForm, CustomUserCreateForm
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.shortcuts import get_object_or_404
from .forms import DeleteAccountForm


# Create your views here.

# 로그인
@require_http_methods(["GET", "POST"])
def login(request):

    # 이미 로그인한 유저는 main 페이지로 이동
    if request.user.is_authenticated:
        return redirect('products:main')

    if request.method == 'POST':
        # AuthenticationForm을 사용하여 폼 데이터를 받아옴
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user()) # 사용자 로그인
            return redirect('products:main')  # 로그인 성공 후 products:main으로 이동
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/account_login.html', context)


# 로그아웃
@login_required
@require_POST
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('products:index')
    

# 회원가입
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())  # 회원가입 성공 후 자동 로그인)
            return redirect('products:main')
    else:
        form = CustomUserCreateForm()
    context = {'form': form}
    return render(request, 'accounts/account_create.html', context)


# 회원탈퇴
@login_required
@require_http_methods(["GET", "POST"])
def delete(request, pk):

    # 본인만 삭제 가능
    if request.user.pk != pk:
        return redirect('users:user_detail', pk=request.user.pk)

    user = get_object_or_404(get_user_model(), pk=pk)
    form = DeleteAccountForm(user=user)

    if request.method == 'POST':
        form = DeleteAccountForm(request.POST, user=user)
        if form.is_valid():
            user.delete()  # 계정 삭제
            return redirect('products:index')  # 삭제 후 홈페이지로 리다이렉트
    context = {'user': user , 'form': form}
    return render(request, 'accounts/account_delete.html', context)


# 정보 업데이트
@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    # 본인만 수정 가능
    if request.user.pk != pk:
        return redirect('users:user', pk=pk)

    user = get_object_or_404(get_user_model() ,pk=pk)
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:user_detail', pk=user.pk)  # 수정 완료 후 상세 페이지로 이동
    else:
        form = CustomUserUpdateForm(instance=user)
    context = {'form': form}
    return render(request, 'accounts/account_update.html', context)



# 비밀번호 변경
@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()  # 비밀번호 변경
            update_session_auth_hash(request, user)  # 세션 유지
            return redirect("users:user_detail")  # 변경 후 리다이렉트
    else:
        form = PasswordChangeForm(request.user)  # 비밀번호 변경 폼 생성
    context = {"form": form}
    return render(request, "accounts/account_change_password.html", context)
