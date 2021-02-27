import random
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from shops.models import ShopItem
from users.models import User

class Command(BaseCommand):
    help = 'Automatically create random shop items'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', help='How many items you would like to create'
        )

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        buyers = User.objects.all()

        seeder.add_entity(ShopItem, 30, {
            'buyer': lambda x: random.choice(buyers),
        })

        seeder.execute()

        self.stdout.write(self.style.SUCCESS('Shop Items Created'))