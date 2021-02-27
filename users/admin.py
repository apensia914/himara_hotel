from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name','email', 'sex', 'language_preference')
    list_filter = ('sex', 'language_preference')
    fieldsets = UserAdmin.fieldsets + (
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('profile_picture', 'sex', 'language_preference'),
        }),
    )
