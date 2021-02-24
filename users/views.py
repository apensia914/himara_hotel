from django.shortcuts import render
from .models import User

def home(request):
<<<<<<< HEAD
    return render(request, 'base.html')
=======
    return render(request, 'users/home.html')
>>>>>>> 5073177 (Users Admin & Template Connecting)
