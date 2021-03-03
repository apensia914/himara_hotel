from django.urls import path, include
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.reservation, name='reservation'),
]