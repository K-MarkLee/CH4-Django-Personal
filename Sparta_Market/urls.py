"""
URL configuration for Sparta_Market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls), # 개발자 페이지로 이동
    path('', lambda request: redirect('products:index'), name='index'),  # 기본 경로를 products:index로 리다이렉트


    path("users/", include("users.urls")), # users app의 urls.py로 이동
    path("products/", include("products.urls")), # products app의 urls.py로 이동
    path("accounts/", include("accounts.urls")), # accounts app의 urls.py로 이동
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)