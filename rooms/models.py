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
    photo = models.ImageField(upload_to='room_picture')
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

    def __str__(self):
        return self.room.name

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
    BED_SINGLE = 'single'
    BED_DELUXE = 'deluxe'
    BED_QUEEN = 'queen'
    BED_KING = 'king'
    BED_CHOICES = [
        (BED_SINGLE, 'Single'),
        (BED_DELUXE, 'Deluxe'),
        (BED_QUEEN, 'Queen'),
        (BED_KING, 'King'),
    ]

    name = models.CharField(max_length=140, verbose_name='Room Name')
    description = models.TextField(verbose_name='Room Description')
    price = models.FloatField(verbose_name='Room Rate')
    bed_type = models.CharField(choices=BED_CHOICES, max_length=10, verbose_name='Bed Type')
    smoke = models.BooleanField(verbose_name='Smoking Availability', default=False)
    early_checkin = models.BooleanField(verbose_name='Early Check-in', default=False)
    check_in = models.TimeField()
    check_out = models.TimeField()
    room_type = models.ForeignKey('RoomType', related_name='rooms', on_delete=models.SET_NULL, null=True, blank=True)
    amenities = models.ManyToManyField('Amenity', related_name='rooms', blank=True)
    facilities = models.ManyToManyField('Facility', related_name='rooms', blank=True)

    def __str__(self):
        return self.name