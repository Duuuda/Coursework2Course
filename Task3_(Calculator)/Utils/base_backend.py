from abc import abstractmethod
from PyQt5.QtWidgets import QPushButton, QMessageBox


class BaseBackend:
    memory = None
    other_ui = None

    def _init_backend(self):
        for widget_name in self.__dir__():
            if not widget_name.startswith('__') and not widget_name.endswith('__'):
                widget = getattr(self, widget_name, None)
                if widget is not None and isinstance(widget, QPushButton):
                    widget.clicked.connect(self._get_event(widget.text()))

    @abstractmethod
    def _get_event(self, widget_text):
        raise NotImplementedError('This method must be overridden')

    @staticmethod
    def _equally_button_exception_message(error: Exception):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle('Calculate error')
        msg.setText('An exception occurred when calculating the result!')
        msg.setInformativeText(str(error))
        msg.exec_()

    @staticmethod
    def _unknown_button_exception_message(widget_text):
        def _event():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Critical error')
            msg.setText('The button method is not implemented!')
            msg.setInformativeText(f'Information for debugging: {widget_text}')
            msg.exec_()
        return _event

    def _click_memory_clear_button(self):
        def _event():
            self.memory.memoryClear()

        return _event

    def _click_change_mode_button(self):
        def _event():
            self.hide()
            self.other_ui.show()

        return _event
