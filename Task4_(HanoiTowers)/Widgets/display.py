from PyQt5.QtWidgets import QGraphicsScene
from json import loads
from BaseObjects import BasePainter
from DBORM.models import Iteration


class Display(BasePainter):
    def __init__(self,
                 screen_width: int = 800, screen_height: int = 500,
                 _scene: QGraphicsScene = None,  # This scene will be cleaned up!
                 _antialiasing: bool = True
                 ):
        super(Display, self).__init__(screen_width, screen_height, _scene, _antialiasing)

    def show_stage(self, database_obj: Iteration, _shafts_separator: str = '|', _disks_separator: str = '-') -> None:
        self._draw_scheme(loads(database_obj.scheme),
                          database_obj.disk_in_motion,
                          database_obj.from_index,
                          database_obj.to_index)
