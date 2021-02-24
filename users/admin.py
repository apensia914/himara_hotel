from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
<<<<<<< HEAD
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name','email', 'sex', 'language_preference')
    list_filters = ('sex', 'language_preference')
    fieldsets = (
        ('Basic Information', {
            'fields': ('username', 'first_name', 'last_name', 'email')
=======
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'sex', 'language_preference')
    list_filter = ('sex', 'language_preference')
    fieldsets = (
        ('Basic Info', {
            'fields': ('username', 'first_name', 'last_name', 'email'),
>>>>>>> 5073177 (Users Admin & Template Connecting)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('profile_picture', 'sex', 'language_preference'),
        }),
    )
