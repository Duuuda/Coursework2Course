from abc import abstractmethod
from PyQt5.QtWidgets import QPushButton, QMessageBox


class BaseBackend:
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
    def _unknown_button_exception_message(widget_text):
        def _event():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Critical error')
            msg.setText('The button method is not implemented!')
            msg.setInformativeText(f'Information for debugging: {widget_text}')
            msg.exec_()
        return _event
