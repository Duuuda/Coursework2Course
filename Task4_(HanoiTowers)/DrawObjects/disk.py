from PyQt5.QtWidgets import QGraphicsPolygonItem
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor, QPolygonF
from random import seed, randint
from DrawObjects import ChildText
from Utils import cached_property


class Disk(QGraphicsPolygonItem):
    __scale = 16  # must be even for better display

    def __init__(self, pos: QPoint, diameter: int):
        self.pos = pos
        self.diameter = diameter
        new_polygon = QPolygonF()
        for delta in self.__mesh:
            new_polygon.append(QPoint(self.pos.x() + delta[0],
                                      self.pos.y() + (delta[1] * self.__scale)))

        super(Disk, self).__init__(new_polygon)
        self.setPen(self.__color)
        self.setBrush(self.__color)

        self.text = ChildText(self, QPoint(0, self.__scale // 4 * 3), str(diameter))

    @cached_property
    def __mesh(self) -> tuple:
        diameter_half = self.diameter / 2
        return (-diameter_half, -0.5), (-diameter_half, 0.5), (diameter_half, 0.5), (diameter_half, -0.5)

    @cached_property
    def __color(self) -> QColor:
        seed(self.diameter)
        r = hex(randint(0, 255))[2:]
        g = hex(randint(0, 255))[2:]
        b = hex(randint(0, 255))[2:]
        seed()
        return QColor(f'#{r:0>2}{g:0>2}{b:0>2}')
