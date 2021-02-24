from django.contrib import admin
from .models import Room

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass