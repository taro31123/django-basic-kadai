from django.db import models
from django.urls import reverse

# 課題012用モデルの追加 
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


# 課題010用モデルの追加
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    # 012で追加
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, default='noImage.png')
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name