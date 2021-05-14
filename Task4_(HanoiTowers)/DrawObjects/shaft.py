from PyQt5.QtWidgets import QGraphicsPolygonItem
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor, QPolygonF
from DrawObjects import ChildText
from Utils import cached_property


class Shaft(QGraphicsPolygonItem):
    __scale = 16  # must be even for better display

    def __init__(self, pos: QPoint, _disks_count: int = 10, _number: int = 0):
        if _disks_count < 1:
            raise ValueError('_disks_count param must be positive')

        self.pos = pos
        self.disks_count = _disks_count
        new_polygon = QPolygonF()
        for delta in self.__mesh:
            new_polygon.append(QPoint(self.pos.x() + (delta[0] * self.__scale),
                                      self.pos.y() + (delta[1] * self.__scale)))

        super(Shaft, self).__init__(new_polygon)
        self.setPen(self.__color)
        self.setBrush(self.__color)

        self.text = ChildText(self, QPoint(0, 0), str(_number))

    def __getitem__(self, num: int) -> QPoint:
        if not isinstance(num, int):
            raise TypeError('Index must be integer')
        if num < 0:
            raise IndexError('Index must be positive')
        num += 0.8
        return QPoint(self.pos.x(), self.pos.y() + self.__scale * num)

    @cached_property
    def __mesh(self) -> tuple:
        return (-2.15, 0.0),\
               (-2.15, 0.3),\
               (-0.15, 0.3),\
               (-0.15, self.disks_count + 1 + 0.3),\
               (0.15, self.disks_count + 1 + 0.3),\
               (0.15, 0.3),\
               (2.15, 0.3),\
               (2.15, 0.0)

    @cached_property
    def __color(self) -> QColor:
        return QColor('#8B4513')
