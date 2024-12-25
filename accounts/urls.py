from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("login/", views.login, name = "login"), # login 페이지로 이동
    path("logout/", views.logout, name = "logout"), # logout 페이지로 이동
    path("create/", views.create, name = "create"), # signup 페이지로 이동
    path("delete/<int:pk>", views.delete, name = "delete"), # delete 페이지로 이동    
    path("update/<int:pk>", views.update, name = "update"), # update 페이지로 이동
    path("password/", views.change_password, name = "change_password"), # change_password 페이지로 이동
]
 