from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings


class Command(BaseCommand):
    help = 'This command check and/or create default user to db'

    def handle(self, *args, **options):
        print('Default user check... ', end='')
        if not User.objects.exists():
            User.objects.create_superuser(**settings.DEFAULT_USER)
        print('OK')
