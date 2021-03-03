from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm

def reservation(request):
    form = ReservationForm()
    return render(request, 'reservations/reservation.html', {'form': form})