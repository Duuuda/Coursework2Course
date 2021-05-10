from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSizePolicy
from PyQt5.Qt import QFont
from PyQt5.QtCore import Qt
from ExtendedMode import ExtendedModeBackend, button_mask
from Utils import BaseUI, Display, DisplayId
from Utils.Memory import Memory


class ExtendedModeUI(QWidget, BaseUI, ExtendedModeBackend):
    def __init__(self, config):
        super(ExtendedModeUI, self).__init__()
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

        self.label_id = QLabel()
        self.label_id.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding))
        self.label_id.setFont(QFont(self.config.font, 16))
        self.label_id.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_id.setText('MUIV ID:')
        self.grid.addWidget(self.label_id, 0, 0, 1, 1)

        self.display_id = DisplayId()
        self.display_id.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.display_id.setFont(QFont(self.config.font, 16))
        self.display_id.setAlignment(Qt.AlignLeft)
        self.display_id.setDefaultText(self.config.student_id)
        self.grid.addWidget(self.display_id, 0, 1, 1, 3)

        self.display_name = QLabel()
        self.display_name.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.display_name.setFont(QFont(self.config.font, 16))
        self.display_name.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.display_name.setText(self.config.student_name)
        self.grid.addWidget(self.display_name, 1, 0, 1, 5)

        self.display = Display()
        self.display.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.display.setFont(QFont(self.config.font, 16))
        self.display.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.display.setRowsCount(self.display_id.display_rows_count)
        self.grid.addWidget(self.display, 2, 0, 1, 5)

        self.memory.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.memory.setFont(QFont(self.config.font, 16))
        self.memory.setMemoryCellsCount(self.display_id.memory_cells_count)
        self.grid.addWidget(self.memory, 3, 2, 1, 1)

        self._init_buttons(button_mask)

        self.setLayout(self.grid)
