from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'shops'

urlpatterns = [
    path('', views.shop_index, name='shopitem'),
    path('<int:pk>', views.item_detail, name='itemdetail'),
    path('search/', views.search_item, name='itemsearch'),
] 
