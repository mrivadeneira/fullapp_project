from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from .forms import StockMovementForm
from .models import Stock

def stock_snapshot(request):
    stock = Stock.objects.select_related("category","stock_type","color","size","movement").all()
    ctx = {"stock": stock}
    return render(request, "stock/stock.html", ctx)

def stock_movement(request):
    if request.method == "POST":
        form = StockMovementForm(request.POST)
        if form.is_valid():
            Stock.objects.create(
                sku = form.cleaned_data["sku"],
                category = form.cleaned_data["category"],
                stock_type = form.cleaned_data["stock_type"],
                color = form.cleaned_data["color"],
                size = form.cleaned_data["size"],
                movement = form.cleaned_data["movement"]
            )
            return HttpResponseRedirect("stock")
    else:
        form = StockMovementForm()
        ctx = {"form": form}
        return render(request, "stock/stock-movement.html", ctx)
        