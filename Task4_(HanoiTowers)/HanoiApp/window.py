from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QLabel, QPushButton, QLineEdit
from PyQt5.Qt import QFont, QRegExpValidator, QRegExp
from PyQt5.QtCore import Qt
from BaseObjects import BaseWindow
from HanoiApp import HanoiBackend
from DBORM.models import Iteration
from Widgets import Display, InfoDisplay


class HanoiWindow(QWidget, BaseWindow, HanoiBackend):
    def __init__(self, config):
        super(HanoiWindow, self).__init__()
        self.config = config
        self._init_ui()
        self._init_backend()

    def _init_ui(self):
        self.setWindowTitle(self.config.title)
        self.resize(*self.config.size)
        self.setMinimumSize(*self.config.min_size)
        self.setStyleSheet(self.config.style_sheet)

        self.grid = QGridLayout()

        _cols = len(self.config.student_id) // 2 + 2

        self.id_label = QLabel()
        self.id_label.setText(f'{self.config.student_name} | {self.config.student_id}')
        self.id_label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.id_label.setFont(QFont(self.config.font, self.config.font_size))
        self.id_label.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.id_label, 0, 0, 1, _cols)

        _start_iteration = Iteration.get(percent=0)

        self.display = Display()
        self.display.show_stage(_start_iteration)
        self.display.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.display.setFont(QFont(self.config.font, self.config.font_size))
        self.display.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.display, 1, 0, 5, _cols)

        self.info_display = InfoDisplay()
        self.info_display.show_info(_start_iteration)
        self.info_display.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.info_display.setFont(QFont(self.config.font, self.config.font_size))
        self.info_display.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.info_display, 6, 0, 1, _cols)

        _n = int()

        for col in range(_cols):
            if col == 0:
                self.button_start = QPushButton()
                self.button_start.setText('Draw begin')
                self.button_start.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
                self.button_start.setFont(QFont(self.config.font, self.config.font_size))
                self.grid.addWidget(self.button_start, 7, col, 2, 1)
            elif col == _cols - 1:
                self.button_end = QPushButton()
                self.button_end.setText('Draw end')
                self.button_end.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
                self.button_end.setFont(QFont(self.config.font, self.config.font_size))
                self.grid.addWidget(self.button_end, 7, col, 2, 1)
            else:
                entry = QLineEdit()
                entry.setValidator(QRegExpValidator(QRegExp(r'\d{2}')))
                entry.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
                entry.setFont(QFont(self.config.font, self.config.font_size))
                entry.setAlignment(Qt.AlignCenter)
                entry.setText(self.config.student_id[_n * 2:_n * 2 + 2])
                _n += 1
                self.grid.addWidget(entry, 7, col, 1, 1)
                setattr(self, f'entry_{col}', entry)

                button = QPushButton()
                button.setText(f'Draw: {col}')
                button.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
                button.setFont(QFont(self.config.font, self.config.font_size))
                self.grid.addWidget(button, 8, col, 1, 1)
                setattr(self, f'button_{col}', button)

        self.setLayout(self.grid)
