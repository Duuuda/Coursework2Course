from typing import List
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtCore import Qt


class Display(QTextBrowser):
    __DEFAULT_TEXT = '\n0'

    def __init__(self, parrent=None):
        super(Display, self).__init__(parrent)
        self.clear()

    def setText(self, text: str) -> None:
        super(Display, self).setText(text)
        self.selectAll()
        self.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        cursor = self.textCursor()
        cursor.clearSelection()
        self.setTextCursor(cursor)

    def clear(self, default_text: str = __DEFAULT_TEXT) -> None:
        super(Display, self).clear()
        self.setText(default_text)

    def setRowsCount(self, num: int) -> None:
        self.setFixedHeight(self.fontMetrics().height() * num)

    @property
    def __lines(self) -> List[str]:
        return self.toPlainText().split('\n')

    @property
    def expression_result(self) -> str:
        return self.__lines[-1]

    @property
    def expression(self) -> str:
        if self.__lines[-2].endswith('='):
            self.append(self.__DEFAULT_TEXT)
        return self.__lines[-2]

    @expression.setter
    def expression(self, value: str):
        _lines = self.__lines[:-2]
        _lines.append(value)
        _lines.append(self.__lines[-1])
        self.setText('\n'.join(_lines))

    @property
    def input(self):
        if self.__lines[-2].endswith('='):
            self.append(self.__DEFAULT_TEXT)
        return self.expression_result

    @input.setter
    def input(self, value: str):
        _lines = self.__lines[:-1]
        _lines.append(value)
        self.setText('\n'.join(_lines))
