from abc import abstractmethod
from PyQt5.QtWidgets import QPushButton, QSizePolicy
from PyQt5.Qt import QFont
from Utils import chained


class BaseUI:
    config = None
    grid = None

    @chained
    def add_other_ui(self, other_ui):
        self.other_ui = other_ui

    @abstractmethod
    def _init_ui(self):
        raise NotImplementedError('This method must be overridden')

    def _init_buttons(self, button_mask):
        for row, line in enumerate(button_mask):
            for column, button_data in enumerate(line):
                if button_data is not None:
                    button = QPushButton()
                    button.setText(button_data.text)
                    button.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
                    button.setFont(QFont(self.config.font, 20))
                    self.grid.addWidget(button, row, column, 1, 1)
                    setattr(self, f'button_{button_data.name}', button)
