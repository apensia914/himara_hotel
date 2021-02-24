from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home),
=======
    path('', views.home, name='home'),
>>>>>>> 5073177 (Users Admin & Template Connecting)
]