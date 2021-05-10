from PyQt5.QtWidgets import QLineEdit
from typing import Union
from BaseObjects import BaseBackend
from DBORM.models import Iteration


class HanoiBackend(BaseBackend):
    display = None
    info_display = None

    def _get_event(self, widget_text: str):
        if widget_text == 'Draw begin':
            return self.__click_get_iteration_button(0)
        elif widget_text == 'Draw end':
            return self.__click_get_iteration_button(100)
        elif widget_text.startswith('Draw: '):
            return self.__click_get_iteration_button(getattr(self, f"entry_{widget_text.lstrip('Draw: ')}"))
        else:
            return self._unknown_button_exception_message(widget_text)

    def __click_get_iteration_button(self, percent: Union[int, QLineEdit]):
        def _event():
            if isinstance(percent, int):
                _iteration = Iteration.get(percent=percent)
            else:
                _iteration = Iteration.get(percent=int(percent.text()))

            self.display.show_stage(_iteration)
            self.info_display.show_info(_iteration)

        return _event
