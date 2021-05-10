from importlib import import_module
from Utils import BaseBackend


class ExtendedModeBackend(BaseBackend):
    display_id = None
    display = None

    def _get_event(self, widget_text):
        if widget_text == 'C':
            return self.__click_clear_button()
        elif widget_text == '←':
            return self.__click_backspace_button()
        elif widget_text == '·':
            return self.__click_dot_button()
        elif widget_text in ('√', 'sin', 'cos', 'tan', 'ln'):
            return self.__click_func_button(widget_text)
        elif widget_text == '±':
            return self.__click_change_sign_button()
        elif widget_text in ('÷', '×', '-', '+', '^', '^3'):
            return self.__click_sign_button(*widget_text)
        elif widget_text.isdecimal():
            return self.__click_num_button(widget_text)
        elif widget_text == '=':
            return self.__click_equally_button()
        elif widget_text == '<>':
            return self.__click_change_id_button()
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
            self.display.clear()

        return _event

    def __click_backspace_button(self):
        def _event():
            if (len(self.display.input) == 1) or \
                    (self.display.input.startswith('-') and len(self.display.input) == 2) or \
                    (self.display.input[-1] == ')'):
                self.display.input = '0'
            else:
                self.display.input = self.display.input[:-1]

        return _event

    def __click_dot_button(self):
        def _event():
            if '.' not in self.display.input:
                self.display.input += '.'

        return _event

    def __click_func_button(self, func: str):
        def _event():
            self.display.input = f'{func}({self.display.input})'

        return _event

    def __click_change_sign_button(self):
        def _event():
            if self.display.input != '0':
                if self.display.input[0] == '-':
                    self.display.input = self.display.input[1:]
                else:
                    self.display.input = '-' + self.display.input

        return _event

    def __click_sign_button(self, sign: str, _num: str = '0'):
        def _event():
            if self.display.expression[-1:] != '=':
                if self.display.input == '0' and self.display.expression != '':
                    self.display.expression = self.display.expression[:-1] + sign
                else:
                    if self.display.input[0] == '-':
                        self.display.expression = self.display.expression + '(' + self.display.input + ')' + sign
                    else:
                        self.display.expression = self.display.expression + self.display.input + sign
                self.display.input = _num

        return _event

    def __click_num_button(self, num: str):
        def _event():
            if self.display.expression[-1:] == '=':
                self.display.expression = ''
                self.display.input = '0'
            if self.display.input[-1] != ')':
                if self.display.input == '0':
                    if num != '00':
                        self.display.input = num
                else:
                    self.display.input = self.display.input + num

        return _event

    def __click_equally_button(self):
        def _event():
            # DYNAMIC IMPORT ZONE -------------------------
            math = import_module('math')
            # WARNING
            # All these imports are used in the eval function
            sqrt = getattr(math, 'sqrt')
            ln = getattr(math, 'log')
            sin = getattr(math, 'sin')
            cos = getattr(math, 'cos')
            tan = getattr(math, 'tan')
            # END OF DYNAMIC IMPORT ZONE ------------------

            if not (self.display.expression == '' and self.display.input == '0') and \
                    self.display.expression[-1:] != '=':
                if self.display.expression == '':
                    expression = self.display.input
                elif self.display.input == '0':
                    expression = self.display.expression[:-1]
                else:
                    if self.display.input[0] == '-':
                        expression = self.display.expression + '(' + self.display.input + ')'
                    else:
                        expression = self.display.expression + self.display.input
                self.display.expression = expression + '='
                expression = expression.replace('×', '*').replace('÷', '/').replace('^', '**').replace('√', 'sqrt')
                try:
                    self.display.input = str(eval(expression))
                except Exception as error:
                    self._equally_button_exception_message(error)

        return _event

    def __click_change_id_button(self):
        def _event():
            self.memory.setMemoryCellsCount(self.display_id.memory_cells_count)
            self.display.setRowsCount(self.display_id.display_rows_count)

        return _event

    def __click_memory_read_button(self):
        def _event():
            self.display.input = self.memory.memoryRead()

        return _event

    def __click_memory_save_button(self):
        def _event():
            self.memory.memorySave(self.display.expression_result)

        return _event

    def __click_memory_plus_button(self):
        def _event():
            self.memory.memoryPlus(self.display.expression_result)

        return _event

    def __click_memory_minus_button(self):
        def _event():
            self.memory.memoryMinus(self.display.expression_result)

        return _event
