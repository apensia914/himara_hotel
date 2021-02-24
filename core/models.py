from django.db import models

class TimeStampModel(models.Model):
    room_created_date = models.DateTimeField(auto_now_add=True)
    room_updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True