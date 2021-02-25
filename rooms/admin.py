from django.contrib import admin
from .models import Room, RoomType, Amenity, Facility, Photo

@admin.register(Amenity, Facility, RoomType)
class RoomItemAdmin(admin.ModelAdmin):
    # Room Items Admin Definition
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # Room Admin Definition 
    pass

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    # Room Admin Definition 
    pass