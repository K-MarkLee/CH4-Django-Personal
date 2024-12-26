from django.db import models
from django.conf import settings

# Create your models here.

# 상품 모델 정의
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()  # 정수로 가격 저장
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # 이미지 업로드
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_products', blank=True)

    def __str__(self):
        return self.title
    


    def price_format(self):
        return f'{self.price:,}'