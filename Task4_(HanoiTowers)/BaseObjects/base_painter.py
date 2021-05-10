from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt5.QtGui import QResizeEvent, QPainter
from PyQt5.QtCore import Qt, QPoint
from typing import List, Union
from DrawObjects import Shaft, Disk


class BasePainter(QGraphicsView):
    def __init__(self,
                 screen_width: int = 800, screen_height: int = 500,
                 _scene: QGraphicsScene = None,  # This scene will be cleaned up!
                 _antialiasing: bool = True):
        if _scene is None:
            _scene = QGraphicsScene()

        super(BasePainter, self).__init__(_scene)

        if _antialiasing:
            self.setRenderHint(QPainter.Antialiasing)

        self.scene().setSceneRect(0, 0, screen_width, screen_height)
        self.scale(1, -1)
        self.resizeEvent()

        self.scene().clear()

    def resizeEvent(self, event: QResizeEvent = None) -> None:
        self.fitInView(self.scene().sceneRect(), Qt.KeepAspectRatio)

    @property
    def _shafts(self) -> List[Union[Shaft, QGraphicsItem]]:
        return list(filter(lambda obj: isinstance(obj, Shaft), self.scene().items(Qt.AscendingOrder)))

    def __draw_shafts(self, shafts_count: int, disks_on_shafts_count: int) -> None:
        interval = self.scene().width() / (shafts_count + 1)
        for shaft_index, shaft_num in zip(range(1, shafts_count + 1), range(shafts_count, 0, -1)):
            self.scene().addItem(Shaft(QPoint(shaft_index * interval, 30), disks_on_shafts_count, shaft_num))

    def _draw_scheme(self,
                     scheme: List[List[int]],
                     diameter_of_disk_in_motion: int = None,
                     from_index_of_shaft: int = None, to_index_shaft: int = None) -> None:
        _is_disk_in_motion = diameter_of_disk_in_motion is not None and \
                             from_index_of_shaft is not None and \
                             to_index_shaft is not None

        self.scene().clear()

        self.__draw_shafts(len(scheme), sum(map(lambda sh_sc: len(sh_sc), scheme)) + _is_disk_in_motion)

        for shaft, shaft_scheme in zip(self._shafts, scheme):
            for disk_index, disk_diameter in enumerate(shaft_scheme):
                self.scene().addItem(Disk(shaft[disk_index], disk_diameter))

        if _is_disk_in_motion:
            _disks_sum = sum(map(len, scheme))

            point_from = self._shafts[from_index_of_shaft][_disks_sum + 3]
            point_to = self._shafts[to_index_shaft][_disks_sum + 3]

            disk_in_motion_pos = QPoint(min(point_from.x(), point_to.x()) + abs(point_from.x() - point_to.x()) // 2,
                                        point_from.y())
            self.scene().addItem(Disk(disk_in_motion_pos, diameter_of_disk_in_motion))
