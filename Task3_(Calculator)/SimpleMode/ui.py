from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QSizePolicy
from PyQt5.Qt import QFont
from PyQt5.QtCore import Qt
from SimpleMode import SimpleModeBackend, button_mask
from Utils import BaseUI
from Utils.Memory import Memory


class SimpleModeUI(QWidget, BaseUI, SimpleModeBackend):
    def __init__(self, config):
        super(SimpleModeUI, self).__init__()
        self.config = config
        self.memory = Memory()
        self._init_ui()
        self._init_backend()

    def _init_ui(self):
        self.setWindowTitle(self.config.title)
        self.resize(*self.config.size)
        self.setMinimumSize(*self.config.min_size)
        self.setStyleSheet(self.config.style_sheet)

        self.grid = QGridLayout()

        self.display_expression = QLineEdit()
        self.display_expression.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.display_expression.setFont(QFont(self.config.font, 16))
        self.display_expression.setReadOnly(True)
        self.display_expression.setDragEnabled(False)
        self.display_expression.setAlignment(Qt.AlignRight)
        self.grid.addWidget(self.display_expression, 0, 0, 1, 5)

        self.display_input = QLineEdit()
        self.display_input.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.display_input.setFont(QFont(self.config.font, 25))
        self.display_input.setReadOnly(True)
        self.display_input.setDragEnabled(False)
        self.display_input.setAlignment(Qt.AlignRight)
        self.display_input.setText('0')
        self.grid.addWidget(self.display_input, 1, 0, 1, 5)

        self._init_buttons(button_mask)

        self.setLayout(self.grid)
