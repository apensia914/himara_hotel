from django.urls import path, include
from . import views

app_name = 'rooms'

urlpatterns = [
    path('', views.room_list, name='rooms'),
    path('<int:pk>/', views.room_detail, name='roomdetail'),
]