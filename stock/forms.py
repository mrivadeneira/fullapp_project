from django.forms import ModelForm
from .models import Stock

class StockMovementForm(ModelForm):
    class Meta:
        model = Stock
        fields = ("sku", "category", "stock_type", "color", "size", "movement")

