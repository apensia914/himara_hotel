from django.urls import path, include
from . import views

app_name = 'shops'

urlpatterns = [
    path('', views.shop_index, name='shopitem'),
    path('<int:pk>', views.item_detail, name='itemdetail'),
    path('search/', views.item_search, name='itemsearch'),
]