from PyQt5.QtWidgets import QGraphicsTextItem, QGraphicsItem
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor, QFont
from Utils import cached_property


class ChildText(QGraphicsTextItem):
    def __init__(self, parent: QGraphicsItem, relative_pos: QPoint, text: str = ''):
        self.relative_pos = relative_pos
        super(ChildText, self).__init__(parent)
        self.setTransform(self.transform().scale(1, -1))
        self.setDefaultTextColor(self.__color)
        self.setFont(QFont('Calibri', 10))
        self.setPlainText(text)

    def setPlainText(self, text: str) -> None:
        super(ChildText, self).setPlainText(text)
        _x = self.parentItem().pos.x() + self.relative_pos.x() - self.document().size().width() // 2
        _y = self.parentItem().pos.y() + self.relative_pos.y()
        self.setPos(QPoint(_x, _y))

    @cached_property
    def __color(self) -> QColor:
        return QColor('#000000')
