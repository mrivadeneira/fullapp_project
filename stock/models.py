from django.db import models

class Stock(models.Model):
    sku = models.CharField(max_length=16)
    category = models.IntegerField()
    stock_type = models.IntegerField()
    color = models.IntegerField()
    size = models.IntegerField()
    movement = models.IntegerField()
