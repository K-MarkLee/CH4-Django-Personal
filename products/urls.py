from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("main/", views.main, name = "main"), # main 페이지로 이동
    path("", views.index, name = "index"), # index 페이지로 이동
    path("create/", views.create, name = "create"), # create 페이지로 이동
    path("<int:pk>/", views.detail, name = "detail"), # detail 페이지로 이동
    path("<int:pk>/delete/", views.delete, name = "delete"), # delete 페이지로 이동
    path("<int:pk>/update/", views.update, name = "update"), # update 페이지로 이동
    path("<int:pk>/like/", views.like, name = "like"), # like 페이지로 이동
    path("liked_products/", views.liked_products, name = "liked_products"), # like_products 페이지로 이동
]
 