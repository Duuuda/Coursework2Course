from os import system


def requirements_update():
    system('pip3 freeze > requirements.txt')
    print('All requirements was collected into "requirements.txt"')


def requirements_install():
    system('pip install -r requirements.txt')
    print('All requirements was installed from "requirements.txt"')


def main():
    while True:
        try:
            question = 'What do you want to do?\n' \
                       '1) Update "requirements.txt"\n' \
                       '2) Install requirements from "requirements.txt\n' \
                       '3) Exit\n' \
                       '-:'
            answer = int(input(question))
            if answer == 1:
                requirements_update()
                break
            elif answer == 2:
                requirements_install()
                break
            elif answer == 3:
                raise SystemExit
            else:
                raise ValueError
        except ValueError:
            print('Incorrect answer! Please, try again...')


if __name__ == '__main__':
    main()
