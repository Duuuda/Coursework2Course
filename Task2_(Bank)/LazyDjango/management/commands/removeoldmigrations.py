from django.core.management.base import BaseCommand
from os import listdir, remove
from os.path import isdir, exists


class Command(BaseCommand):
    help = 'This command delete all migrations files in "<App>/migrations"'

    def handle(self, *args, **options):
        for app_dir in listdir('.'):
            if isdir(app_dir) and exists(f'{app_dir}/migrations'):
                for migrations_file in listdir(f'{app_dir}/migrations'):
                    if migrations_file != '__init__.py' and migrations_file.endswith('.py'):
                        remove(f'{app_dir}/migrations/{migrations_file}')
