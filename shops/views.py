from django.shortcuts import render
import django_filters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ShopItem
from .forms import ShopSearchForm

def shop_index(request):
    shopitem_list = ShopItem.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(shopitem_list, 9) # Shows 9 items per page

    try:
        shopitems = paginator.page(page)
    except PageNotAnInteger:
        shopitems = paginator.page(1)
    except EmptyPage:
        shopitems = paginator.page(paginator.num_pages)

    return render(request, 'shops/shopitem_list.html', {'shopitems': shopitems})

def item_detail(request, pk):
    item = ShopItem.objects.get(pk=pk)
    return render(request, 'shops/shopitem_detail.html', {'item': item})

def search_item(request):  
    form = ShopSearchForm()
    return render(request, 'shops/shopitem_search.html', {'form': form})