from django.urls import path
from . import views

app_name = "users"

urlpatterns = [ 
    path("", views.users, name= "users"), # users 페이지로 이동
]
