from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms


class CustomUserCreateForm(UserCreationForm):
    # 추가 필드 정의
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = get_user_model()  # 커스텀 유저 모델 사용
        fields = UserCreationForm.Meta.fields + ('email',)  # 필드 추가




class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name')  # 이메일 제외


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 비밀번호 변경 링크 추가
        if self.fields.get("password"):
            password_help_text =(
                "You can change the password"
                ' <a href="{}">here</a>'
            ).format(f"{reverse('accounts:change_password')}") # 변경 링크 
            self.fields["password"].help_text = password_help_text


class DeleteAccountForm(forms.Form):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"}),
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # 사용자 객체 받기
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not self.user or not self.user.check_password(password):
            raise forms.ValidationError("The password you entered is incorrect.")
        return password