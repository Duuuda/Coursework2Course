from importlib import import_module
from Utils import BaseBackend


class SimpleModeBackend(BaseBackend):
    display_expression = None
    display_input = None

    def _get_event(self, widget_text):
        if widget_text == 'C':
            return self.__click_clear_button()
        elif widget_text == '←':
            return self.__click_backspace_button()
        elif widget_text == '·':
            return self.__click_dot_button()
        elif widget_text == '√':
            return self.__click_root_button()
        elif widget_text == '±':
            return self.__click_change_sign_button()
        elif widget_text in ('÷', '×', '-', '+', '^'):
            return self.__click_sign_button(widget_text)
        elif widget_text.isdecimal():
            return self.__click_num_button(widget_text)
        elif widget_text == '=':
            return self.__click_equally_button()
        elif widget_text == 'MC':
            return self._click_memory_clear_button()
        elif widget_text == 'MR':
            return self.__click_memory_read_button()
        elif widget_text == 'MS':
            return self.__click_memory_save_button()
        elif widget_text == 'M+':
            return self.__click_memory_plus_button()
        elif widget_text == 'M-':
            return self.__click_memory_minus_button()
        elif widget_text == '≡':
            return self._click_change_mode_button()
        else:
            return self._unknown_button_exception_message(widget_text)

    def __click_clear_button(self):
        def _event():
            self.display_expression.setText('')
            self.display_input.setText('0')
        return _event

    def __click_backspace_button(self):
        def _event():
            if (len(self.display_input.text()) == 1) or \
                    (self.display_input.text().startswith('-') and len(self.display_input.text()) == 2) or \
                    (self.display_input.text()[-1] == ')'):
                self.display_input.setText('0')
            else:
                self.display_input.setText(self.display_input.text()[:-1])

        return _event

    def __click_dot_button(self):
        def _event():
            if '.' not in self.display_input.text():
                self.display_input.setText(self.display_input.text() + '.')

        return _event

    def __click_root_button(self):
        def _event():
            self.display_input.setText(f'√({self.display_input.text()})')

        return _event

    def __click_change_sign_button(self):
        def _event():
            if self.display_input.text() != '0':
                if self.display_input.text()[0] == '-':
                    self.display_input.setText(self.display_input.text()[1:])
                else:
                    self.display_input.setText('-' + self.display_input.text())

        return _event

    def __click_sign_button(self, sign: str):
        def _event():
            if self.display_expression.text()[-1:] != '=':
                if self.display_input.text() == '0' and self.display_expression.text() != '':
                    self.display_expression.setText(self.display_expression.text()[:-1] + sign)
                else:
                    if self.display_input.text()[0] == '-':
                        self.display_expression.setText(
                            self.display_expression.text() + '(' + self.display_input.text() + ')' + sign)
                    else:
                        self.display_expression.setText(
                            self.display_expression.text() + self.display_input.text() + sign)
                    self.display_input.setText('0')

        return _event

    def __click_num_button(self, num: str):
        def _event():
            if self.display_expression.text()[-1:] == '=':
                self.display_expression.setText('')
                self.display_input.setText('0')
            if self.display_input.text()[-1] != ')':
                if self.display_input.text() == '0':
                    if num != '00':
                        self.display_input.setText(num)
                else:
                    self.display_input.setText(self.display_input.text() + num)

        return _event

    def __click_equally_button(self):
        def _event():
            # DYNAMIC IMPORT ZONE -------------------------
            math = import_module('math')
            # WARNING
            # All these imports are used in the eval function
            sqrt = getattr(math, 'sqrt')
            # END OF DYNAMIC IMPORT ZONE ------------------

            if not (self.display_expression.text() == '' and self.display_input.text() == '0') and \
                    self.display_expression.text()[-1:] != '=':
                if self.display_expression.text() == '':
                    expression = self.display_input.text()
                elif self.display_input.text() == '0':
                    expression = self.display_expression.text()[:-1]
                else:
                    if self.display_input.text()[0] == '-':
                        expression = self.display_expression.text() + '(' + self.display_input.text() + \
                                     ')'
                    else:
                        expression = self.display_expression.text() + self.display_input.text()
                self.display_expression.setText(expression + '=')
                expression = expression.replace('×', '*').replace('÷', '/').replace('^', '**').replace('√', 'sqrt')
                try:
                    self.display_input.setText(str(eval(expression)))
                except Exception as error:
                    self._equally_button_exception_message(error)

        return _event

    def __click_memory_read_button(self):
        def _event():
            self.display_input.setText(self.memory.memoryRead())

        return _event

    def __click_memory_save_button(self):
        def _event():
            self.memory.memorySave(self.display_input.text())

        return _event

    def __click_memory_plus_button(self):
        def _event():
            self.memory.memoryPlus(self.display_input.text())

        return _event

    def __click_memory_minus_button(self):
        def _event():
            self.memory.memoryMinus(self.display_input.text())

        return _event
