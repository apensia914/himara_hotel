from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = 'Automatically create random users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', help='How many users you would like to create'
        )

    def handle(self, *args, **options):
        seeder = Seed.seeder()
    
        seeder.add_entity(User, 10, {
            'is_staff': False,
            'is_superuser': False,
        })

        seeder.execute()

        self.stdout.write(self.style.SUCCESS('Users created'))