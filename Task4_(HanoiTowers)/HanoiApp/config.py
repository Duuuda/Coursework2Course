class HAConfig:
    student_id = '70150235'
    student_name = 'Чунихин Вадим Андреевич'
    font = 'Calibri'
    font_size = 16
    title = 'HanoiTower'
    size = 850, 700
    min_size = 800, 650
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
                border-radius: 13px;
            }
            
            QPushButton:hover
            {
                background-color: #396D45;
            }
            
            QPushButton:pressed
            {
                background-color: #2E5737;
            }
            
            QLineEdit
            {
                border-radius: 13px;
            }
            
            QLineEdit:hover
            {
                background-color: #5AA96C;
            }
        """
