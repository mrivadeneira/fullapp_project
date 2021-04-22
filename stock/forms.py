from django import forms

class StockMovementForm(forms.Form):
    sku = forms.CharField(label="Sku", max_length=128)
    categories = (
        (1, "Category1"),
        (2, "Category2"),
        (3, "Category3")
        )
    category = forms.ChoiceField(label="Category", choices=categories)
    types = (
        (1, "Type1"),
        (2, "Type2"),
        (3, "Type3"),
        (4, "Type4")
        )
    stock_type = forms.ChoiceField(label="Type", choices=types)
    colors = (
        (1, "Color1"),
        (2, "Color2"),
        (3, "Color3"),
        (4, "Color4"),
        (5, "Color5"),
        (6, "Color6"),
        (7, "Color7")
        )
    color = forms.ChoiceField(label="Color", choices=colors)
    sizes = (
        (1, "Size1"),
        (2, "Size2"),
        (3, "Size3"),
        (4, "Size4"),
        (5, "Size5"),
        (6, "Size6")
        )
    size = forms.ChoiceField(label="Size", choices=sizes)
    movements = (
        (1, "inbound"),
        (2, "outbound"),
        (3, "lost"),
        (4, "found"),
        (5, "definitive_lost"),
        (6, "repairing"),
        (7, "repairing_reactivated")
        )
    movement = forms.ChoiceField(label="Movement", choices=movements)    

