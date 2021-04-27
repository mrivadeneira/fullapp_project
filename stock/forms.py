from django.forms import ModelForm
from django import forms
from .models import Stock

class StockMovementForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ("sku", "category", "stock_type", "color", "size", "movement", "movement_date")
        widgets = {
            "movement_date": forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }
