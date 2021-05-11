from django.core.management.base import BaseCommand
from os import system


class Command(BaseCommand):
    help = 'This command will delete all migrations files and create new ones'

    def handle(self, *args, **options):
        system('python manage.py removeoldmigrations')
        system('python manage.py makemigrations')
        system('python manage.py migrate')
