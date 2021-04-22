from django.urls import path
from . import views

urlpatterns = [
    path("stock", views.stock_snapshot, name = "stock_snapshot"),
    path("stock-movement", views.stock_movement, name = "stock_movement")

]