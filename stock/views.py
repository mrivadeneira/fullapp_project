from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from .forms import StockMovementForm
from .models import Stock
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *

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
        
@api_view(['GET', 'POST'])
def stockapi_list(request):
    if request.method == 'GET':
        data = Stock.objects.all()

        serializer = StockSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def stockapi_details(request, pk):
    try:
        stock_item = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StockSerializer(stock_item, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stock_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)