# CH4-Django-Personal

# Django Sparta - Market 

## 프로젝트 개요

이 프로젝트는 Django를 기반으로 사용자의 계정 관리와 제품 관리 기능을 제공하는 웹 애플리케이션입니다. 사용자 간의 팔로우 기능, 좋아요한 제품 관리, 제품 등록, 수정, 삭제 등의 다양한 기능을 포함하고 있습니다.
  
   
&nbsp;&nbsp;
## 주요 기능
### 1. 사용자 관리 (Accounts)
- 회원가입 및 로그인
    - 이메일을 아이디로 사용하게함.
    - 비밀번호 변경 및 계정의 삭제 기능을 제공.

  
&nbsp;  
- 프로필(정보페이지)
    - 프로필 페이지를 다른 사람이 보는 user와 내 중요 정보를 둔 user_detail로 분리.
    - 프로필에서는 기본적인 정보를 제공.
    - 팔로우/ 언팔로우 기능 지원.

&nbsp;  
- 계정 생성일 표시
    - 사용자의 계정 생성 날짜를 user_detail에서 확인 가능.

&nbsp;
### 2. 물품 관리 (Products)
- 물품의 CRUD
    - 물품 등록, 수정 , 삭제 기능 제공.
    - 물품 목록은 최신순으로 정렬.

&nbsp;
- 물품의 상세 페이지
     - 물품의 제목, 가격, 설명, 이미지 등을 표시함
     - action을 경로에 따라 다르게 제공

&nbsp;
- 좋아요 기능 제공
    - 사용자는 물품에 좋아요를 하거나 취소할 수 있음.
    - 좋아요한 제품만을 골라서 확인 가능 (user_detail)

&nbsp;
### 3. 기타 기능
- 접근의 제한
    - 기본적으로 로그인 하지 않은 유저 기능제한
    - user_detail 은 해당 유저만, post를 이용해서 해당 유저만 갈수 있도록 함.

&nbsp;
- 동적 링크
    - 사용자가 특정 페이지에서 물품 상세 페이지로 이동했을 시, 원래 즉 이전의 페이지로의 동적 링크를 제공. 이는 타고온 링크의 영향을 받음.

&nbsp;
---
## 사용된 기술의 스택
- 프레임워크 : Django
- 프론트 엔드 : HTML, CSS(Django Template)
- 데이터베이스 : SQLite (Base Django Database)
- etc
    - Django's `AUTH_USER_MODEL` 사용자 모델 확장
    - 커스텀 모델 및 폼 생성

&nbsp;
---
## 프로젝트의 구조
```
project/
├── accounts/
│   ├── forms.py           # 계정 관리 커스텀 폼
│   ├── models.py          # 계정 관리 커스텀 모델
│   ├── urls.py            # 계정 관리 URL 매핑
│   ├── views.py           # 계정 관리 뷰
│   ├── templates/accounts/ # 계정 관리 html 목록 
|
├── products/
│   ├── forms.py           # 물품 커스텀 폼
│   ├── models.py          # 물품 커스텀 모델
│   ├── urls.py            # 물품 관련 URL 매핑
│   ├── views.py           # 물품 관련 뷰
│   ├── templates/products/ # 물품 관련 html 목록
|
├── users/
│   ├── urls.py            # 유저 관련 URL 매핑
|   ├── views.py           # 유저 관련 뷰
|   ├── templates/users/   # 유저 관련 html 목록 
|
├── project/
│   ├── settings.py        # Django 설정
│   ├── urls.py            # 전체 URL 매핑
|
├── static/
│   ├── css/
│       ├── styles.css     # 전역 CSS
|
├── templates/
│   ├── base.html          # 공통 레이아웃
|
```
&nbsp;


---
&nbsp;
## 설치 및 실행
### 1. 클론 및 환경의 설정
```git clone <repository-url>
cd project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

&nbsp;
### 2. 데이터베이스의 마이그레이션
```
python manage.py makemigrations
python manage.py migrate
```
&nbsp;
### 3. 개발 서버 실행
```
python manage.py runserver
```
&nbsp;
### 4. 관리자 계성 생성 (선택)
```
python manage.py createsuperuser
```
&nbsp;

---
&nbsp;
## 사용 방법
1. 첫 화면에서 로그인 및 회원등록을 실시한다.

2. 로그인 후 자동으로 메인 페이지에 접속이 가능하다.

    1. 메인 페이지 에서는 등록된 물품의 목록을 확인하거나 등록 가능하다.

3. 물품을 클릭해서 상세정보로 들어 갈 수 있다.
    1. 물품글의 수정과 삭제가 가능하다.
    2. 물품글에 좋아요가 가능하다.

4. 작성자의 이름을 클릭해서 정보로 들어갈 수 있다.

    1. 작성자를 팔로우 하거나 언팔로우 할 수 있다.

5. 나의 정보는 좌측 상단의 링크를 클릭하면 된다.
    1. 기본적인 정보를 알 수 있는 user 페이지로 들어가게된다.
    2. action 에서 user_detail로 갈 수 있다.

6. user_detail 에서 디테일한 정보의 확인이 가능하다.
    1. 좋아요한 글을 누르면 리스트를 볼 수 있게 했다.
        1. 리스트를 클릭하면 상세가 나오는데 이떄 action에 넘어온 경로에 따라 차이점을 줬다. (바로 좋아요한 글 리스트로 이동)
    2. 유저의 정보 수정과 삭제가 가능하다.
        1. 삭제의 경우에는 비밀번호를 다시 입력해야 삭제가 된다.

&nbsp;
---
## 추가 구현 계획
- 댓글 기능
- 검색 기능
---

&nbsp;
## Trouble Shooting
1. `SystemCheckError` : Reverse accessor clashes
- 문제 : 
    - Django 에서 `CustomUser`모델이 2개 정의되서 충돌이 발생
- 해결방법:
    - `accounts.CustomUser` 만 유지라고 이외의 CustomUser 삭제
    - `setting.py`에서 `AUTH_USER_MODEL` 을 `accounts.CustomUser`로 등록
    - 데이터베이스 마이그레이션

&nbsp;
2. 좋아요 상태를 템플릿에서 처리 할때 `TemplateSyntaxError`
- 문제 :
    - `request.user.following.fillter(pk = user.pk).exists()`와 같은 메서드 호출이 템플릿에서 작동하지 않음
- 해결방법 : 
    - 뷰에서 좋아요 상태를 처리하게하는 컨텍스트 추가.
    ```is_following = request.user.followings.filter(pk=user.pk).exists()```
    - 템플릿에서는 이를 가져와 `is_following`을 사용하여서 조건으로 처리

&nbsp;
3. 물품 리스트가 비어 있을 때 에러 발생
- 문제 : 
    - 물품이 없을 떄 빈페이지로 표시되거나 에러가 발생
- 해결방법 :
    - 템플릿에서 `{% if products%}` 조건을 for 조건문 밖에 추가
