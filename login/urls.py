from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name = "index"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("auth-view", views.auth_view, name = "auth-view"),
    ]