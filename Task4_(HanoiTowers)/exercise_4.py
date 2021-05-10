from PyQt5.QtWidgets import QApplication
from sys import argv, exit
from sqlalchemy_utils import database_exists
from HanoiApp import HAConfig, HanoiWindow
from DBORM.models import Iteration
from Utils import bake


def main():
    if not database_exists(Iteration.__databaseurl__):
        bake(HAConfig.student_id)

    app = QApplication(argv)
    hanoi_window = HanoiWindow(HAConfig)
    hanoi_window.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()
