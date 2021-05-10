from settings import SMConfig, EMConfig
from PyQt5.QtWidgets import QApplication
from ExtendedMode import ExtendedModeUI
from SimpleMode import SimpleModeUI
from sys import argv, exit


def main():
    app = QApplication(argv)
    window_si = SimpleModeUI(SMConfig)
    window_ex = ExtendedModeUI(EMConfig)
    window_si.add_other_ui(window_ex).show()
    window_ex.add_other_ui(window_si).hide()
    exit(app.exec_())


if __name__ == '__main__':
    main()
