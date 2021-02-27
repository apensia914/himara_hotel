from django.shortcuts import render
from .models import Room

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})

def room_detail(request, pk):
    rooms = Room.objects.filter(pk=pk)
    return render(request, 'rooms/room_detail.html', {'rooms': rooms})