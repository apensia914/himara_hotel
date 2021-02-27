from django.contrib import admin
from .models import ShopItem

@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_price', 'item_picture')
    search_fields = ('item_name',)