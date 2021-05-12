from os import system
from requests import get
from requests.exceptions import ConnectionError
from threading import Thread
from time import sleep


def _open_site(site):
    def _is_django_available(_site):
        try:
            request = get(_site, timeout=1)
        except ConnectionError:
            return False
        if request.status_code != 200:
            return False
        return True

    while not _is_django_available(site):
        sleep(1)

    system(f'start {site}')


def main():
    thread = Thread(target=_open_site, args=('http://127.0.0.1:9000/',), daemon=True)
    thread.start()
    system('python manage.py lazyrunserver --port 9000 --no_collect_static --no_re_migrate')


if __name__ == '__main__':
    main()
