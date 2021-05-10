from PyQt5.QtWidgets import QLabel
from DBORM.models import Iteration


class InfoDisplay(QLabel):
    def show_info(self, database_obj: Iteration) -> None:
        _iter_number = int(database_obj.number) if database_obj.number.is_integer() else round(database_obj.number, 3)
        if database_obj.disk_in_motion is not None:
            self.setText(f'{database_obj.percent}% | '
                         f'Итерация № {_iter_number} | '
                         f'Диск № {database_obj.disk_in_motion} '
                         f'перемещен с вала № {database_obj.from_name} на вал № {database_obj.to_name}')
        else:
            self.setText(f'{database_obj.percent}% | Итерация № {_iter_number}')
