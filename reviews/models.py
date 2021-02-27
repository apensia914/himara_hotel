from django.db import models
from core.models import TimeStampModel

class Review(TimeStampModel):
    # Review Model Definition
    review = models.TextField()
    cleanliness = models.IntegerField()
    service = models.IntegerField()
    price = models.IntegerField()
    amenity = models.IntegerField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)

    def __str__(self):
        return self.room.name 
    
    def average_rating(self):
        average = (self.cleanliness + self.service + self.price + self.amenity) / 4
        return round(average, 2)
    
    average_rating.short_description = 'Average Rating'
