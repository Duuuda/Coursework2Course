from SimpleMode import SimpleModeUI, SimpleModeBackend
from ExtendedMode import ExtendedModeUI, ExtendedModeBackend


# General settings
_default_student_id = '70150235'
_default_student_name = 'Чунихин Вадим Андреевич'


# Simple mode settings

class SMConfig:
    student_id = _default_student_id
    student_name = _default_student_name
    ui = SimpleModeUI
    backend = SimpleModeBackend
    font = 'Calibri'
    title = 'Calculator - normal mode'
    size = 350, 500
    min_size = 300, 450
    resizable = True, True
    style_sheet = \
        """
            *
            {
                background-color: #448352;
                color: #FFFFFF;
                border: 0;
            }
            
            QPushButton
            {
                border-radius: 15px;
            }
            
            QPushButton:hover
            {
                background-color: #396D45;
            }
            
            QPushButton:pressed
            {
                background-color: #2E5737;
            }
        """


# Extended mode settings
class EMConfig:
    student_id = _default_student_id
    student_name = _default_student_name
    ui = ExtendedModeUI
    backend = ExtendedModeBackend
    font = 'Calibri'
    title = 'Calculator - extended mode'
    size = 450, 750
    min_size = 400, 700
    resizable = True, True
    style_sheet = \
        """
            *
            {
                background-color: #448352;
                color: #FFFFFF;
                border: 0;
            }
            
            QPushButton
            {
                border-radius: 15px;
            }
            
            QPushButton:hover
            {
                background-color: #396D45;
            }
            
            QPushButton:pressed
            {
                background-color: #2E5737;
            }
        """
