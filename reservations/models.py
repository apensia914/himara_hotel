from django.db import models
from core.models import TimeStampModel
from django.utils import timezone

class Reservation(TimeStampModel):
    # Reservation Model Definition
    STATUS_PENDING = 'pending'
    STATUS_CONFIRM = 'confirm'
    STATUS_CANCELED = 'canceled'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRM, 'Confirm'),
        (STATUS_CANCELED, 'Canceled'),
    ]

    status = models.CharField(choices=STATUS_CHOICES, max_length=10, verbose_name='Reservation Status', default=STATUS_PENDING)
    guest = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Guest')
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE, verbose_name='Room Reserved')
    check_in = models.DateField(verbose_name='Check-in Date')
    check_out = models.DateField(verbose_name='Check-out Date')

    def __str__(self):
        return f'{self.room}: {self.check_in} ~ {self.check_out}'

    def progress_status(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    progress_status.boolean = True