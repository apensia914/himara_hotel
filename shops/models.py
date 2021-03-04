from django.db import models
from django.urls import reverse
from core.models import TimeStampModel

class ShopItem(TimeStampModel):
    item_name = models.CharField(max_length=30, verbose_name='Item Name')
    item_price = models.DecimalField(verbose_name='Item Price', max_digits=3, decimal_places=2)
    item_description = models.TextField(verbose_name='Item Description')
    item_picture = models.ImageField(upload_to='item_picture', verbose_name='Item Picture', blank=True)
    buyer = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.item_name

    def item_rating(self):
        pass 

    def get_absolute_url(self):
        return reverse('shops:itemdetail', kwargs={'pk': self.pk})


    def item_thumbnail(self):
        item_picture = self.photos.all()[:1]
        return photo.file.url