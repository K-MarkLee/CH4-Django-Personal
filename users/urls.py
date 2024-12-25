from django.urls import path
from . import views

app_name = "users"

urlpatterns = [ 
    path("<int:pk>/", views.user, name= "user"), # /user 링크로 들어오면 view.user 함수로 이동
    path("<int:pk>/detail/", views.detail, name= "detail"), # /user/detail 링크로 들어오면 view.user_detail 함수로 이동
    path("<int:pk>/follow/", views.follow, name= "follow"), # /user/follow 링크로 들어오면 view.follow 함수로 이동 팔로우/언팔로우 기능
]
