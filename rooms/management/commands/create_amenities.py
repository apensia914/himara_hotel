from django.core.management.base import BaseCommand, CommandError
from rooms.models import Amenity

class Command(BaseCommand):
    help = 'Automatically create amenities'

    def handle(self, *args, **options):
        amenities = [
            'Private Balcony',
            'Air-conditioner',
            'Wi-Fi',
            'Bath Items',
            'Aroma',
            'Beverages',
            'Snacks',
            'Safe',
            'Iron',
            'Newspaper'
        ]

        for amenity in amenities:
            Amenity.objects.create(name=amenity)
        self.stdout.write(self.style.SUCCESS('Amenities created'))
        