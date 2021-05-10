from typing import Dict
from PyQt5.QtWidgets import QComboBox
from Utils.Memory import Cell


class Memory(QComboBox):
    def __init__(self, parent=None, _memory_cells_count: int = 1):
        super(Memory, self).__init__(parent)
        self.__cells: Dict[str, Cell] = dict()

        self.setMemoryCellsCount(_memory_cells_count)

    def setMemoryCellsCount(self, memory_cells_count: int = 1):
        # WARNING: This method removes all data from memory locations

        if memory_cells_count <= 0:
            raise ValueError("the 'memory_cells_count' parameter must be greater than zero")

        self.clear()
        self.__cells.clear()

        for num in range(1, memory_cells_count + 1):
            self.addItem(f'M{num}')
            self.__cells[f'M{num}'] = Cell()

    def memoryClear(self):
        self.__cells[self.currentText()].clear()

    def memoryRead(self) -> str:
        return self.__cells[self.currentText()].read()

    def memorySave(self, new_value: str):
        self.__cells[self.currentText()].save(new_value)

    def memoryPlus(self, value: str):
        self.__cells[self.currentText()].plus(value)

    def memoryMinus(self, value: str):
        self.__cells[self.currentText()].minus(value)
