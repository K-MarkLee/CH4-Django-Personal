from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("main/", views.main, name = "main"), # main 페이지로 이동
    path("index/", views.index, name = "index"), # index 페이지로 이동
]
 