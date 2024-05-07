from PySide6.QtWidgets import QLineEdit
from constants import *
from PySide6.QtCore import Qt
class Display(QLineEdit):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()
        
    def config_style(self):
        self.setStyleSheet(f'font-size:{BIG_FONT_SIZE}px;')
        self.setMinimumHeight(2 * BIG_FONT_SIZE)
        self.setMinimumWidth(MINIMUN_WIDHT)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[DEFAULT_TXT_MARGIN for _ in range(4)])
        
        