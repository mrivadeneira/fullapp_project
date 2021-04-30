from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock 
        fields = ('pk', 'sku', 'category', 'stock_type', 'color', 'size', 'movement', 'movement_date', 'movement_registration')


