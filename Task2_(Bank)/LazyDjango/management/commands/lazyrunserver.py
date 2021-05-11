from django.core.management.base import BaseCommand
from os import system


class Command(BaseCommand):
    help = 'This command prepares and launches Django without user intervention'

    def add_arguments(self, parser):
        parser.add_argument('-host', '--host',
                            action='store', default='127.0.0.1',
                            help='Start your project on this address')
        parser.add_argument('-p', '--port',
                            action='store', default='8000',
                            help='Start your project on this port')
        parser.add_argument('-ncs', '--no_collect_static',
                            action='store_true', default=False,
                            help='Start your project without collecting static')
        parser.add_argument('-nrm', '--no_re_migrate',
                            action='store_true', default=False,
                            help='Start your project without re-migrate')
        parser.add_argument('-ncdu', '--no_check_default_user',
                            action='store_true', default=False,
                            help='Start your project without checking default user in db')

    def handle(self, *args, **options):
        if not options['no_collect_static']:
            system('python manage.py collectstatic --no-input')
        if not options['no_re_migrate']:
            system('python manage.py remigrate')
        if not options['no_check_default_user']:
            system('python manage.py checkdefaultuser')

        system(f'python manage.py runserver {options["host"]}:{options["port"]}')
