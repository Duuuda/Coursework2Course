from PyQt5.QtWidgets import QLineEdit
from PyQt5.Qt import QRegExpValidator, QRegExp


class DisplayId(QLineEdit):
    def __init__(self, *__args, _default_text: str = '0'):
        super(DisplayId, self).__init__(*__args)

        # Guarantee of getting an int-shaped string
        self.setValidator(QRegExpValidator(QRegExp(r'\d{8}')))
        self.__default_text = _default_text
        self.setDefaultText(self.__default_text)

    def text(self) -> str:
        # ALWAYS returns a NON-empty string

        if super(DisplayId, self).text() == '':
            self.setText(self.__default_text)
        return super(DisplayId, self).text()

    def setDefaultText(self, text: str = '0') -> None:
        if not text.isdecimal():
            raise ValueError("the 'text' parameter must be int-shaped string")

        self.__default_text = text
        self.setText(self.__default_text)

    @property
    def display_rows_count(self) -> int:
        _rows_count = self.__sum(int(self.text()))
        if _rows_count <= 1:
            return 10
        return _rows_count

    @property
    def memory_cells_count(self) -> int:
        _cells_count = self.__sum(int(self.text()[-3:]))
        if _cells_count <= 1:
            return 2
        return _cells_count

    @staticmethod
    def __sum(number: int) -> int:
        summed_number = int()
        while number > 9:
            while number > 0:
                summed_number += number % 10
                number //= 10
            number = summed_number
            summed_number = 0
        return number
