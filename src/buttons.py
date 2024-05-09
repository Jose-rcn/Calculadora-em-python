from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from constants import *
class Button(QPushButton):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()
        
    def config_style(self):
        font = self.font()
        font.setPixelSize(BIG_FONT_SIZE)
        self.setFont(font)
        
        self.setMinimumSize(MINIMUN_BTN_W,MINIMUN_BTN_H)
        
class ButtonsGrid(QGridLayout):
    def __init__(self,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)