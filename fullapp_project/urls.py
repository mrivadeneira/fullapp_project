"""fullapp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views #MR: Imported standar login module
from login import views as login_views #MR: Login app should be created at first before importing its views
from django.urls import re_path
from stock import views as stock_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", include("login.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', login_views.index, name='index'),
    # path('auth-view', login_views.auth_view, name='auth-view'),   
    path('login/', include('login.urls')),
    path('stock/', include('stock.urls')),
    re_path('^api/stock/$', stock_views.stockapi_list),
    re_path('^api/stock/([0-9])$', stock_views.stockapi_details),
]
