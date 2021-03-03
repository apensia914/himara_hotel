from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rooms'

urlpatterns = [
    path('', views.room_list, name='rooms'),
    path('<int:pk>/', views.room_detail, name='roomdetail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)