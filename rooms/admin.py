from django.contrib import admin
from .models import Room, RoomType, Amenity, Facility, Photo
from django.utils.html import mark_safe

@admin.register(Amenity, Facility, RoomType)
class RoomItemAdmin(admin.ModelAdmin):
    # Room Items Admin Definition
    list_display = ('name',)

class PhotoInline(admin.TabularInline):
    '''Tabular Inline View for Photo'''
    model = Photo

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # Room Admin Definition 

    inlines = (PhotoInline,)

    fieldsets = (
        (
            'Basic Info',
            {'fields': ('name', 'price', 'bed_type', 'description', 'smoke')},
        ),
        (
            'Times',
            {'fields': ('check_in', 'check_out', 'early_checkin')},
        ),
        (
            'Others',
            {'fields': ('amenities', 'facilities')},
        )
    )
    list_display = ('name', 'price', 'bed_type', 'room_type', 'smoke', 'early_checkin', 'check_in', 'check_out', 'count_amenities', 'count_facilities')
    search_fields = ('amenities__name', 'facilities__name', 'bed_type')
    filter_horizontal = ('amenities', 'facilities')
    ordering = ('name', 'price')

    def count_amenities(self, obj):
        return obj.amenities.count()
    
    def count_facilities(self, obj):
        return obj.facilities.count()

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    # Photo Admin Definition 
    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="70px" src="{obj.photo.url}" />')
    
    get_thumbnail.short_description = 'Thumbnail'