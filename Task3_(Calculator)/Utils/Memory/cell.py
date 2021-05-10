from typing import Union
from importlib import import_module


class Cell:
    """
    This is not an independent class.
    Do not use it for memorization.
    Use the <Memory> class (with the same API) for these purposes
    """

    __slots__ = ('value',)

    def __init__(self, value: Union[int, float] = 0):
        self.value = value

    @staticmethod
    def _calculate(value: str) -> Union[int, float]:
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
        return eval(value.replace('×', '*').replace('÷', '/').replace('^', '**').replace('√', 'sqrt'))

    def clear(self):
        self.value = 0

    def read(self) -> str:
        return str(self.value)

    def save(self, new_value: str):
        self.value = self._calculate(new_value)

    def plus(self, value: str):
        self.value += self._calculate(value)

    def minus(self, value: str):
        self.value -= self._calculate(value)
