import random
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from users.models import User
from rooms.models import Room


class Command(BaseCommand):
    help = 'Automatically create random rooms'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', help='How many rooms you would like to create'
        )

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        all_users = User.objects.all()
        room_types = Room.RoomType.objects.all()
        seeder.add_entity(Room, 10, {
            'host': lambda x: random.choice(all_users),
            'room_types': lambda x: random.choice(room_types),
        })

        seeder.execute()

        self.stdout.write(self.style.SUCCESS('Rooms created'))