from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'users/home.html')