from django.db import models
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length=128)

class StockType(models.Model):
    stock_type_name = models.CharField(max_length=128)

class Color(models.Model):
    color_name = models.CharField(max_length=128)

class Size(models.Model):
    size_name = models.CharField(max_length=128)

class Movement(models.Model):
    movement_name = models.CharField(max_length=128)

class Stock(models.Model):
    sku = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    stock_type = models.ForeignKey(StockType, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    movement = models.ForeignKey(Movement, on_delete=models.SET_NULL, null=True)
    movement_date = models.DateTimeField(default=timezone.now())
    movement_registration = models.DateTimeField(auto_now_add=True)