from django.db import models
from core.models import TimeStampModel

class AbstractRoomItem(TimeStampModel):
    # Abstract Room Item 
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Photo(TimeStampModel):
    # Room Photos
    photo = models.ImageField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

class Amenity(AbstractRoomItem):
    # Room Amenities 
    class Meta:
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'

class Facility(AbstractRoomItem):
    # Room Facilities
    
    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'


class RoomType(AbstractRoomItem):
    # Room Type
    class Meta:
        verbose_name = 'Room Type'
        verbose_name_plural = 'Room Types'

class Room(TimeStampModel):
    # Room Model Definition
    name = models.CharField(max_length=140, verbose_name='Room Name')
    description = models.TextField(verbose_name='Room Description')
    price = models.FloatField(verbose_name='Room Rate')
    bed = models.IntegerField(verbose_name='Number of beds')
    wifi = models.BooleanField(verbose_name='Free Wi-Fi', default=False)
    breakfast = models.BooleanField(verbose_name='Breakfast', default=False)
    check_in = models.TimeField()
    check_out = models.TimeField()
    room_type = models.ForeignKey('RoomType', on_delete=models.SET_NULL, null=True, blank=True)
    amenities = models.ManyToManyField('Amenity', blank=True)
    facilities = models.ManyToManyField('Facility', blank=True)

    def __str__(self):
        return self.name 

