from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "login/index.html")

@login_required(redirect_field_name="login/login.html")
def auth_view(request):
    return render(request, "login/auth-view.html")
